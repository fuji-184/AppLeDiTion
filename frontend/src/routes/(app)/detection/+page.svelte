<script>
  import Upload_File from "$lib/Upload_File.svelte"
  import { Howl } from "howler"
  import { onDestroy } from "svelte"
  
  let hasil_prediksi = {
    'hasil_prediksi': 'Healthy'
  }
  
  function kirimHasilPrediksi(e){
    hasil_prediksi = e.detail
    console.log(hasil_prediksi)
  }
  
  let pilih_gambar = new Howl({
		src: ['http://127.0.0.1:5173/pilih_gambar.mp3'],
		html5: true
	})
	
	pilih_gambar.play()
	
	onDestroy(() => {
		pilih_gambar.stop()
	})
</script>


<Upload_File on:message={kirimHasilPrediksi} />


<!--{#if hasil_prediksi}-->
  <!--<div class="bg-green-600 text-white p-5  m-5 rounded-md">{hasil_prediksi.hasil_prediksi}</div>-->
<!--  <img src={hasil_prediksi} />-->
<!--{/if}-->