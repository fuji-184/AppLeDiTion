<script>
import { fetcher } from "$lib/utils/fetcher.js"

	let pengaturan = [
		{
			data: "id",
			tipe: "angka",
			isi_bawaan: 12
		},
		{
			data: "nama",
			tipe: "teks",
			isi_bawaan: "fuji"
		},
		{
			data: "gambar",
			tipe: "gambar"
		}
	]
	
	let isi_bawaan = true
	
	let isi_formulir = {}
	
	if (isi_bawaan){
		for (let i=0; i<pengaturan.length; i++){
			isi_formulir[
					pengaturan[
							i
						][
								"data"
							]
				] = pengaturan[
									i
								][
										"isi_bawaan"
									]
		}
	}
	
	function proses_gambar(e, data){
		const gambar = e.target.files[0]
		const pembaca_gambar = new FileReader
		pembaca_gambar.onload = (e) => {
			isi_formulir[data] = e.target.result
		}
		pembaca_gambar.readAsDataURL(gambar)
	}
	
	isi_formulir["gambar"] = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlHeavMGuSDnzymxaNqqTBHUP4sS7hnop2m6ZaodkfQ_u17keaBp7cqn8&s=10"
</script>

<form class="p-8 rounded-lg bg-gradient-to-br from-emerald-500 via-emerald-800 to-emerald-950  text-md">
	{#each pengaturan as p}
		<label class="text-emerald-100 font-semibold">
			{p.data}
		</label>
		{#if p.tipe === "teks"}
			<input type="text" placeholder={p.data} bind:value={isi_formulir[p.data]} />
		{:else if p.tipe === "angka"}
			<input type="number" placeholder={p.data} bind:value={isi_formulir[p.data]} />
		{:else if p.tipe === "gambar"}
			<input type="file" accept="images/*" on:change={(e) => proses_gambar(e, p.data)} placeholder={p.data} />
			{#if isi_formulir[p.data]}
				<img src={isi_formulir[p.data]} alt={p.data} width="50%" class="rounded-lg m-auto" />
			{/if}	
		{/if}
	{/each}
	<button class="bg-emerald-950 text-emerald-100 p-4 mt-16 rounded-lg font-semibold m-auto w-[80px] block">Submit</button>
</form>

<style>
	input {
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