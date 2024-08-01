<script>
  import { onMount } from "svelte";
  import io from "socket.io-client";
  import { fetcher } from "$lib/utils/fetcher.js"
  import { goto } from "$app/navigation"

  let socket;
  $: pesan = [];
  let pesan_baru = "";
  const id_user = JSON.parse(localStorage.getItem("id"))
  const nama = JSON.parse(localStorage.getItem("nama"))

  // Inisialisasi koneksi socket saat komponen dimuat
  onMount(() => {
    if (!id_user){
      goto("/masuk")
    }

    ambilPesan()

    socket = io("http://127.0.0.1:5000"); // Ganti dengan URL server Anda

    // Event listener untuk menerima pesan dari server
    socket.on("pesan_diterima", (data) => {
      pesan = [...pesan, data];
      console.log(pesan)
    });

    return () => {
      // Tutup koneksi socket saat komponen dilepas
      socket.disconnect();
    };
  });

  async function ambilPesan(){
    const res = await fetcher({
      path: "/chat"
    })

    pesan = res.hasil
  }

  function kirimPesan() {
    const message = {
      id_user: id_user,
      nama: nama,
      pesan: pesan_baru
    };

    // Kirim pesan ke server
    socket.emit("kirim_pesan", message);

    pesan_baru = "";
  }
</script>

<div>
  <div class="flex flex-col gap-4 p-5 overflow-y-auto pb-[160px] md:pb-[96px]">
    {#if pesan}
      {#each pesan as p}
        <div class="max-w-max bg-gradient-to-r from-emerald-500 to-teal-500 p-4 rounded-lg" class:self-end={p.id_user == id_user}>
          <p class="mb-1 text-green-300 text-md font-semibold">{p.nama}</p>
          <p class="text-emerald-100 text-sm">{p.pesan}</p>
        </div>
      {/each}
    {/if}
  </div>
  <div class="fixed grid grid-cols-[80%,auto] justify-center place-content-center gap-3 left-0 right-0 bottom-[60px] md:bottom-0 z-20 bg-gradient-to-b from-emerald-500 via-black to-black p-4">
    <input type="text" placeholder="Pesan...." bind:value={pesan_baru} class="bg-black text-white p-3 rounded-md focus:outline-none placeholder-emerald-500" />
    <button on:click={kirimPesan} class="bg-black text-emerald-500 p-3 rounded-md">Kirim</button>
  </div>
</div>

<a class="bg-blue text-emerald-500 text-md font-semibold z-40 fixed bottom-[24px] left-[24px]" href="/">
  Home
</a>