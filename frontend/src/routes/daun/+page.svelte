<script>
  import { onMount } from 'svelte';

  let canvas;
  let ctx;
  let leaves = [];

  // Fungsi untuk membuat daun baru
  function createLeaf() {
    const side = Math.random() < 0.5 ? -20 : canvas.width + 20;
    return {
      x: side,
      y: Math.random() * canvas.height,
      speedX: Math.random() * 2 - 1,
      speedY: Math.random() * 2 - 1,
      rotation: Math.random() * 2 * Math.PI,
      rotationSpeed: Math.random() * 0.01 - 0.005,
    };
  }

  onMount(() => {
    ctx = canvas.getContext('2d');

    // Buat daun awal
    for (let i = 0; i < 100; i++) {
      leaves.push(createLeaf());
    }

    // Mulai animasi
    requestAnimationFrame(animate);
  });

  function animate() {
    // Bersihkan kanvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Gambar dan perbarui setiap daun
    for (const leaf of leaves) {
      ctx.save();
      ctx.translate(leaf.x, leaf.y);
      ctx.rotate(leaf.rotation);
      ctx.beginPath();
      ctx.moveTo(0, 0);
      ctx.quadraticCurveTo(10, 10, 20, 0);
      ctx.quadraticCurveTo(10, -10, 0, 0);
      ctx.fillStyle = 'green';
      ctx.fill();
      ctx.restore();

      leaf.x += leaf.speedX;
      leaf.y += leaf.speedY;
      leaf.rotation += leaf.rotationSpeed;

      // Jika daun telah jatuh dari kanvas, buat daun baru
      if (leaf.x < -20 || leaf.x > canvas.width + 20 || leaf.y < -20 || leaf.y > canvas.height + 20) {
        Object.assign(leaf, createLeaf());
      }
    }

    // Panggil fungsi ini lagi pada frame berikutnya
    requestAnimationFrame(animate);
  }
</script>

{#if typeof window !== 'undefined'}
  <canvas bind:this={canvas} width={window.innerWidth} height={window.innerHeight}></canvas>
{/if}
