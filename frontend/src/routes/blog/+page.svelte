<script>
import Kartu from "$lib/Kartu.svelte"

let artikel = [
  {
    thumbnail: "",
    judul: "Judul",
    isi: "Isi"
  },
  {
    thumbnail: "",
    judul: "Judul",
    isi: "Isi"
  },
  {
    thumbnail: "",
    judul: "Judul",
    isi: "Isi"
  },
  {
    thumbnail: "",
    judul: "Judul",
    isi: "Isi"
  },
  {
    thumbnail: "",
    judul: "Judul",
    isi: "Isi"
  },
  {
    thumbnail: "",
    judul: "Judul",
    isi: "Isi"
  }
]
</script>

<div class="bg-black h-screen flex justify-center items-center">
  <Kartu artikel={artikel}/>
</div>

<button class="block m-auto bg-emerald-500 p-3 rounded-md text-emerald-100 mt-[50px]">More</button>