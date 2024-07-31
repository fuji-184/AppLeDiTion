<script>
	let artikel = {}
	
	let gambar_base64
	
	let penampil_artikel
	
	let kotak_upload_gambar = true
	
	function proses_gambar(e){
		const gambar = e.target.files[0]
		const pembaca_gambar = new FileReader()
		pembaca_gambar.onload = (e) => {
			gambar_base64 = e.target.result
		}
		pembaca_gambar.readAsDataURL(gambar)
	}
	
	function memasukkan_gambar(e, gambar){
		let pemilihan = window.getSelection()
		let jangkauan = pemilihan.getRangeAt(0)
		
		if (penampil_artikel.contains(jangkauan.commonAncestorContainer)){
			let tag_img = document.createElement("img")
			tag_img.src = gambar
			tag_img.className = "w-[50%] m-auto rounded-lg"
			
			jangkauan.deleteContents()
			jangkauan.insertNode(tag_img)
			
			jangkauan.setStartAfter(tag_img)
			jangkauan.collapse(true)
			pemilihan.removeAllRanges()
			pemilihan.addRange(jangkauan)
			
			gambar_base64 = ""
			let form = e.target.closest("form")
			form.reset()
			kotak_upload_gambar = true
		}
		else {
			alert("Gambar hanya dapat dimasukkan di isi artikel")
		}
	}
	
	function format_teks(e, perintah){
		document.execCommand(perintah, false, null)
	}
	
	function format_aktif(perintah){
		return document.queryCommandState(perintah)
	}
	
	function edit_teks(){
		let selection = window.getSelection()
		let awal = selection.anchorOffset
		let akhir = selection.focusOffset
		let selisih = akhir - awal
		
		let range = selection.getRangeAt(0)
		
		if (selisih > 0){
			let teks = selection.toString()
			
			if (!teks.includes("<b>")){
				let b = document.createElement("b")
				// b.textContent = teks
				
				var myAnchorNodeValue = window.getSelection().anchorNode.nodeValue;
				
				// let tes = range.surroundmContents(b)
    
				console.log(range.parentNode)
				
				range.deleteContents()
				range.insertNode(b)
				range.setStartAfter(b)
			}
			else {
				// teks = teks.replace(/<\/?b>/g, '')
				
				console.log(range.cloneContents().innerHTML)
				
				range.deleteContents()
				range.insertNode(teks)
				range.setStartAfter(teks)
			}
			
			range.collapse(true)
			
			selection.removeAllRanges()
			selection.addRange(range)
			
			// console.log(range)
		}
	}
	
	document.addEventListener("select", () => {
		console.log("hello2")
	})
	
	function tes(){
    let selection = document.getSelection();
		let cloned = document.createElement("div")
		let astext = document.createElement("div")
    cloned.innerHTML = ""
    astext.innerHTML = ""

    // Clone DOM nodes from ranges (we support multiselect here)
    for (let i = 0; i < selection.rangeCount; i++) {
      cloned.append(selection.getRangeAt(i).cloneContents());
    }

    // Get as text
    astext.innerHTML += selection;
    console.log("hasil : " + astext.innerHTML)
  }
</script>

<div class="flex flex-col gap-4 p-8 h-screen">
	<input type="text" class="bg-emerald-500 text-white p-4 rounded-lg focus:border-none focus:outline-none" bind:value={artikel["judul"]} />
	<div class="relative text-white">
		<button on:click={() => kotak_upload_gambar = false} >
			<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="40px" width="40px"><path fill="white" d="M13.3 34.15h21.45q.5 0 .7-.4.2-.4-.1-.8l-5.85-7.8q-.25-.3-.6-.3t-.6.3l-6 7.75-4.05-5.55q-.25-.3-.6-.3t-.6.3l-4.3 5.6q-.25.4-.075.8t.625.4ZM9 42q-1.2 0-2.1-.9Q6 40.2 6 39V9q0-1.2.9-2.1Q7.8 6 9 6h30q1.2 0 2.1.9.9.9.9 2.1v30q0 1.2-.9 2.1-.9.9-2.1.9Zm0-3h30V9H9v30ZM9 9v30V9Z"/></svg>
			<!--{#if kotak_upload_gambar}-->
				<form class:hidden={kotak_upload_gambar} class="bg-emerald-500 p-8 rounded-lg flex justify-center items-center flex-col gap-8 absolute top-[110%] relative" bind:this={kotak_upload_gambar}>
					<input type="file" accept="images/*" on:change={proses_gambar} class="rounded-lg text-emerald-100 text-xs font-semibold bg-emerald-950 p-4" />
					{#if gambar_base64}
						<img src={gambar_base64} class="rounded-lg w-[50%]" />
						<button on:click|stopPropagation={memasukkan_gambar(event, gambar_base64)} class="bg-emerald-950 text-emerald-100 p-4 text-xs font-semibold rounded-lg" >Tambah</button>
					{/if}
					<button on:click|stopPropagation={() => kotak_upload_gambar = true} class="p-1 rounded-full m-2 absolute top-0 right-0 bg-emerald-950 hover:bg-red-500" >
						<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="16px" width="16px"><path fill="white" d="M24 26.1 13.5 36.6q-.45.45-1.05.45-.6 0-1.05-.45-.45-.45-.45-1.05 0-.6.45-1.05L21.9 24 11.4 13.5q-.45-.45-.45-1.05 0-.6.45-1.05.45-.45 1.05-.45.6 0 1.05.45L24 21.9l10.5-10.5q.45-.45 1.05-.45.6 0 1.05.45.45.45.45 1.05 0 .6-.45 1.05L26.1 24l10.5 10.5q.45.45.45 1.05 0 .6-.45 1.05-.45.45-1.05.45-.6 0-1.05-.45Z"/></svg>
					</button>
				</form>
			<!--{/if}-->
		</button>
	</div>
	<div id="penampil_artikel" class="bg-emerald-500 text-white p-4 rounded-lg focus:border-none focus:outline-none" bind:innerHTML={artikel["isi"]} contenteditable="true" bind:this={penampil_artikel} ><i><b>hello</b></i></div>
	<button class="text-white" on:click={() => edit_teks()}>edit</button>
</div>

<style>
	input:active {
		border: 0;
		outline: 0;
	}
	
	.sembunyikan {
		display: none;
	}
</style>