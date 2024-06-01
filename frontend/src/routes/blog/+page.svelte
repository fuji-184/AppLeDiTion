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
  }
]
</script>

<Kartu artikel={artikel}/>

<button class="block m-auto bg-green-600 p-3 rounded-md text-white mt-[50px]">More</button>