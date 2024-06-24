<script>
  import { onMount } from "svelte"
  import io from "socket.io-client"

  $: pesan = []
  
  let pesan_baru = ""
  
  function kirimPesan(){
    pesan = [...pesan, {
      nama: "fuji",
      isi: pesan_baru
    }]
    pesan_baru = ""
  }
</script>

<div>
  <div class="flex flex-col gap-2 p-5">
    {#each pesan as p}
      <div class="bg-black text-white p-4 rounded-md">
        <p class="mb-1 text-green-300">{p.nama}</p>
        <p class="text-white">{p.isi}</p>
      </div>
    {/each}
  </div>
  <div class="absolute grid grid-cols-[80%,auto] justify-center place-content-center gap-3 left-0 right-0 bottom-[60px] z-50 bg-gradient-to-b from-green-600 via-black to-black p-4">
    <input type="text" placeholder="Pesan...." bind:value={pesan_baru} class="bg-black text-white p-3 rounded-md focus:outline-none placeholder-green-600" />
    <button on:click={kirimPesan} class="bg-black text-green-600 p-3 rounded-md">Kirim</button>
  </div>
</div>