<script>
    export let data

    import Grafik_Kebun from "$lib/Grafik_Kebun.svelte"
    import { onMount } from "svelte"
    import { fetcher } from "$lib/utils/fetcher.js"

    let rangkuman_deteksi = []

    onMount(() => {
        ambil_kebun()
    })

    async function ambil_kebun(){
        rangkuman_deteksi = await fetcher({
            path: `/histori_deteksi_by_id_user_dan_kebun/${localStorage.getItem("id")}/${data.id_kebun}`,
            method: "GET"
        })
        rangkuman_deteksi = rangkuman_deteksi.data
        console.log("rangkuman deteksi: ", rangkuman_deteksi)
    }
</script>

{#if rangkuman_deteksi.length > 0}
    <Grafik_Kebun data={rangkuman_deteksi} />
{:else}
    <div>Belum Ada Data Hasil Deteksi</div>
{/if}