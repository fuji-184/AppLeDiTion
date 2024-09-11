<script>
	export let data = []
	export let setting = {}

	import Konfirmasi from "$lib/Konfirmasi.svelte"
	import Notif from "$lib/Notif.svelte"
	import { fetcher } from "$lib/utils/fetcher.js"

	// export let data = [
	// 	{
	// 		id: 1,
	// 		nama: "fuji"
	// 	},
	// 	{
	// 		id: 2,
	// 		nama: "a"
	// 	}
	// ]

	// export let setting = {
	// 	key_view: {
	// 		"url_awal": "/blog",
	// 		"key": "judul"
	// 	},
	// 	url_delete: "/artikel"
	// }
	
	let total_data = data.length
	
	let kolom = total_data > 0 ? Object.keys(data[0]) : []
	
	let data_tampil = []
	
	$: i_awal, input_pencarian, data, tes(data)
	
	function tes(tes){
		if (input_pencarian.length > 0){
			data_tampil = hasil_pencarian
		  total_data = data_tampil.length
		}
		else {
			data_tampil = halaman()
			total_data = data.length
		}
	}
	
	let kotak_centang = false
	
	let centang_semua = false
	
	let data_terpilih = []
	
	let kotak_pencarian = false
	
	let input_pencarian = ""
	
	let kotak_pengurutan = false
	
	let kolom_pengurutan = null
	
	let arah = null
	
	let i_awal = 0
	
	let i_akhir = 5
	
	// $: kolom_pengurutan, arah, pengurutan(kolom_pengurutan, arah)
	
	$: data.length > 0 && (kolom_pengurutan, arah, pengurutan(kolom_pengurutan, arah));


	$: hasil_pencarian = data.filter(item => {
		return Object.values(item).some(isi => {
			return String(isi).toLowerCase().includes(input_pencarian.toLowerCase())
		})
	})
	
	function pilihItem(e, item){
		if (e.target.checked){
			data_terpilih = [...data_terpilih, item]
		}
		else {
			data_terpilih = data_terpilih.filter(
				item_di_data =>
				item_di_data.id !== item.id
			)
		}
	}
	
	function pilihSemuaItem(e){
		if (e.target.checked){
			data_terpilih = data
			centang_semua = true
		}
		else {
			data_terpilih = []
			centang_semua = false
		}
	}
	
	function pengurutan(kolom, arah){
		console.log(kolom + " " + arah)
		if (kolom, arah){
			data = data.sort((a, b) => {
				const isiA = a[kolom]
				const isiB = b[kolom]
				
				if (isiA !== isiB){
					return arah === "asc" ? (
							isiA < isiB ? -1 : 1
						) : (
								isiA < isiB ? 1 : -1
							)
				}
				else {
					return 0
				}
				
			})
			console.log(data)
		}
	}
	
	function halaman(arah=null, jumlah_tampil=5){
		if (arah !== null){
			if (arah == "maju"){
				i_awal += jumlah_tampil
				i_akhir += jumlah_tampil
			}
			else {
				i_awal -= jumlah_tampil
				i_akhir -= jumlah_tampil
			}
			return data.slice(i_awal, i_akhir)
		}
		else {
			return data.slice(i_awal, i_akhir)
		}
	}
	
	let kotak_konfirmasi = {
		tampil: false,
		message: "",
		state: null
	}

	let notif = {}
	
	async function konfirmasi(event){
		if (event.detail.state_baru){
			let hasil = await fetcher({
				path: `${setting["url_delete"]}/${kotak_konfirmasi["id_data"]}`,
				method: "DELETE"
			})
			if (hasil.berhasil){
				notif = {
					pesan: "Data berhasil dihapus",
					muncul: true
				}
				data = data.filter(isi => isi.id !== kotak_konfirmasi.id_data)
				kotak_konfirmasi.id_data = null
			}
		}
	}

	function hapus(id){
		kotak_konfirmasi = {
			message: "Apakah Anda yakin ingin menghapus data ini?",
			tampil: true,
			id_data: id
		}
	}
</script>


<div class="w-full min-h-full flex flex-col items-center bg-gradient-to-b from-teal-500 via-teal-800 to-teal-950 text-white p-8 rounded-3xl">
	<div class="flex gap-4 mb-8">
		<a href={window.location.pathname + "/tambah"}>
			<button class="inline-block bg-teal-950 rounded-lg p-2">
				<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="1.5em" width="1.5em"><path fill="currentColor" d="M24 38q-.65 0-1.075-.425-.425-.425-.425-1.075v-11h-11q-.65 0-1.075-.425Q10 24.65 10 24q0-.65.425-1.075.425-.425 1.075-.425h11v-11q0-.65.425-1.075Q23.35 10 24 10q.65 0 1.075.425.425.425.425 1.075v11h11q.65 0 1.075.425Q38 23.35 38 24q0 .65-.425 1.075-.425.425-1.075.425h-11v11q0 .65-.425 1.075Q24.65 38 24 38Z"/></svg>
			</button>
		</a>
		<button on:click={() => kotak_pencarian = !kotak_pencarian} class="inline-block bg-teal-950 rounded-lg p-2">
			<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="1.5em" width="1.5em"><path fill="currentColor" d="M38.7 40.85 26.65 28.8q-1.5 1.3-3.5 2.025-2 .725-4.25.725-5.4 0-9.15-3.75T6 18.75q0-5.3 3.75-9.05 3.75-3.75 9.1-3.75 5.3 0 9.025 3.75 3.725 3.75 3.725 9.05 0 2.15-.7 4.15-.7 2-2.1 3.75L40.95 38.7q.45.4.45 1.025 0 .625-.5 1.125-.45.45-1.1.45-.65 0-1.1-.45Zm-19.85-12.3q4.05 0 6.9-2.875Q28.6 22.8 28.6 18.75t-2.85-6.925Q22.9 8.95 18.85 8.95q-4.1 0-6.975 2.875T9 18.75q0 4.05 2.875 6.925t6.975 2.875Z"/></svg>
		</button>
			<div class="relative">
			<button on:click={() => kotak_pengurutan = !kotak_pengurutan} class="inline-block bg-teal-950 rounded-lg p-2">
				<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="1.5em" width="1.5em"><path fill="currentColor" d="M21.5 36q-.65 0-1.075-.425Q20 35.15 20 34.5q0-.65.425-1.075Q20.85 33 21.5 33h5q.65 0 1.075.425Q28 33.85 28 34.5q0 .65-.425 1.075Q27.15 36 26.5 36Zm-14-21q-.65 0-1.075-.425Q6 14.15 6 13.5q0-.65.425-1.075Q6.85 12 7.5 12h33q.65 0 1.075.425Q42 12.85 42 13.5q0 .65-.425 1.075Q41.15 15 40.5 15Zm6 10.5q-.65 0-1.075-.425Q12 24.65 12 24q0-.65.425-1.075.425-.425 1.075-.425h21q.65 0 1.075.425Q36 23.35 36 24q0 .65-.425 1.075-.425.425-1.075.425Z"/></svg>
			</button>
			{#if kotak_pengurutan}
				<span class="bg-gradient-to-b from-teal-500 to-teal-900 flex flex-col gap-4 p-4 rounded-lg text-xs absolute top-[110%]">
					<span class="font-semibold">pilih kolom</span>
					<select bind:value={kolom_pengurutan} class="bg-teal-950 p-1 rounded-lg">
						{#each kolom as k}
							<option value={k}>
								{k}
							</option>
						{/each}
					</select>
					{#if kolom_pengurutan !== null}
						<span class="mt-4 font-semibold">pilih arah</span>
						<select bind:value={arah} class="bg-emerald-950 p-1 rounded-lg">
							<option value="asc">asc</option>
							<option value="desc">desc</option>
						</select>
					{/if}
				</span>
			{/if}
		</div>
		<button on:click={() => kotak_centang = !kotak_centang} class="inline-block bg-teal-950 rounded-lg p-2">
			<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="1.5em" width="1.5em"><path fill="currentColor" d="M18.9 35.1q-.3 0-.55-.1-.25-.1-.5-.35L8.8 25.6q-.45-.45-.45-1.1 0-.65.45-1.1.45-.45 1.05-.45.6 0 1.05.45l8 8 18.15-18.15q.45-.45 1.075-.45t1.075.45q.45.45.45 1.075T39.2 15.4L19.95 34.65q-.25.25-.5.35-.25.1-.55.1Z"/></svg>
		</button>
	</div>
	{#if kotak_pencarian}
		<input type="text" bind:value={input_pencarian} placeholder="pencarian..." class="p-2 mb-8 rounded-lg text-white bg-teal-950 border-none outline-none w-full" />
	{/if}
	<div class="w-full overflow-x-auto">
		{#if data.length > 0}
			<table class="w-full">
				<thead>
					<tr class="text-lg font-semibold">
						{#if kotak_centang}
							<td>
								<input type="checkbox" on:change={(e) => pilihSemuaItem(e)} checked={centang_semua} />
							</td>
						{/if}
						<th>no</th>
						{#each kolom as k}
							{#if k !== "id" && k !== "thumbnail"}
								<th>
									{k}
								</th>
							{/if}
						{/each}
						<th>menu</th>
					</tr>
				</thead>
				<tbody>
					{#each data_tampil as d,i}
						<tr class="text-md">
							{#if kotak_centang}
								<td>
									<input type="checkbox" on:change={(e) => pilihItem(e, d)} checked={centang_semua} />
								</td>
							{/if}
							<td class="text-center">{i_awal+i+1}</td>
							{#each kolom as k}
								{#if k !== "id" && k !== "thumbnail"}
									<td>
										{d[k]}
									</td>
								{/if}
							{/each}
							<td class="flex justify-center gap-2">
								{#if setting["key_view"]}
									<a href={setting.key_view.url_awal + "/" + d[setting.key_view.key]}>View</a>
								{/if}
								<a href="{window.location.pathname + "/edit/" + d.id}" class="inline-block bg-emerald-500 rounded-lg p-1">
									<svg class="inline-block" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="20px" width="20px"><path fill="currentColor" d="M9 39h2.2l22.15-22.15-2.2-2.2L9 36.8Zm30.7-24.3-6.4-6.4 2.1-2.1q.85-.85 2.125-.825 1.275.025 2.125.875L41.8 8.4q.85.85.85 2.1t-.85 2.1ZM7.5 42q-.65 0-1.075-.425Q6 41.15 6 40.5v-4.3q0-.3.1-.55.1-.25.35-.5L31.2 10.4l6.4 6.4-24.75 24.75q-.25.25-.5.35-.25.1-.55.1Zm24.75-26.25-1.1-1.1 2.2 2.2Z"/></svg>
								</a>
								<button on:click={hapus(d.id)} class="inline-block bg-emerald-500 rounded-lg p-1">
									<svg class="inline-block" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="20px" width="20px"><path fill="currentColor" d="M13.05 42q-1.2 0-2.1-.9-.9-.9-.9-2.1V10.5H9.5q-.65 0-1.075-.425Q8 9.65 8 9q0-.65.425-1.075Q8.85 7.5 9.5 7.5h7.9q0-.65.425-1.075Q18.25 6 18.9 6h10.2q.65 0 1.075.425.425.425.425 1.075h7.9q.65 0 1.075.425Q40 8.35 40 9q0 .65-.425 1.075-.425.425-1.075.425h-.55V39q0 1.2-.9 2.1-.9.9-2.1.9Zm0-31.5V39h21.9V10.5Zm5.3 22.7q0 .65.425 1.075.425.425 1.075.425.65 0 1.075-.425.425-.425.425-1.075V16.25q0-.65-.425-1.075-.425-.425-1.075-.425-.65 0-1.075.425-.425.425-.425 1.075Zm8.3 0q0 .65.425 1.075.425.425 1.075.425.65 0 1.075-.425.425-.425.425-1.075V16.25q0-.65-.425-1.075-.425-.425-1.075-.425-.65 0-1.075.425-.425.425-.425 1.075Zm-13.6-22.7V39 10.5Z"/></svg>
								</button>
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
		{:else}
			<div class="text-center text-sm">Maaf, belum ada data yang ditambahkan</div>
		{/if}
	</div>
	<div class="w-full grid grid-flow-col auto-cols-max place-content-between place-items-center mt-8">
		<button on:click={() => halaman("mundur")} class:invisible={i_awal === 0} class="inline-block bg-emerald-500 rounded-lg" >
			<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" width="40px" height="40px"><path fill="currentColor" d="m25.45 31.45-6.4-6.4q-.25-.25-.35-.5-.1-.25-.1-.55 0-.3.1-.55.1-.25.35-.5l6.4-6.4q.7-.7 1.625-.325Q28 16.6 28 17.6v12.8q0 1-.925 1.375t-1.625-.325Z"/></svg>
		</button>
		<div class="text-xs p-4">total data = {total_data}</div>
		<button on:click={() => halaman("maju")} class:invisible={i_akhir >= total_data} class="inline-block bg-emerald-500 rounded-lg">
			<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" width="40px" height="40px"><path fill="currentColor" d="M22.55 31.45q-.7.7-1.625.325Q20 31.4 20 30.4V17.6q0-1 .925-1.375t1.625.325l6.4 6.4q.25.25.35.5.1.25.1.55 0 .3-.1.55-.1.25-.35.5Z"/></svg>
		</button>
	</div>
</div>


<Konfirmasi {kotak_konfirmasi} on:event_klik={konfirmasi} />
<Notif {notif} />

<style>
	th, td {
		padding: 16px;
	}
	th, td {
		border-bottom: 2px solid white;
		border-right: 2px solid white;
	}
	th:last-child {
		border-radius: 0 10px 0 0;
	}
	tr:last-child td:first-child {
		border-radius: 0 0 0 10px;
	}
	tr:last-child td:last-child {
		border-radius: 0 0 10px 0;
	}
	table {
		border-collapse: separate;
		border-spacing: 0;
		border-top: 2px solid white;
		border-left: 2px solid white;
		border-radius: 10px 10px 0 10px;
	}
	svg {
		stroke: white;
		stroke-width: 4px;
	}
</style>