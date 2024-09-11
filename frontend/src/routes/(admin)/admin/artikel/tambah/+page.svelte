<script>
	import Editor from '@tinymce/tinymce-svelte'
	import { fetcher } from "$lib/utils/fetcher.js"
	import Notif from "$lib//notif.svelte"
	import { goto } from "$app/navigation"

	let artikel = {
		judul: "",
		isi: ""
	}
	
	const useDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
	const isSmallScreen = window.matchMedia('(max-width: 1023.5px)').matches;

	let conf = {
	  height: 800,
	  menubar: true,
	  editimage_cors_hosts: ['picsum.photos'],
	  autosave_ask_before_unload: true,
	  autosave_interval: '30s',
	  autosave_prefix: '{path}{query}-{id}-',
	  autosave_restore_when_empty: false,
	  autosave_retention: '2m',
	  image_advtab: true,
	  importcss_append: true,
	  image_caption: true,
	  quickbars_selection_toolbar: 'bold italic | quicklink h2 h3 blockquote quickimage quicktable',
	  noneditable_class: 'mceNonEditable',
	  toolbar_mode: 'sliding',
	  contextmenu: 'link image table',
	  skin: useDarkMode ? 'oxide-dark' : 'oxide',
	  //skin: 'borderless',
	  //icons: 'thin',
	  content_css: useDarkMode ? 'dark' : 'default',
	  content_style: '* {background: linear-gradient(to right, #14b8a6, #10b981)}',
	  plugins: [
		'advlist', 'autolink', 'lists', 'link', 'image', 'charmap',
		'anchor', 'searchreplace', 'visualblocks', 'code', 'fullscreen',
		'insertdatetime', 'media', 'table', 'preview', 'help', 'wordcount', 'importcss', 'autosave', 'save', 'directionality', 'visualchars', 'codesample', 'pagebreak', 'nonbreaking', 'quickbars', 'emoticons', 'accordion'
	  ],
	  toolbar: 'undo redo | accordion accordionremove | blocks fontfamily fontsize | ' +
		'bold italic underline strikethrough forecolor backcolor | alignleft aligncenter ' +
		'alignright alignjustify | bullist numlist outdent indent lineheight | link image | table media | charmap emoticons | code fullscreen preview | save print | pagebreak anchor codesample | ltr rtl | ' +
		'removeformat | help',
		// license_key: 'gpl'
	}

	let notif = {}

	async function save(){
		const res = await fetcher({
			path: "/artikel",
			method: "POST",
			body: artikel
		})
		if (res.berhasil){
			notif = {
				pesan: "Artikel berhasil disimpan",
				muncul: true
			}
			setTimeout(() => {
				goto("/admin/artikel")
			}, 400)
		}
	}
</script>

<div class="h-screen bg-[#222f3e] overflow-y-auto rounded-t-lg">
	<div class="flex justify-center items-center">
	<input type="text" bind:value={artikel.judul} placeholder="judul" class="p-4 rounded-lg w-full focus:outline-none text-xl font-bold bg-[#222f3e] text-white" />
		<button on:click={save} class="block p-2 m-2 text-md font-bold rounded-lg bg-gradient-to-r from-emerald-500 to-teal-500">Save</button>
	</div>
	<Editor licenseKey='gpl' scriptSrc='http://127.0.0.1:5173/tinymce/tinymce.min.js'
	
		bind:value={artikel.isi}
		{conf}
		
	/>
</div>

<Notif {notif} />