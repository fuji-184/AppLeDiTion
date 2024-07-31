<script>
	import Editor from '@tinymce/tinymce-svelte'

	let artikel = {
		judul: "",
		isi: ""
	}

	let conf = {
	  height: 800,
	  menubar: true,
	  plugins: [
		'advlist', 'autolink', 'lists', 'link', 'image', 'charmap',
		'anchor', 'searchreplace', 'visualblocks', 'code', 'fullscreen',
		'insertdatetime', 'media', 'table', 'preview', 'help', 'wordcount'
	  ],
	  toolbar: 'undo redo | blocks | ' +
		'bold italic forecolor | alignleft aligncenter ' +
		'alignright alignjustify | bullist numlist outdent indent | ' +
		'removeformat | help',
	}
</script>

<div>
	<input type="text" bind:value={artikel.judul} placeholder="judul" class="p-4 rounded-lg w-full focus:outline-none text-xl font-bold" />
	<Editor scriptSrc='http://127.0.0.1:5173/tinymce/tinymce.min.js' bind:value={artikel.isi}
  	{conf}
	/>
</div>