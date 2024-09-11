<script>
    import { goto } from "$app/navigation"
    import { page } from "$app/stores"

    let menu = [
        {
            teks: "Dashboard",
            href: "/dashboard"
        },
        {
            teks: "Kebun",
            href: "/dashboard/kebun"
        },
        {
            teks: "Histori",
            href: "/dashboard/histori"
        }
    ]

    let path_aktif = "new"

    $: {
        path_aktif = $page.url.pathname
    }

    function klik_path(path){
        goto(path)
    }
</script>

<div class="fixed text-white flex flex-col justify-center items-center h-full text-md font-semibold">
    {#each menu as m}
        <a href={m.href} class:gradien={path_aktif === m.href} class="w-full p-4 rounded-l-full">
            {m.teks}
        </a>
    {/each}
</div>

<style>
    .gradien {
        background-image: linear-gradient(to right, #065f46, #2dd4bf, #2dd4bf)
    }
</style>