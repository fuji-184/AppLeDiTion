<script>
    export let data

    import { onMount } from "svelte"
    import { fetcher } from "$lib/utils/fetcher.js"

    let artikel = {}

    console.log(data.judul)

    onMount(async () => {
        artikel = await fetcher({
            path: `/artikel/by/${data.judul}`,
            method: "GET"
        })
        artikel = artikel.data[0]
    })
</script>

<div class="p-16 lg:w-3/4 lg:m-auto bg-gradient-to-b from-black via-black to-emerald-950 min-h-screen">
    <h1 class="text-5xl text-center font-bold mt-4 mb-16">
        {artikel.judul}
    </h1>
    <div class="text-base text-balance mt-8 text-justify text text-md kontainer-artikel">
        {@html artikel.isi}
    </div>
</div>

<style>
    :global(.kontainer-artikel img) {
        border-radius: 16px;
        margin: 0 auto;
        width: 50%;
    }
    :global(.kontainer-artikel p) {
        margin-top: 40px;
    }
</style>