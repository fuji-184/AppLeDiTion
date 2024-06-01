<div class="bg-gradient-to-b from-black to-green-950 h-screen">
  <Navigasi/>
  <slot/>
</div>

<script>
        import "../app.css"
        import Navigasi from "$lib/Navigasi.svelte"
        
        import eruda from 'eruda';
        eruda.init();
        
</script>