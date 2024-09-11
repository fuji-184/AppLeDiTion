<script>
    import Grafik  from "$lib/Grafik.svelte"
    import { fetcher } from "$lib/utils/fetcher.js"
    import { onMount } from "svelte"

    onMount(() => {
        grafik_visitor()
    })

    let setting_grafik = {
        judul: "Jumlah Pengunjung",
        label: "Pengunjung"
    }

    async function grafik_visitor(){
        setting_grafik["data"] = await fetcher({
            path: "/visitors",
            method: "GET"
        })
        setting_grafik["data"] = setting_grafik["data"]["hasil"]
        console.log(setting_grafik)
    }
</script>

{#if setting_grafik["data"]}
    <Grafik {setting_grafik}/>
{/if}