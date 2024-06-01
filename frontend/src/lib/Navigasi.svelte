<script>
  import Pencarian from "$lib/Pencarian.svelte";

  export let menu = [
    { label: "Home", href: "/", active: true },
    { label: "Detect", href: "/detection", active: false },
    { label: "Blog", href: "/blog", active: false },
    { label: "Forum", href: "/forum", active: false }
  ];

  let activeMenu = menu.find(item => item.active)?.href || menu[0].href;
  let tampilkanPencarian = false;

  function setActiveMenu(href) {
    activeMenu = href;
    tampilkanPencarian = false;  // Close search when another menu item is active
  }

  function klikPencarian() {
    tampilkanPencarian = true;
    activeMenu = "search";  // Set activeMenu to "search" when search is clicked
  }

  function tutupPencarian() {
    tampilkanPencarian = false;
    activeMenu = menu.find(item => item.active)?.href || menu[0].href;  // Reset active menu
  }
</script>

<header class="z-10 h-[60px] p-0 fixed bottom-0 left-0 right-0 flex justify-center bg-black text-black sm:static sm:justify-between box-border">
  <div class="grid grid-cols-5 text-green-500 place-items-center place-content-center font-bold">
    {#each menu as m}
      <a href="{m.href}" class="box-border text-xl p-3 hover:bg-gradient-to-b from-black via-black to-green-600 hover:text-white {activeMenu === m.href ? 'bg-gradient-to-b from-black via-black to-green-60 text-white' : ''}" on:click="{() => setActiveMenu(m.href)}">
        <span class="hover:animate-blink {activeMenu === m.href ? 'text-white' : ''}">{m.label}</span>
      </a>
    {/each}
    <div class="text-xl p-3 cursor-pointer hover:bg-gradient-to-b from-black via-black to-green-60 hover:text-white {activeMenu === 'search' ? 'bg-gradient-to-b from-black via-black to-green-60 text-gradient' : 'text-green-400'}" on:click={klikPencarian}>
      Search
    </div>
  </div>
</header>

{#if tampilkanPencarian}
  <div class="fixed flex justify-center items-center top-0 right-0 bottom-0 left-0 bg-black bg-opacity-50 z-20">
    <input class="rounded-md p-3" type="text"/>
    <button class="rounded-md p-3 bg-black text-white ml-2">Cari</button>
    <button class="absolute bottom-[20%] bg-black text-white w-[50px] h-[50px] rounded-full" on:click={tutupPencarian}>X</button>
  </div>
{/if}

<style>
  @keyframes gradient {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

.text-gradient {
  
  background-size: 400% 400%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gradient 3s ease infinite;
}

@keyframes blink {
  0%, 49% { opacity: 0; }
  50%, 100% { opacity: 1; }
}

.animate-blink {
  animation: blink 0.6s ease-in-out infinite;
}


</style>
