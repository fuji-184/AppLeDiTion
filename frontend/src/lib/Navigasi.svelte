<script>
  import Pencarian from "$lib/Pencarian.svelte"
  import Notif from "$lib/Notif.svelte"
  import { goto } from "$app/navigation"
  import { onMount } from "svelte";
  import {Howl} from 'howler';

  $: nama = null

  onMount(() => {
    nama = JSON.parse(localStorage.getItem("nama"))
    console.log(nama)
  })

  let menu = [
    { label: "Home", href: "/", active: true, icon: '<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="1.5em" width="1.5em"><path fill="currentColor" d="M11 39h7.5V26.5h11V39H37V19.5L24 9.75 11 19.5Zm0 3q-1.25 0-2.125-.875T8 39V19.5q0-.7.325-1.35.325-.65.875-1.05l13-9.75q.4-.3.85-.45.45-.15.95-.15.5 0 .95.15.45.15.85.45l13 9.75q.55.4.875 1.05.325.65.325 1.35V39q0 1.25-.875 2.125T37 42H26.5V29.5h-5V42Zm13-17.65Z"/></svg>' },
    { label: "Dashboard", href: "/dashboard", active: false, icon: '<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="1.5em" width="1.5em"><path fill="currentColor" d="M24 39.8q-2.95 0-5.525-.975T13.8 36.1l-3.1 3.1q-.45.45-1.05.45-.6 0-1.05-.45-.45-.45-.45-1.05 0-.6.45-1.05l3.1-3.1q-1.75-2.1-2.725-4.675Q8 26.75 8 23.8q0-6.7 4.65-11.35Q17.3 7.8 24 7.8h16v16q0 6.7-4.65 11.35Q30.7 39.8 24 39.8Zm0-3q5.4 0 9.2-3.8 3.8-3.8 3.8-9.2v-13H24q-5.4 0-9.2 3.8-3.8 3.8-3.8 9.2 0 2.3.75 4.375T13.8 31.9l10.8-10.8q.45-.45 1.05-.45.6 0 1.05.45.45.45.45 1.075t-.45 1.075L15.9 34q1.65 1.3 3.725 2.05 2.075.75 4.375.75Z"/></svg>' },
    { label: "Detect", href: "/detection", active: false, icon: '<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="1.5em" width="1.5em"><path fill="currentColor" d="M24 39.8q-2.95 0-5.525-.975T13.8 36.1l-3.1 3.1q-.45.45-1.05.45-.6 0-1.05-.45-.45-.45-.45-1.05 0-.6.45-1.05l3.1-3.1q-1.75-2.1-2.725-4.675Q8 26.75 8 23.8q0-6.7 4.65-11.35Q17.3 7.8 24 7.8h16v16q0 6.7-4.65 11.35Q30.7 39.8 24 39.8Zm0-3q5.4 0 9.2-3.8 3.8-3.8 3.8-9.2v-13H24q-5.4 0-9.2 3.8-3.8 3.8-3.8 9.2 0 2.3.75 4.375T13.8 31.9l10.8-10.8q.45-.45 1.05-.45.6 0 1.05.45.45.45.45 1.075t-.45 1.075L15.9 34q1.65 1.3 3.725 2.05 2.075.75 4.375.75Z"/></svg>' },
    { label: "Blog", href: "/blog", active: false, icon: '<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="1.5em" width="1.5em"><path fill="currentColor" d="M15.35 34.05H26.1q.65 0 1.075-.425.425-.425.425-1.075 0-.65-.425-1.075-.425-.425-1.075-.425H15.35q-.65 0-1.075.425-.425.425-.425 1.075 0 .65.425 1.075.425.425 1.075.425Zm0-8.55h17.3q.65 0 1.075-.425.425-.425.425-1.075 0-.65-.425-1.075-.425-.425-1.075-.425h-17.3q-.65 0-1.075.425-.425.425-.425 1.075 0 .65.425 1.075.425.425 1.075.425Zm0-8.55h17.3q.65 0 1.075-.425.425-.425.425-1.075 0-.65-.425-1.075-.425-.425-1.075-.425h-17.3q-.65 0-1.075.425-.425.425-.425 1.075 0 .65.425 1.075.425.425 1.075.425ZM9 42q-1.2 0-2.1-.9Q6 40.2 6 39V9q0-1.2.9-2.1Q7.8 6 9 6h30q1.2 0 2.1.9.9.9.9 2.1v30q0 1.2-.9 2.1-.9.9-2.1.9Zm0-3h30V9H9v30Zm0 0V9v30Z"/></svg>' },
    { label: "Forum", href: "/forum", active: false, icon: '<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="1.5em" width="1.5em"><path fill="currentColor" d="M4 32.2V6.1q0-.7.65-1.4T6 4h25.95q.75 0 1.4.675Q34 5.35 34 6.1v17.8q0 .7-.65 1.4t-1.4.7H12l-6.7 6.7q-.35.35-.825.175T4 32.2ZM7 7v16V7Zm7.05 29q-.7 0-1.375-.7T12 33.9V29h25V12h5q.7 0 1.35.7.65.7.65 1.45v28q0 .5-.475.675-.475.175-.825-.175L36.05 36ZM31 7H7v16h24Z"/></svg>' }
  ];

  let activeMenu = menu.find(item => item.active)?.href || menu[0].href;
  let tampilkanPencarian = false;
  let tampilkanProfil = false
  let muncul = false, pesan = ""

  function setActiveMenu(href) {
  	sound.play()
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

  function klikProfil() {
    tampilkanProfil = !tampilkanProfil
    activeMenu = "profil";  // Set activeMenu to "search" when search is clicked
  }

  function keluar(){
    localStorage.removeItem("token")
    localStorage.removeItem("id")
    localStorage.removeItem("nama")

    pesan = "Logout berhasil"
    muncul = true

    window.location.href = "/"
  }

  // let scrolled = false;

  // onMount(() => {
  //   const handleScroll = () => {
  //     scrolled = window.scrollY > 50;
  //   };

  //   window.addEventListener('scroll', handleScroll);
  //   return () => {
  //     window.removeEventListener('scroll', handleScroll);
  //   };
  // });
  
	let sound = new Howl({
		src: ['http://127.0.0.1:5173/click.wav'],
		// html5: true
	})
</script>

<header class="z-10 h-auto p-0 fixed bottom-0 left-0 right-0 flex justify-center bg-black text-black box-border h-[80px] md:justify-center md:fixed md:bottom-[8px] md:bg-transparent">
  <div class="md:rounded-lg md:bg-[rgba(0,0,0,0.8)] relative grid grid-cols-7 text-emerald-500 place-items-center place-content-center font-bold">
    {#each menu as m}
    <div class="relative h-[100%] w-auto box-border">
      <a href="{m.href}" class="md:bg-none md:hover:bg-none p-4 flex justify-center items-center box-border w-[100%] h-[100%] hover:bg-gradient-to-b from-black via-black to-emerald-600 hover:text-white {activeMenu === m.href ? 'bg-gradient-to-b from-black via-black to-emerald-60 text-white' : ''}" on:click="{() => setActiveMenu(m.href)}">
        <span class="flex justify-center items-center flex-col hover:animate-blink {activeMenu === m.href ? 'text-white' : ''} text-sm drop-shadow-[0_10px_8px_rgba(16,185,129,1)]">
          {@html m.icon}
          {m.label}
          </span>
      </a>
      </div>
    {/each}

    <div class="relative h-[100%] w-auto box-border cursor-pointer">
      <span class="md:bg-none md:hover:bg-none p-4 flex justify-center items-center box-border w-[100%] h-[100%] hover:bg-gradient-to-b from-black via-black to-emerald-600 hover:text-white {activeMenu === 'search' ? 'bg-gradient-to-b from-black via-black to-emerald-60 text-white' : ''}" on:click="{() => klikPencarian()}">
        <span class="flex justify-center items-center flex-col hover:animate-blink {activeMenu === 'search' ? 'text-white' : ''} text-sm">
      <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="1.5em" width="1.5em"><path fill="currentColor" d="M38.7 40.85 26.65 28.8q-1.5 1.3-3.5 2.025-2 .725-4.25.725-5.4 0-9.15-3.75T6 18.75q0-5.3 3.75-9.05 3.75-3.75 9.1-3.75 5.3 0 9.025 3.75 3.725 3.75 3.725 9.05 0 2.15-.7 4.15-.7 2-2.1 3.75L40.95 38.7q.45.4.45 1.025 0 .625-.5 1.125-.45.45-1.1.45-.65 0-1.1-.45Zm-19.85-12.3q4.05 0 6.9-2.875Q28.6 22.8 28.6 18.75t-2.85-6.925Q22.9 8.95 18.85 8.95q-4.1 0-6.975 2.875T9 18.75q0 4.05 2.875 6.925t6.975 2.875Z"/></svg>
      Search
      </span>
      </span>
    </div>

    {#if nama}
      <button on:click={klikProfil} class="relative h-[100%] w-auto box-border">
        <span class="md:bg-none md:hover:bg-none p-4 flex justify-center items-center box-border w-[100%] h-[100%] hover:bg-gradient-to-b from-black via-black to-emerald-600 hover:text-white {activeMenu === "profil" ? 'bg-gradient-to-b from-black via-black to-emerald-60 text-white' : ''}">
          <span class="flex justify-center items-center flex-col hover:animate-blink {activeMenu === "profil" ? 'text-white' : ''} text-sm drop-shadow-[0_10px_8px_rgba(16,185,129,1)]">
            <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="1.5em" width="1.5em"><path fill="currentColor" d="M20 23.75q-3.3 0-5.4-2.1-2.1-2.1-2.1-5.4 0-3.3 2.1-5.4 2.1-2.1 5.4-2.1 3.3 0 5.4 2.1 2.1 2.1 2.1 5.4 0 3.3-2.1 5.4-2.1 2.1-5.4 2.1ZM5.5 39.8q-.65 0-1.075-.425Q4 38.95 4 38.3v-3.2q0-1.75.875-3.15T7.4 29.8q3.6-1.6 6.675-2.3 3.075-.7 5.925-.7h1.15q-.3.7-.45 1.375-.15.675-.25 1.625H20q-2.9 0-5.675.625T8.6 32.5q-.8.4-1.2 1.125Q7 34.35 7 35.1v1.7h13.45q.25.9.6 1.625t.85 1.375ZM20 20.75q1.95 0 3.225-1.275Q24.5 18.2 24.5 16.25q0-1.95-1.275-3.225Q21.95 11.75 20 11.75q-1.95 0-3.225 1.275Q15.5 14.3 15.5 16.25q0 1.95 1.275 3.225Q18.05 20.75 20 20.75Zm0-4.5Zm.45 20.55Zm14.25-.85q1.65 0 2.825-1.175Q38.7 33.6 38.7 31.95q0-1.65-1.175-2.825Q36.35 27.95 34.7 27.95q-1.65 0-2.825 1.175Q30.7 30.3 30.7 31.95q0 1.65 1.175 2.825Q33.05 35.95 34.7 35.95Zm-1.85 2.75q-.85-.25-1.725-.725-.875-.475-1.475-1.075l-2.2.5q-.25.1-.5 0t-.35-.35l-.65-1.15q-.15-.2-.1-.45.05-.25.25-.45l1.9-1.8q-.1-.45-.1-1.25t.1-1.25l-1.9-1.8q-.2-.2-.25-.45-.05-.25.1-.45l.65-1.15q.1-.25.35-.35.25-.1.5 0l2.2.5q.6-.6 1.475-1.075.875-.475 1.725-.725l.4-2.65q.05-.3.25-.475t.5-.175h1.4q.3 0 .5.175t.25.475l.4 2.65q.85.25 1.725.725.875.475 1.475 1.075l2.2-.5q.25-.1.5 0t.35.35l.65 1.15q.15.2.1.45-.05.25-.25.45l-1.9 1.8q.1.45.1 1.25t-.1 1.25l1.9 1.8q.2.2.25.45.05.25-.1.45l-.65 1.15q-.1.25-.35.35-.25.1-.5 0l-2.2-.5q-.6.6-1.475 1.075-.875.475-1.725.725l-.4 2.65q-.05.3-.25.475t-.5.175H34q-.3 0-.5-.175t-.25-.475Z"/></svg>
            {nama}
            </span>
          </span>
        </button>
    {/if}

    {#if tampilkanProfil}
      <div class="z-10 shadow-lg hover:bg-black p-4 rounded-lg bg-gradient-to-r from-emerald-500 to-teal-500 text-emerald-100 text-sm font-semibold absolute bottom-[110%] right-0">
        <button on:click={keluar}>Keluar</button>
      </div>
    {/if}

  </div>
</header>

{#if tampilkanPencarian}
  <div class="fixed flex justify-center items-center top-0 right-0 bottom-0 left-0 bg-black bg-opacity-50 z-20">
    <input class="rounded-md p-3" type="text"/>
    <button class="rounded-md p-3 bg-black text-white ml-2">Cari</button>
    <button class="absolute bottom-[20%] bg-black text-white w-[50px] h-[50px] rounded-full" on:click={tutupPencarian}>X</button>
  </div>
{/if}

<Notif muncul={muncul} pesan={pesan}/>

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


.hover {
  border-radius: 12px;
  background: none;
}

.hover:hover {
  border-radius: 12px;
  background: none;
}

.background {
  background-color: rgba(0, 0, 0, 0.8);
  border-radius: 12px;
}


</style>
