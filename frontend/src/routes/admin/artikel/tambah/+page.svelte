<script>
	import Editor from '@tinymce/tinymce-svelte'

	let artikel

	let conf = {
	  height: 500,
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

		content_style: '* {background-color: black; color: white; border-radius: 16px}'
	}
</script>

<div>
  <Editor id="tes" scriptSrc='http://127.0.0.1:5173/tinymce/tinymce.min.js' bind:value={artikel}
  	{conf}
	/>
</div>

<style>
	#tes {
		background-color: black;
	}
</style>