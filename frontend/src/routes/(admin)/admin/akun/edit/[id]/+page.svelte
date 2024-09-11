<script>
	export let data

	import Formulir from "$lib/Formulir.svelte"
	import { fetcher } from "$lib/utils/fetcher.js"
  	import { onMount } from "svelte"

	let formulir = {}

	let setting_fetcher = {
		path: "/histori_deteksi",
		method: "PUT",
		body: true
	}

	onMount(async () => {
		formulir = await fetcher({
			path: `/histori_deteksi/${data.id}`,
			method: "GET"
		})
		formulir = formulir.data[0]
		console.log(formulir)
	})

</script>

<!-- {#if formulir.length > 0} -->
	<Formulir {formulir} {setting_fetcher} />
<!-- {/if} -->