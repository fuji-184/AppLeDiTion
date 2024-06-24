<script>
  import Pencarian from "$lib/Pencarian.svelte";

  let menu = [
    { label: "Home", href: "/", active: true, icon: '<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="1.5em" width="1.5em"><path fill="currentColor" d="M11 39h7.5V26.5h11V39H37V19.5L24 9.75 11 19.5Zm0 3q-1.25 0-2.125-.875T8 39V19.5q0-.7.325-1.35.325-.65.875-1.05l13-9.75q.4-.3.85-.45.45-.15.95-.15.5 0 .95.15.45.15.85.45l13 9.75q.55.4.875 1.05.325.65.325 1.35V39q0 1.25-.875 2.125T37 42H26.5V29.5h-5V42Zm13-17.65Z"/></svg>' },
    { label: "Detect", href: "/detection", active: false, icon: '<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="1.5em" width="1.5em"><path fill="currentColor" d="M24 39.8q-2.95 0-5.525-.975T13.8 36.1l-3.1 3.1q-.45.45-1.05.45-.6 0-1.05-.45-.45-.45-.45-1.05 0-.6.45-1.05l3.1-3.1q-1.75-2.1-2.725-4.675Q8 26.75 8 23.8q0-6.7 4.65-11.35Q17.3 7.8 24 7.8h16v16q0 6.7-4.65 11.35Q30.7 39.8 24 39.8Zm0-3q5.4 0 9.2-3.8 3.8-3.8 3.8-9.2v-13H24q-5.4 0-9.2 3.8-3.8 3.8-3.8 9.2 0 2.3.75 4.375T13.8 31.9l10.8-10.8q.45-.45 1.05-.45.6 0 1.05.45.45.45.45 1.075t-.45 1.075L15.9 34q1.65 1.3 3.725 2.05 2.075.75 4.375.75Z"/></svg>' },
    { label: "Blog", href: "/blog", active: false, icon: '<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="1.5em" width="1.5em"><path fill="currentColor" d="M15.35 34.05H26.1q.65 0 1.075-.425.425-.425.425-1.075 0-.65-.425-1.075-.425-.425-1.075-.425H15.35q-.65 0-1.075.425-.425.425-.425 1.075 0 .65.425 1.075.425.425 1.075.425Zm0-8.55h17.3q.65 0 1.075-.425.425-.425.425-1.075 0-.65-.425-1.075-.425-.425-1.075-.425h-17.3q-.65 0-1.075.425-.425.425-.425 1.075 0 .65.425 1.075.425.425 1.075.425Zm0-8.55h17.3q.65 0 1.075-.425.425-.425.425-1.075 0-.65-.425-1.075-.425-.425-1.075-.425h-17.3q-.65 0-1.075.425-.425.425-.425 1.075 0 .65.425 1.075.425.425 1.075.425ZM9 42q-1.2 0-2.1-.9Q6 40.2 6 39V9q0-1.2.9-2.1Q7.8 6 9 6h30q1.2 0 2.1.9.9.9.9 2.1v30q0 1.2-.9 2.1-.9.9-2.1.9Zm0-3h30V9H9v30Zm0 0V9v30Z"/></svg>' },
    { label: "Forum", href: "/forum", active: false, icon: '<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="1.5em" width="1.5em"><path fill="currentColor" d="M4 32.2V6.1q0-.7.65-1.4T6 4h25.95q.75 0 1.4.675Q34 5.35 34 6.1v17.8q0 .7-.65 1.4t-1.4.7H12l-6.7 6.7q-.35.35-.825.175T4 32.2ZM7 7v16V7Zm7.05 29q-.7 0-1.375-.7T12 33.9V29h25V12h5q.7 0 1.35.7.65.7.65 1.45v28q0 .5-.475.675-.475.175-.825-.175L36.05 36ZM31 7H7v16h24Z"/></svg>' }
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

<header class="z-10 h-auto p-0 fixed bottom-0 left-0 right-0 flex justify-center bg-black text-black sm:static sm:justify-between box-border h-[80px]">
  <div class="grid grid-cols-5 text-green-500 place-items-center place-content-center font-bold">
    {#each menu as m}
    <div class="relative h-[100%] w-auto box-border">
      <a href="{m.href}" class="p-4 flex justify-center items-center box-border w-[100%] h-[100%] hover:bg-gradient-to-b from-black via-black to-green-600 hover:text-white {activeMenu === m.href ? 'bg-gradient-to-b from-black via-black to-green-60 text-white' : ''}" on:click="{() => setActiveMenu(m.href)}">
        <span class="flex justify-center items-center flex-col hover:animate-blink {activeMenu === m.href ? 'text-white' : ''} text-sm">
          {@html m.icon}
          {m.label}
          </span>
      </a>
      </div>
    {/each}
    <div class="relative h-[100%] w-auto box-border">
      <span class="p-4 flex justify-center items-center box-border w-[100%] h-[100%] hover:bg-gradient-to-b from-black via-black to-green-600 hover:text-white {activeMenu === 'search' ? 'bg-gradient-to-b from-black via-black to-green-60 text-white' : ''}" on:click="{() => klikPencarian()}">
        <span class="flex justify-center items-center flex-col hover:animate-blink {activeMenu === 'search' ? 'text-white' : ''} text-sm">
      <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="1.5em" width="1.5em"><path fill="currentColor" d="M38.7 40.85 26.65 28.8q-1.5 1.3-3.5 2.025-2 .725-4.25.725-5.4 0-9.15-3.75T6 18.75q0-5.3 3.75-9.05 3.75-3.75 9.1-3.75 5.3 0 9.025 3.75 3.725 3.75 3.725 9.05 0 2.15-.7 4.15-.7 2-2.1 3.75L40.95 38.7q.45.4.45 1.025 0 .625-.5 1.125-.45.45-1.1.45-.65 0-1.1-.45Zm-19.85-12.3q4.05 0 6.9-2.875Q28.6 22.8 28.6 18.75t-2.85-6.925Q22.9 8.95 18.85 8.95q-4.1 0-6.975 2.875T9 18.75q0 4.05 2.875 6.925t6.975 2.875Z"/></svg>
      Search
      </span>
      </span>
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
