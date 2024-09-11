<script>
    import { onMount } from "svelte"
    import { fetcher } from "$lib/utils/fetcher.js"

    import Tabel from "$lib/Tabel.svelte"

    let kebun = []
    let tabel_setting = {
        key_view: {
			"url_awal": "/dashboard/kebun",
			"key": "id"
		},
        url_delete: "/kebun"
    }

    onMount(() => {
        ambil_kebun()
    })

    async function ambil_kebun(){
        kebun = await fetcher({
            path: `/kebun_by_user_id/${localStorage.getItem("id")}`,
            method: "GET"
        })
        kebun = kebun.data
        console.log("kebun: ", kebun)
    }
</script>

{#if kebun.length > 0}
    <Tabel data={kebun} setting={tabel_setting} />
{:else}
    <Tabel data={[]} setting={{}} />
{/if}