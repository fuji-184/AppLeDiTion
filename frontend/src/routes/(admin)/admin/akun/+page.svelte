<script>
	import Tabel from "$lib/Tabel.svelte"
	import { fetcher } from "$lib/utils/fetcher.js"
  import { onMount } from "svelte";
	
	$: data = []

	console.log(localStorage.getItem("token"))

	onMount(async () => {
		data = await fetcher({
			path: "/histori_deteksi",
			method: "GET",
			// token: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImZ1amkifQ.LfagiBOZDdvalAlvt5h_Vn9YcYbVgI_jycOLSVsoX-8`
		})
		data = data.data
	})
	
</script>

{#if data.length > 0}
	<Tabel {data} />
{/if}