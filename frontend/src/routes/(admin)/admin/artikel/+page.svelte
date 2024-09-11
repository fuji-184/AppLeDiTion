<script>
	import Tabel from "$lib/Tabel.svelte"
	import { fetcher } from "$lib/utils/fetcher.js"
  import { onMount } from "svelte";
	
	$: data = []

	let setting = {
		key_view: {
			"url_awal": "/blog",
			"key": "judul"
		},
		url_delete: "/artikel"
	}

	onMount(async () => {
		data = await fetcher({
			path: "/artikel",
			method: "GET",
			// token: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImZ1amkifQ.LfagiBOZDdvalAlvt5h_Vn9YcYbVgI_jycOLSVsoX-8`
		})
		data = data.data
	})
	
</script>

{#if data.length > 0}
	<Tabel {data} {setting} />
{/if}