<script>
        import Hero from "$lib/Hero.svelte"
        import Fitur from "$lib/Fitur.svelte"
        import Guider from "$lib/Guider.svelte"
        import QnA from "$lib/QnA.svelte"
        import Footer from "$lib/Footer.svelte"
        import Testimoni from "$lib/Testimoni.svelte"
        import Chart from "$lib/Chart.svelte"

        import { fetcher } from "$lib/utils/fetcher.js"
        import { onMount } from "svelte"

        let data_penyakit_per_bulan = []

        onMount(() => {
                ambil_data_penyakit_per_bulan()
        })

        async function ambil_data_penyakit_per_bulan(){
                data_penyakit_per_bulan = await fetcher({
                        path: "/histori_deteksi_by_bulan",
                        method: "GET"
                })
                data_penyakit_per_bulan = data_penyakit_per_bulan.data
                console.log(data_penyakit_per_bulan)
        }
</script>

<Hero />
<Fitur />

<Guider />
<Testimoni />
<QnA />

{#if data_penyakit_per_bulan.length > 0}
        <Chart data={data_penyakit_per_bulan} />
{/if}

<Footer />
