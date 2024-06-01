<div class="text-green-400 text-xl p-5 hover:bg-green-500 hover:text-white">
  <button on:click={klikPencarian}>Search</button>
</div>

{#if tampilkanPencarian}
<div class="fixed flex justify-center items-center top-0 right-0 bottom-0 left-0 bg-black bg-opacity-50 z-20">
  <input class="rounded-md p-3" type="text"/>
  <button class="rounded-md p-3 bg-black text-white ml-2">Cari</button>
  <button class="absolute bottom-[20%] bg-black text-white w-[50px] h-[50px] rounded-full" on:click={tutupPencarian}>X</button>
</div>
{/if}

<script>
  let tampilkanPencarian = false
  
  function klikPencarian(){
    tampilkanPencarian = true
  }
  
  function tutupPencarian(){
    tampilkanPencarian = false
  }
</script>