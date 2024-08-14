<script>
	import "../app.css"
    import eruda from 'eruda'
    import { onMount } from "svelte"
    import { Howl, Howler } from "howler"
        
    eruda.init();
    
    
	let wellcome = new Howl({
		src: ['http://127.0.0.1:5173/wellcome.mp3'],
		html5: true
	})
	
	Howler.volume(1)
	
	onMount(() => {
		wellcome.once("load", () => {
			wellcome.play()
		})
	})
		
</script>

<slot />