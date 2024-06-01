<script>
  import Upload_File from "$lib/Upload_File.svelte"
  
  let hasil_prediksi = {
    'hasil_prediksi': 'Healthy'
  }
  
  function kirimHasilPrediksi(e){
    hasil_prediksi = e.detail
    console.log(hasil_prediksi)
  }
</script>

<div class="flex justify-center h-screen items-center">
  <Upload_File on:message={kirimHasilPrediksi} />
</div>

<!--{#if hasil_prediksi}-->
  <!--<div class="bg-green-600 text-white p-5  m-5 rounded-md">{hasil_prediksi.hasil_prediksi}</div>-->
<!--  <img src={hasil_prediksi} />-->
<!--{/if}-->