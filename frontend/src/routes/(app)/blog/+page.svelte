<script>
  import Kartu from "$lib/Kartu.svelte";
  import { fetcher } from "$lib/utils/fetcher.js";
  import { onMount } from "svelte";

  let artikel = [];
  let jumlah_artikel = 0;
  let artikel_tampil = [];
  let i_awal = 0;

  function setting_artikel(e = null, jumlah_tampil = 5) {
    const artikel_baru = artikel.slice(i_awal, i_awal + jumlah_tampil);
    if (artikel_baru.length > 0) {
      artikel_tampil = [...artikel_tampil, ...artikel_baru];
      i_awal += jumlah_tampil;
    }

    if (i_awal >= jumlah_artikel && e) {
      e.target.style.display = "none";
    }
  }

  onMount(async () => {
    artikel = await fetcher({
      path: "/artikel",
      method: "GET"
    });
    artikel = artikel.data;
    jumlah_artikel = artikel.length;
    setting_artikel();
  });
</script>

<div class="bg-gradient-to-br from-black via-black to-emerald-950 pb-16">
  <div class="flex justify-center items-center min-h-screen">
    <Kartu artikel={artikel_tampil}/>
  </div>

  <button on:click={(e) => setting_artikel(e, 5)} class="block m-auto bg-emerald-500 p-3 rounded-md text-emerald-100 mt-[px]">More</button>
</div>