<div class="grid grid-cols-1 md:grid-cols-4 gap-16 p-16">
  {#each artikel as a}
    <div class="group rounded-xl shadow-lg shadow-emerald-500 group-hover:shadow-xl group-hover:shadow-emerald-500 overflow-hidden">
      <div class="relative">
        <div class="w-full">
          <img class="h-48 w-full object-cover group-hover:scale-125 transition-transform duration-200 ease-in-out" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQVPbB7pENaEhkc4ps1JbQ4ozMMgmi4BR-ykoUHXkNfA&s" alt="An image">
        </div>
        <div class="rounded-b-xl absolute bottom-0 z-[2] w-full">
          <div class="p-5 tracking-wide text-lg text-center text-emerald-100 font-semibold group-hover:drop-shadow-[0_10px_8px_rgba(16,185,129,1)] group-hover:text-emerald-400">{a.judul}</div>
          <p class="hidden p-5 bg-black bg-opacity-50 mt-2 text-gray-500">{a.isi}</p>
        </div>
        <div class="absolute z-[1] inset-0 bg-gradient-to-b from-transparent to-black bg-opacity-[20%]">
        </div>
      </div>
    </div>
  {/each}
</div>

<script>
  export let artikel = []
</script>
