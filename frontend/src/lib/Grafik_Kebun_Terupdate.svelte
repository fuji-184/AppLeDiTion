<script>
    export let dataKebun = []
  
</script>

<div class="lg:w-1/4 overflow-y-auto bg-gradient-to-r from-teal-500 to-emerald-500 p-4 rounded-lg">
    <h2 class="text-justify text-lg font-bold mb-4">Rangkuman Kesehatan Kebun Terbaru</h2>
    
    <div class="grid grid-cols-2 gap-1">
        {#each dataKebun as d}
            <div class="group relative aspect-square flex flex-col justify-center items-center rounded-lg 
            {d.hasil === 'Healthy' ? 'bg-emerald-800' : 'bg-red-800'} cursor-pointer">
                <div class="text-xs font-semibold">{d.tanggal}</div>
                <div class="text-sm font-semibold">{d.kebun}</div>
                <div class="text-md font-bold">{d.hasil}</div>
                <!-- <div class="tooltip absolute bottom-full mb-2 left-1/2 transform -translate-x-1/2 bg-black text-white text-sm rounded px-2 py-1">
                Hello
                </div> -->
            </div>
        {/each}
    </div>
</div>

<style>
   .tooltip {
      visibility: hidden;
      opacity: 0;
      transition: opacity 0.3s;
      position: absolute;
    }
    .group:hover .tooltip {
      visibility: visible;
      opacity: 1;
    }
  </style>