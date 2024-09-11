<script>
	import "../app.css"
    import eruda from 'eruda'
    import { onMount } from "svelte"
    import { Howl, Howler } from "howler"
	import { fetcher } from "$lib/utils/fetcher.js"
        
    // eruda.init();
    
    
	let wellcome = new Howl({
		src: ['http://127.0.0.1:5173/wellcome.mp3'],
		html5: true
	})
	
	Howler.volume(1)
	
	onMount(() => {
		wellcome.once("load", () => {
			wellcome.play()
		})
		kirim_visitor()
	})

	async function kirim_visitor(){
		await fetcher({
			path: "/visitors",
			method: "POST",
		
		})
	}
		
</script>

<slot />