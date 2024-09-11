<script>
    import { onMount } from "svelte"
    import { fetcher } from "$lib/utils/fetcher.js"
    import Grafik_Kebun_Terupdate from "$lib/Grafik_Kebun_Terupdate.svelte"
    import Grafik_Perkembangan_Kebun from "$lib/Grafik_Perkembangan_Kebun.svelte"

    let deteksi_terbaru = []

    onMount(() => {
        ambil_deteksi_terbaru()
    })

    async function ambil_deteksi_terbaru(){
        deteksi_terbaru = await fetcher({
            path: `/histori_deteksi_terbaru_by_user_id/${localStorage.getItem("id")}`,
            method: "GET"
        })
        deteksi_terbaru = deteksi_terbaru.data
        console.log(deteksi_terbaru)
    }
</script>

<div class="flex flex-col lg:flex-row gap-8 lg:min-h-full lg:justify-around lg:items-center">
    <div class="lg:w-1/4 lg:flex justify-center items-center">
        <h2 class="text-4xl">
            <div>Hello <span class="font-bold">{localStorage.getItem("nama")}</span></div>
            <div>Wellcome to <span class="font-bold">AppLeDiTion</span></div>
        </h2>
    </div>
    
    <div class="bg-gradient-to-r from-teal-500 to-emerald-500 p-4 rounded-lg">
        <h2 class="text-lg font-bold mb-4">Rangkuman Deteksi Terbaru</h2>
        <div class="flex flex-col gap-4 bg-gradient-to-br from-teal-800 via-emerald-700 to-teal-800 p-4 rounded-lg text-md">
            {#each deteksi_terbaru as d}
                <div class="text-center text-md font-bold">{d.tanggal}</div>
                <table class="text-sm">
                    <tr>
                        <td>Nama kebun</td>
                        <td>:&nbsp;&nbsp;&nbsp;</td>
                        <td>{d.kebun}</td>
                    </tr>
                    <tr>
                        <td class="py-2">Alamat kebun</td>
                        <td class="py-2">:</td>
                        <td class="py-2">{d.alamat_kebun}</td>
                    </tr>
                    <tr>
                        <td>Hasil</td>
                        <td>:</td>
                        <td class={d.hasil === "Healthy" ? "bg-green-500 px-2 py-1 rounded-lg inline-block" : "bg-red-500 px-2 py-1 rounded-lg inline-block"}>{d.hasil}</td>
                    </tr>
                </table>  
            {/each}
        </div>
    </div>
    
    <Grafik_Kebun_Terupdate dataKebun={deteksi_terbaru} />
</div>