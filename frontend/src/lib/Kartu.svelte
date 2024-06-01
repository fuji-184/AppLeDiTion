{#each artikel as a}
<div class="group w-[100%] rounded-xl shadow-md overflow-hidden md:max-w-2xl">
  <div class="md:flex relative">
    <div class="md:flex-shrink-0">
      <img class="left-0 right-0 top-0 z-40 h-48 w-full object-cover md:w-48 group-hover:scale-125" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQVPbB7pENaEhkc4ps1JbQ4ozMMgmi4BR-ykoUHXkNfA&s" alt="An image">
    </div>
    <div class="rounded-b-xl absolute bottom-0 z-40">
      <div class="p-5 tracking-wide text-lg text-center text-green-500 font-semibold group-hover:drop-shadow-[0_0_10px_green]">{a.judul}</div>
      <p class="hidden p-5 bg-black bg-opacity-50 mt-2 text-gray-500">{a.isi}</p>
    </div>
    <div class="absolute z-30 inset-0 bg-gradient-to-b from-transparent to-black bg-opacity-[20%]">
    </div>
  </div>
</div>
{/each}

<script>
let artikel = [
  {
    judul: "Judul 1",
    isi: "Isi"
  },
  {
    judul: "Judul 2",
    isi: "Isi"
  }
]
</script>
