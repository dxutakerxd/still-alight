import './style.css';

const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
let reducedMotion = motionQuery.matches;
const motionButton = document.querySelector('#motion-toggle');
function updateMotion(value) {
  reducedMotion = value;
  document.documentElement.classList.toggle('reduced-motion', value);
  document.documentElement.dataset.reducedMotion = String(value);
  if (motionButton) {
    motionButton.setAttribute('aria-pressed', String(value));
    motionButton.textContent = value ? 'Motion off' : 'Motion on';
    motionButton.setAttribute('aria-label', value ? 'Enable gentle motion' : 'Reduce motion');
  }
  document.dispatchEvent(new CustomEvent('candle-motion-change'));
}
motionButton?.addEventListener('click', () => updateMotion(!reducedMotion));
motionQuery.addEventListener('change', (e) => updateMotion(e.matches));
updateMotion(reducedMotion);

// Only the sound the visitor selects plays. Nothing starts automatically.
const audioPlayers = [...document.querySelectorAll('audio')];
audioPlayers.forEach((player) => {
  player.volume = 0.5;
  player.addEventListener('play', () => audioPlayers.forEach((other) => {
    if (other !== player) other.pause();
  }));
});
document.addEventListener('visibilitychange', () => {
  if (document.hidden) audioPlayers.forEach((player) => player.pause());
});

const viewer = document.querySelector('#candle-viewer');
const mount = document.querySelector('#candle-canvas') || viewer;
const status = document.querySelector('#candle-status');
const lightButton = document.querySelector('#light-toggle');
const sceneButtons = [...document.querySelectorAll('[data-scene]')];
const rotateButtons = ['#rotate-left', '#rotate-right'].map((id) => document.querySelector(id));
const allControls = [lightButton, ...sceneButtons, ...rotateButtons].filter(Boolean);
allControls.forEach((button) => { button.disabled = true; });

async function initCandle() {
  const THREE = await import('three');
  const { GLTFLoader } = await import('three/addons/loaders/GLTFLoader.js');
  const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true, powerPreference: 'low-power' });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.7));
  renderer.setClearColor(0x000000, 0);
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 0.9;
  const canvas = renderer.domElement;
  canvas.setAttribute('role', 'img');
  canvas.setAttribute('aria-label', 'Interactive Vanilla Blossom candle. Use the buttons below to rotate, change style, or extinguish it.');
  canvas.style.cssText = 'display:block;width:100%;height:100%;touch-action:pan-y;cursor:grab;';
  mount.append(canvas);

  const scene = new THREE.Scene();
  const base = `${import.meta.env.BASE_URL}assets/`;
  const room = await new THREE.TextureLoader().loadAsync(`${base}hero-room.webp`);
  room.colorSpace = THREE.SRGBColorSpace;
  room.mapping = THREE.EquirectangularReflectionMapping;
  const pmrem = new THREE.PMREMGenerator(renderer);
  const env = pmrem.fromEquirectangular(room);
  scene.environment = env.texture;
  room.dispose();
  pmrem.dispose();
  scene.add(new THREE.HemisphereLight(0xfff0d9, 0x46331f, 0.9));
  const key = new THREE.DirectionalLight(0xffe6bc, 2.1);
  key.position.set(-6, 16, 12);
  scene.add(key);
  const rim = new THREE.DirectionalLight(0xffc376, 1.3);
  rim.position.set(8, 12, -6);
  scene.add(rim);

  const camera = new THREE.PerspectiveCamera(35, 1, 0.1, 100);
  camera.position.set(0, 12, 29);
  camera.lookAt(0, 5.2, 0);
  const candle = new THREE.Group();
  candle.scale.setScalar(100);
  scene.add(candle);

  const loader = new GLTFLoader();
  const [model, lidModel, studio] = await Promise.all([
    loader.loadAsync(`${base}candle.glb`),
    loader.loadAsync(`${base}candle-lid.glb`),
    loader.loadAsync(`${base}studio.glb`),
  ]);
  candle.add(model.scene);
  const lid = lidModel.scene;
  lid.position.y = 0.1012;
  lid.visible = false;
  candle.add(lid);
  const coaster = studio.scene.getObjectByName('Studio_Coaster');
  if (coaster) candle.add(coaster);
  const flame = model.scene.getObjectByName('Flame_3D');
  const ember = model.scene.getObjectByName('Wick_EmberTip');
  const label = model.scene.getObjectByName('Label_Decal');
  const waxMaterials = [];
  model.scene.traverse((object) => {
    if (object.isLight) object.intensity = 0;
    if (!object.isMesh) return;
    const material = object.material;
    if (object.name === 'Jar_Glass') {
      // Transparent glass preserves the photographic backdrop; geometry is unchanged.
      material.transmission = 1;
      material.transparent = false;
      material.opacity = 1;
      material.color.set('#fff3df');
      material.roughness = 0.09;
      material.envMapIntensity = 1.3;
      material.depthWrite = true;
      object.renderOrder = 3;
    }
    if (object.name === 'Wax_Body' || object.name === 'Wax_MeltPool') waxMaterials.push(material);
    if (object.name === 'Label_Decal') {
      material.side = THREE.DoubleSide;
      material.roughness = 0.9;
    }
    if (object.name === 'Flame_3D') material.emissiveIntensity = 3;
  });

  const glow = new THREE.PointLight(0xffb450, 2.5, 16, 2);
  glow.position.set(0, 9.4, 1);
  scene.add(glow);
  const palettes = {
    vanilla: { color: '#F1DEC0', name: 'Vanilla Blossom' },
    lavender: { color: '#BEA3D1', name: 'Lavender Fields' },
    cabin: { color: '#CB975C', name: 'Cozy Cabin' },
  };
  const textureLoader = new THREE.TextureLoader();
  const textures = {};
  await Promise.all(Object.keys(palettes).map(async (name) => {
    const texture = await textureLoader.loadAsync(`${base}label-${name}.png`);
    texture.colorSpace = THREE.SRGBColorSpace;
    texture.flipY = false;
    texture.anisotropy = Math.min(renderer.capabilities.getMaxAnisotropy(), 4);
    textures[name] = texture;
  }));

  let lit = true;
  let selected = 'vanilla';
  let active = true;
  let frame = 0;
  let lastTime = 0;
  let pointer = null;
  let dragging = false;
  let closed = 0;
  let closeTarget = 0;
  const announce = () => {
    if (status) status.textContent = `${palettes[selected].name} · ${lit ? 'Your candle is lit' : 'Your candle is resting'}`;
    viewer.dataset.scene = selected;
    viewer.dataset.lit = String(lit);
    canvas.setAttribute('aria-label', `${palettes[selected].name} 3D candle, ${lit ? 'lit' : 'unlit'}. Rotate with the arrow buttons or drag horizontally.`);
    lightButton.setAttribute('aria-pressed', String(lit));
    lightButton.textContent = lit ? 'Extinguish candle' : 'Light the candle';
  };
  function render(time = performance.now()) {
    frame = 0;
    if (!active || document.hidden) return;
    const delta = Math.min((time - lastTime) / 1000, 0.1);
    lastTime = time;
    if (reducedMotion) closed = closeTarget;
    else closed += Math.sign(closeTarget - closed) * Math.min(Math.abs(closeTarget - closed), delta * 1.4);
    lid.visible = closed > 0.005;
    lid.position.y = 0.1012 + (1 - closed) * 0.065;
    lid.position.x = (1 - closed) * 0.022;
    flame.visible = lit || closed < 0.82;
    ember.visible = flame.visible;
    if (flame.morphTargetInfluences) flame.morphTargetInfluences.forEach((_, i, array) => {
      array[i] = reducedMotion || !lit ? 0 : (0.5 + Math.sin(time * 0.0017 + i * 1.8) * 0.5) * 0.45;
    });
    glow.intensity = flame.visible ? 2.5 : 0;
    renderer.render(scene, camera);
    if ((!reducedMotion && lit) || Math.abs(closed - closeTarget) > 0.001) frame = requestAnimationFrame(render);
  }
  function requestRender() {
    if (!frame && active && !document.hidden) frame = requestAnimationFrame(render);
  }
  function setScene(name) {
    if (!palettes[name]) return;
    selected = name;
    waxMaterials.forEach((material) => material.color.set(palettes[name].color));
    label.material.map = textures[name];
    label.material.needsUpdate = true;
    sceneButtons.forEach((button) => button.setAttribute('aria-pressed', String(button.dataset.scene === name)));
    announce();
    requestRender();
  }
  function toggleLight() {
    lit = !lit;
    closeTarget = lit ? 0 : 1;
    announce();
    requestRender();
  }
  lightButton.addEventListener('click', toggleLight);
  sceneButtons.forEach((button) => button.addEventListener('click', () => setScene(button.dataset.scene)));
  rotateButtons.forEach((button, index) => button?.addEventListener('click', () => {
    candle.rotation.y += (index === 0 ? -1 : 1) * Math.PI / 8;
    requestRender();
  }));
  canvas.addEventListener('pointerdown', (event) => {
    if (event.button !== 0) return;
    pointer = { id: event.pointerId, x: event.clientX, y: event.clientY, rotation: candle.rotation.y };
    dragging = false;
  });
  canvas.addEventListener('pointermove', (event) => {
    if (!pointer || pointer.id !== event.pointerId) return;
    const dx = event.clientX - pointer.x;
    const dy = event.clientY - pointer.y;
    if (!dragging && Math.abs(dy) > Math.abs(dx) && Math.abs(dy) > 8) { pointer = null; return; }
    if (Math.abs(dx) > 5) {
      dragging = true;
      canvas.setPointerCapture(event.pointerId);
      canvas.style.cursor = 'grabbing';
      candle.rotation.y = pointer.rotation + dx / Math.max(mount.clientWidth, 1) * Math.PI * 2;
      requestRender();
    }
  });
  canvas.addEventListener('pointerup', (event) => {
    if (pointer && pointer.id === event.pointerId && !dragging) toggleLight();
    pointer = null;
    canvas.style.cursor = 'grab';
  });
  canvas.addEventListener('pointercancel', () => { pointer = null; canvas.style.cursor = 'grab'; });

  const resize = () => {
    const width = mount.clientWidth;
    const height = mount.clientHeight;
    renderer.setSize(width, height, false);
    camera.aspect = width / Math.max(height, 1);
    // Keep the same composition on narrow phones, including the coaster.
    camera.position.z = camera.aspect < 0.8 ? 32 : 29;
    camera.updateProjectionMatrix();
    requestRender();
  };
  new ResizeObserver(resize).observe(mount);
  new IntersectionObserver(([entry]) => {
    active = entry.isIntersecting;
    if (!active && frame) { cancelAnimationFrame(frame); frame = 0; }
    requestRender();
  }, { rootMargin: '80px' }).observe(viewer);
  document.addEventListener('visibilitychange', () => {
    if (document.hidden && frame) { cancelAnimationFrame(frame); frame = 0; }
    requestRender();
  });
  document.addEventListener('candle-motion-change', requestRender);
  canvas.addEventListener('webglcontextlost', (event) => {
    event.preventDefault();
    active = false;
    if (frame) cancelAnimationFrame(frame);
    allControls.forEach((button) => { button.disabled = true; });
    canvas.hidden = true;
    document.querySelector('#candle-fallback').hidden = false;
    status.textContent = 'Candle preview paused. Reload to try the 3D view again.';
  });
  allControls.forEach((button) => { button.disabled = false; });
  document.querySelector('#candle-fallback').hidden = true;
  viewer.dataset.ready = 'true';
  setScene('vanilla');
  resize();
}

initCandle().catch((error) => {
  console.warn('Using Still Alight’s static candle preview:', error.message);
  mount.querySelector('canvas')?.remove();
  allControls.forEach((button) => { button.disabled = true; });
  viewer.dataset.ready = 'fallback';
  if (status) status.textContent = 'Still Alight’s vanilla candle. Interactive 3D is unavailable in this browser.';
});
