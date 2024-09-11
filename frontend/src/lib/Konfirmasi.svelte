<script>
	export let kotak_konfirmasi = {}
	
	import { createEventDispatcher } from "svelte"
	
	let event_klik = createEventDispatcher()
	
	function ok(){
		kotak_konfirmasi["state"] = true
		event_klik("event_klik", {
			state_baru: kotak_konfirmasi.state
		})
		kotak_konfirmasi.tampil = false
	}
	
	function cancel(){
		kotak_konfirmasi["state"] = false
		event_klik("event_klik", {
			state_baru: kotak_konfirmasi.state
		})
		kotak_konfirmasi.tampil = false
	}
</script>

<div hidden={!kotak_konfirmasi.tampil} class="absolute top-1/2 left-1/2 translate-x-[-50%] translate-y-[-50%] p-4 bg-gradient-to-br from-teal-500 to-teal-900 text-teal-50 rounded-lg">
	<p class="text-md font-semibold mb-4 text-center">
		{kotak_konfirmasi.message}
	</p>
	<div class="text-xs font-semibold flex justify-center">
		<button on:click={ok} class="bg-teal-900 p-2 rounded-lg mr-1">Ok</button>
		<button on:click={cancel} class="bg-red-700 p-2 rounded-lg">Cancel</button>
	</div>
</div>