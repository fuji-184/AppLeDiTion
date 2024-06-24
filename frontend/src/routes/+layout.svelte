<div class="h-screen bg-black">
  <Navigasi/>
  <slot/>
</div>

<script>
        import "../app.css"
        import Navigasi from "$lib/Navigasi.svelte"
        
        import eruda from 'eruda';
        eruda.init();
        
</script>