<!-- src/components/WaveAnimation.svelte -->
<script>
  import { onMount } from 'svelte';
  let canvas;
  
  onMount(() => {
    const ctx = canvas.getContext('2d');
    const wave = {
      amplitude: 50,
      frequency: 0.01,
      phase: 0,
      speed: 0.1,
      yOffset: 100,
      fillStyle: '#3182CE'
    };
    
    function animate() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.beginPath();
      for (let x = 0; x < canvas.width; x += 10) {
        const y = wave.amplitude * Math.sin(wave.frequency * x + wave.phase) + wave.yOffset;
        ctx.lineTo(x, y);
      }
      ctx.lineTo(canvas.width, canvas.height);
      ctx.lineTo(0, canvas.height);
      ctx.closePath();
      ctx.fillStyle = wave.fillStyle;
      ctx.fill();
      wave.phase += wave.speed;
      requestAnimationFrame(animate);
    }
    
    animate();
  });
</script>

<canvas bind:this={canvas} class="w-full h-20 absolute bottom-[100%]"></canvas>
