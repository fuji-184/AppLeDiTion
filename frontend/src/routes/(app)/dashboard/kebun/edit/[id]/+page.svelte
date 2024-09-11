<script>
    export let data

    import { onMount } from "svelte"
    import { fetcher } from "$lib/utils/fetcher.js"
    import Formulir from "$lib/Formulir.svelte"

    let kebun = []
    let setting_fetcher = {
        path: "/kebun",
        method: "PUT",
        body: true
    }

    onMount(() => {
        ambil_kebun_by_id()
    })

    async function ambil_kebun_by_id(){
        kebun = await fetcher({
            path: `/kebun/${data.id}`,
            method: "GET"
        })
        kebun = kebun.data
    }
</script>

{#if kebun.length > 0}
    <Formulir formulir={kebun[0]} setting_fetcher={setting_fetcher} />
{/if}