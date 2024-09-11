<script>
	export let menu = [
			"akun",
			"artikel"
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

<div bind:this={kotak_menu} class="z-10 hidden lg:flex w-[50%] bg-teal-950 text-white fixed right-0 bottom-0 top-0 p-8 flex flex-col gap-4 justify-center items-center lg:static lg:w-full lg:h-full overflow-y-auto">
	<span class="absolute top-24 text-3xl flex justify-center items-center flex-col hover:animate-blink drop-shadow-[0_10px_8px_rgba(16,185,129,1)]">
		<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="1.5em" width="1.5em"><path fill="currentColor" d="M20 23.75q-3.3 0-5.4-2.1-2.1-2.1-2.1-5.4 0-3.3 2.1-5.4 2.1-2.1 5.4-2.1 3.3 0 5.4 2.1 2.1 2.1 2.1 5.4 0 3.3-2.1 5.4-2.1 2.1-5.4 2.1ZM5.5 39.8q-.65 0-1.075-.425Q4 38.95 4 38.3v-3.2q0-1.75.875-3.15T7.4 29.8q3.6-1.6 6.675-2.3 3.075-.7 5.925-.7h1.15q-.3.7-.45 1.375-.15.675-.25 1.625H20q-2.9 0-5.675.625T8.6 32.5q-.8.4-1.2 1.125Q7 34.35 7 35.1v1.7h13.45q.25.9.6 1.625t.85 1.375ZM20 20.75q1.95 0 3.225-1.275Q24.5 18.2 24.5 16.25q0-1.95-1.275-3.225Q21.95 11.75 20 11.75q-1.95 0-3.225 1.275Q15.5 14.3 15.5 16.25q0 1.95 1.275 3.225Q18.05 20.75 20 20.75Zm0-4.5Zm.45 20.55Zm14.25-.85q1.65 0 2.825-1.175Q38.7 33.6 38.7 31.95q0-1.65-1.175-2.825Q36.35 27.95 34.7 27.95q-1.65 0-2.825 1.175Q30.7 30.3 30.7 31.95q0 1.65 1.175 2.825Q33.05 35.95 34.7 35.95Zm-1.85 2.75q-.85-.25-1.725-.725-.875-.475-1.475-1.075l-2.2.5q-.25.1-.5 0t-.35-.35l-.65-1.15q-.15-.2-.1-.45.05-.25.25-.45l1.9-1.8q-.1-.45-.1-1.25t.1-1.25l-1.9-1.8q-.2-.2-.25-.45-.05-.25.1-.45l.65-1.15q.1-.25.35-.35.25-.1.5 0l2.2.5q.6-.6 1.475-1.075.875-.475 1.725-.725l.4-2.65q.05-.3.25-.475t.5-.175h1.4q.3 0 .5.175t.25.475l.4 2.65q.85.25 1.725.725.875.475 1.475 1.075l2.2-.5q.25-.1.5 0t.35.35l.65 1.15q.15.2.1.45-.05.25-.25.45l-1.9 1.8q.1.45.1 1.25t-.1 1.25l1.9 1.8q.2.2.25.45.05.25-.1.45l-.65 1.15q-.1.25-.35.35-.25.1-.5 0l-2.2-.5q-.6.6-1.475 1.075-.875.475-1.725.725l-.4 2.65q-.05.3-.25.475t-.5.175H34q-.3 0-.5-.175t-.25-.475Z"/></svg>
		Fuji
	</span>
	<a class="p-4 w-full text-md text-center font-semibold bg-teal-600 rounded-lg hover:bg-teal-500 hover:p-8 hover:text-2xl" href={"/admin"}>
		Dashboard
	</a>
	{#each menu as m}
		<a class="p-4 w-full text-md text-center font-semibold bg-teal-600 rounded-lg hover:bg-teal-500 hover:p-8 hover:text-2xl" href={"/admin/" + m}>
			{m}
		</a>
	{/each}
</div>

<button on:click={(event) => klik_menu(event)} class="z-20 hijau1 p-4 rounded-full fixed bottom-4 right-4 lg:hidden">
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