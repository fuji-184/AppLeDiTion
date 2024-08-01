<script>
	let menu = [
			"akun",
			"artikel",
			"menu"
		]
	let kotak_menu
	
	function klik_menu(e){
		if (kotak_menu.classList.contains("hidden")){
			e.target.classList.remove("hijau1")
			e.target.classList.add("hijau2")
			kotak_menu.classList.remove("hidden")
		}
		else {
			e.target.classList.remove("hijau2")
			e.target.classList.add("hijau1")
			kotak_menu.classList.add("hidden")
		}
	}
</script>

<div bind:this={kotak_menu} class="hidden lg:flex w-[50%] bg-gradient-to-r from-emerald-500 to-emerald-950 text-white absolute right-0 bottom-0 top-0 p-8 flex flex-col gap-4 justify-center items-center lg:static lg:w-full lg:h-full">
	{#each menu as m}
		<a class="p-4 w-full text-md text-center font-semibold bg-emerald-800 rounded-lg hover:bg-emerald-700 hover:p-8 hover:text-2xl" href={m}>
			{m}
		</a>
	{/each}
</div>

<button on:click={(event) => klik_menu(event)} class="hijau1 p-4 rounded-full absolute bottom-4 right-4 lg:hidden">
	<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="40px" width="40px"><path fill="white" d="M7.5 36q-.65 0-1.075-.425Q6 35.15 6 34.5q0-.65.425-1.075Q6.85 33 7.5 33h33q.65 0 1.075.425Q42 33.85 42 34.5q0 .65-.425 1.075Q41.15 36 40.5 36Zm0-10.5q-.65 0-1.075-.425Q6 24.65 6 24q0-.65.425-1.075Q6.85 22.5 7.5 22.5h33q.65 0 1.075.425Q42 23.35 42 24q0 .65-.425 1.075-.425.425-1.075.425Zm0-10.5q-.65 0-1.075-.425Q6 14.15 6 13.5q0-.65.425-1.075Q6.85 12 7.5 12h33q.65 0 1.075.425Q42 12.85 42 13.5q0 .65-.425 1.075Q41.15 15 40.5 15Z"/></svg>
</button>

<style>
	.hijau1 {
		background-color: rgb(16, 185, 129);
	}
	.hijau2 {
		background-color: rgb(2, 44, 34);
	}
</style>