<script>
	import { fetcher } from "$lib/utils/fetcher.js"
	import Notif from "$lib/Notif.svelte"
	import { createEventDispatcher } from "svelte"

	export let formulir = {}
	export let setting_fetcher = {}

	// export let formulir = {
	// 	nama: "",
	// 	username: "",
	// 	password: "",
	// 	is_admin: false,
	// 	tanggal_lahir: null
	// }

	// export let setting_fetcher = {
	// 	path: "/histori_deteksi",
	// 	method: "POST",
	// 	body: true
	// }

	let kotak_form

	let notif = {
		muncul: false,
		pesan: setting_fetcher["method"] && setting_fetcher["method"].toUpperCase() === "POST" ? "Data berhasil disimpan" : "Data berhasil diupdate"
	}
	
	function proses_gambar(e, key){
		const gambar = e.target.files[0]
		const pembaca_gambar = new FileReader
		pembaca_gambar.onload = (e) => {
			formulir[key] = e.target.result
		}
		pembaca_gambar.readAsDataURL(gambar)
	}
	
	// isi_formulir["gambar"] = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlHeavMGuSDnzymxaNqqTBHUP4sS7hnop2m6ZaodkfQ_u17keaBp7cqn8&s=10"

	async function submit(){

		if (setting_fetcher["body"] === true){
			setting_fetcher.body = formulir
		}
		let hasil = await fetcher(setting_fetcher)
		if (hasil.berhasil){
			notif.muncul = true
			if (setting_fetcher["method"].toUpperCase() === "POST"){
				window.history.back()
			}
		}
	}
</script>

<form bind:this={kotak_form} class="p-8 rounded-lg bg-gradient-to-br from-teal-500 via-teal-800 to-teal-950  text-md">
	{#each Object.entries(formulir) as [key, isi]}
		{#if key !== "id" && isi["tipe"] !== "hidden"}
			<label class="text-emerald-100 font-semibold">
				{key}
			</label>
		{/if}
		{#if typeof(isi) === "file" || key === "gambar"}
			<input type="file" accept="images/*" on:change={(e) => proses_gambar(e, key)} placeholder={key} />
			{#if isi}
				<img src={formulir[key]} alt={key} width="50%" class="rounded-lg m-auto" />
			{/if}
		{:else if key === "tanggal_lahir"}
			<input type="date" bind:value={formulir[key]} />
		{:else if typeof(isi) === "string"}
			<input type="text" placeholder={key} bind:value={formulir[key]} />
		{:else if typeof(isi) === "number" && key !== "id"}
			<input type="number" placeholder={key} bind:value={formulir[key]} />
		{:else if typeof(isi) === "boolean"}
			<select bind:value={formulir[key]}>
				<option value={true}>Iya</option>
				<option value={false}>Tidak</option>
			</select>
		{/if}
	{/each}
	<button on:click={submit} class="bg-teal-950 text-teal-50 p-4 mt-16 rounded-lg font-semibold m-auto w-[80px] block">Submit</button>
</form>

<Notif {notif} />

<style>
	input, select {
		padding: 16px;
		border-radius: 8px;
		border: none;
		outline: none;
		width: 100%;
		background-color: rgb(209, 250, 229);
		color: rgb(2, 44, 34);
		margin: 4px 0 32px 0;
	}
</style>