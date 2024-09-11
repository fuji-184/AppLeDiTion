<script>
	import Formulir from "$lib/Formulir.svelte"

	let formulir = {
		nama: "",
		username: "",
		password: "",
		is_admin: false,
		tanggal_lahir: null
	}

	let setting_fetcher = {
		path: "/histori_deteksi",
		method: "POST",
		body: true
	}
</script>

<Formulir {formulir} {setting_fetcher} />