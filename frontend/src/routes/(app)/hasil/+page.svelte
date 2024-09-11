<script>
   import { hasil } from "$lib/stores/hasil.js"
  import { onMount } from "svelte";
  import { goto } from "$app/navigation"
  import { fetcher } from "$lib/utils/fetcher.js"

   // let hasil_prediksi = {
   //    hasil_prediksi: "healthys",
   //    score: 100,
   //    deskripsi: "<p><strong>Cedar Apple Rust (CAR)</strong>, juga dikenal sebagai <em>Gymnosporangium juniperi-virginianae</em>, adalah penyakit jamur yang mempengaruhi pohon apel (<em>Malus spp.</em>) dan juniper (<em>Juniperus spp.</em>), terutama <em>Juniperus virginiana</em> (cedar merah timur). Penyakit ini adalah salah satu penyakit karat yang paling merusak pada pohon apel.</p> <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4ATw7XcYXRIwEh5z4BhE60Nn6F-87wKj0dg&s' /> <h2>Infeksi Awal</h2> <p>Setelah spora teliospora terbawa angin dan mendarat di daun atau buah pohon apel, mereka mulai berkecambah dan menginfeksi jaringan tanaman, biasanya pada awal musim semi ketika daun muda baru muncul. Infeksi ini sering dimulai sebagai bercak kecil berwarna kuning atau oranye pada daun apel.</p> <h2>Perkembangan Karat</h2> <p>Bercak ini kemudian membesar dan berubah menjadi oranye cerah, sering kali dengan bintik hitam di tengahnya. Saat infeksi berkembang, karat menyebabkan daun melengkung atau cacat dan mungkin menyebabkan defoliasi dini, mengurangi produktivitas pohon secara signifikan.</p> <h2>Pembentukan Aecia</h2> <p>Setelah beberapa minggu, struktur seperti tabung kecil yang disebut aecia mulai berkembang di bagian bawah daun yang terinfeksi. Aecia menghasilkan aeciospora yang dapat terbawa angin kembali ke pohon juniper, menyelesaikan siklus hidup jamur.</p> <h2>Dampak dan Gejala</h2> <ul> <li><strong>Bercak Karat:</strong> Bercak oranye atau kuning yang menonjol pada daun adalah gejala yang paling jelas. Bercak ini sering dikelilingi oleh lingkaran berwarna merah atau hitam dan dapat menyebabkan daun jatuh prematur.</li> <li><strong>Buah Terdampak:</strong> Buah yang terinfeksi mungkin mengalami deformasi, mengembangkan bercak karat, dan mengalami penurunan kualitas serta ukuran, sehingga tidak dapat dijual atau dikonsumsi.</li> <li><strong>Defoliasi:</strong> Dalam kasus infeksi yang parah, pohon apel dapat mengalami defoliasi dini, yang berdampak pada kesehatan umum pohon dan mengurangi hasil panen.</li> </ul>"
   //    ,pengobatan: "<p><h2>Pemangkasan</h2><ul><li>Pangkas dan buang bagian tanaman yang terinfeksi untuk mengurangi jumlah sumber infeksi. Hapus daun dan cabang yang menunjukkan gejala penyakit.</li><li>Kumpulkan dan buang material tanaman yang terinfeksi dari area kebun untuk mencegah penyebaran lebih lanjut</li></ul></p><p><h2>Fungisida</h2><ul><li>Semprotkan fungisida pada tanaman. Beberapa fungisida yang dapat digunakan adalah Chlorothalonil, Myclobutanil, dan Difenoconazole. Chlorothalonil adalah fungisida kontak yang bekerja dengan membentuk lapisan pelindung pada permukaan tanaman, mencegah infeksi baru. Myclobutanil adalah fungisida sistemik yang dapat menembus jaringan tanaman dan memberikan perlindungan yang lebih lama. Difenoconazole juga merupakan fungisida sistemik yang bekerja dengan menghambat pertumbuhan jamur</li></ul></p>"
   // }
   

   let hasil_prediksi = []
   

   hasil.subscribe(data => {
      hasil_prediksi = data
      hasil_prediksi.hasil.score = hasil_prediksi.hasil.score.toFixed(2)
      console.log(hasil_prediksi)
      simpan_histori(data)
   })

   async function simpan_histori(data_histori){
      await fetcher({
         path: "/histori_deteksi",
         method: "POST",
         body: {
            id_user: localStorage.getItem("id"),
            id_kebun: data_histori.id_kebun,
            id_hasil: data_histori.hasil.id_hasil,
            skor: data_histori.hasil.score
         }
      })
   }
</script>
 
{#if hasil_prediksi.hasil}
   <div class="bg-black h-full text-white flex-col m-auto p-8">
      <div class="flex justify-around items-center gap-4 p-8 rounded-lg {hasil_prediksi.hasil_prediksi === "healthy" ? "bg-emerald-500" : "bg-red-500"}">
         <div class="flex flex-col gap-4">
               <span class="text-3xl font-bold">
                  {hasil_prediksi.hasil.hasil_prediksi}
               </span>
               <span class=" text-lg font-semibold">
                  <span>Keyakinan</span>
                  <span class="block text-emerald-950">
                     {hasil_prediksi.hasil.score}%
                  </span>
               </span>
         </div>
         <div class="">
               <img class="rounded-xl" src="http://127.0.0.1:5000/static/heatmap.jpg" alt="An image" />
         </div>
      </div>
      <div class="kontainer w-full mt-16">
         {#if hasil_prediksi.hasil.deskripsi !== null}
         {@html hasil_prediksi.hasil.deskripsi}
         {/if}
      </div>
      <div class="bg-emerald-500 p-8 mt-16 rounded-lg">
         <h2 class="text-2xl font-bold text-center">Rekomendasi Pengobatan</h2>
         <p class="kontainer mt-4">
            {@html hasil_prediksi.hasil.pengobatan}
         </p>
      </div>
   </div>
{/if}

<style>
   div :global(p) {
      padding-bottom: 16px;
   }
   div :global(.kontainer) {
      font-size: 14px;
      line-height: 20px;
      text-align: justify;
      font-weight: 400;
      -webkit-font-smoothing: auto;
-moz-osx-font-smoothing: auto;
   }
   div :global(.kontainer h2){
      font-size: 18px;
      line-height: 48px;
      font-weight: 700;
   }
   div :global(strong){
      font-weight: 600;
   }
   div :global(ul){
      padding-left: 16px;
   }
   div :global(li){
      padding-bottom: 12px;
   }
   div :global(.kontainer img){
      margin: auto;
      border-radius: 8px;
   }
   @media screen and (max-width: 767px) {
      div :global(.kontainer img){
         width: 100%;
         padding: 48px 0;
      }
   }
   @media screen and (min-width: 768px) {
      div :global(.kontainer img){
         width: 48%;
         padding: 48px 0;
      }
   }
   @media screen and (min-width: 1280px) {
      div :global(.kontainer img){
         width: 32%;
         padding: 48px 0;
      }
   }
</style>