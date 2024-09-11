<script>
    import { fetcher } from "$lib/utils/fetcher.js"
    import { onMount } from "svelte"

    let histori = []

    onMount(() => {
        ambil_histori_deteksi()
    })

    async function ambil_histori_deteksi(){
        histori = await fetcher({
            path: `/histori_deteksi_by_user_id/${localStorage.getItem("id")}`,
            method: "GET"
        })
        console.log(histori)
        histori = histori.data
    }
</script>

<div class="flex flex-col gap-8 justify-center lg:items-center w-full min-h-screen p-8 lg:m-auto">
    {#if histori.length > 0}
        {#each histori as h}
            <div class="{h.hasil === 'Healthy' ? 'bg-emerald-800' : 'bg-red-800'} rounded-lg flex flex-col gap-1 relative p-4 lg:w-3/4">
                <h2 class="text-xl font-bold">{h.hasil}</h2>
                <span class="text-md font-semibold">{h.kebun}, 
                    <span class="text-sm">{h.alamat_kebun}</span>
                </span>
                <span class="text-lg font-semibold absolute top-4 right-4">{h.skor}%</span>
                <span class="text-xs absolute bottom-4 right-4">{h.tanggal}</span>
            </div>
        {/each}
    {:else}
        <div class="flex justify-center items-center h-full">Belum ada histori deteksi</div>
    {/if}
</div>