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

<div hidden={!kotak_konfirmasi.tampil}>
	<p>
		{kotak_konfirmasi.message}
	</p>
	<div>
		<button on:click={ok}>Ok</button>
		<button on:click={cancel}>Cancel</button>
	</div>
</div>