<script>
  import { onMount } from 'svelte';
  import * as THREE from 'three';

  let container;
  let camera, scene, renderer;
  let leaves = [];

  onMount(() => {
    init();
    animate();
  });

  function init() {
    camera = new THREE.PerspectiveCamera(70, window.innerWidth / window.innerHeight, 0.01, 10);
    camera.position.z = 1;

    scene = new THREE.Scene();

    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    container.appendChild(renderer.domElement);

    for (let i = 0; i < 100; i++) {
      const geometry = new THREE.ShapeGeometry(createLeafShape());
      const material = new THREE.MeshBasicMaterial({ color: 'green', side: THREE.DoubleSide });
      const leaf = new THREE.Mesh(geometry, material);
      leaf.position.x = Math.random() - 0.5;
      leaf.position.y = Math.random() - 0.5;
      leaf.position.z = Math.random() - 0.5;
      leaf.rotation.x = Math.random() * 2 * Math.PI;
      leaf.rotation.y = Math.random() * 2 * Math.PI;
      leaf.rotation.z = Math.random() * 2 * Math.PI;
      scene.add(leaf);
      leaves.push(leaf);
    }
  }

  function createLeafShape() {
    const shape = new THREE.Shape();
    shape.moveTo(0, 0);
    shape.quadraticCurveTo(2, 4, 5, 20);
    shape.quadraticCurveTo(2, 4, 0, 0);
    return shape;
  }

  function animate() {
    requestAnimationFrame(animate);

    for (const leaf of leaves) {
      leaf.rotation.x += 0.01;
      leaf.rotation.y += 0.01;
    }

    renderer.render(scene, camera);
  }
</script>

<div class="fixed top-0 right-0 bottom-0 z-[-1]" bind:this={container}></div>