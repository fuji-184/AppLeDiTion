<script>
  import Accordion from '$lib/Accordion.svelte';

  let qna = [
    {
        q: "Apa itu website deteksi penyakit daun apel?",
        a: "Website ini adalah platform yang menggunakan teknologi pembelajaran mesin untuk mendeteksi dan mengidentifikasi penyakit pada daun apel dari gambar yang diunggah pengguna."
    },
    {
        q: "Bagaimana cara menggunakan website ini untuk mendeteksi penyakit daun apel?",
        a: "Anda dapat menggunakan website ini dengan mengunggah foto daun apel yang ingin Anda periksa. Sistem akan menganalisis gambar tersebut dan memberikan hasil deteksi mengenai jenis penyakit yang mungkin menyerang daun tersebut."
    },
    // {
    //     q: "Penyakit apa saja yang bisa dideteksi oleh website ini?",
    //     a: "Website ini dapat mendeteksi berbagai penyakit umum pada daun apel seperti Apple Scab, Black Root Rot, Cedar Apple Rust, dan lainnya."
    // },
    {
        q: "Bagaimana tingkat akurasi dari deteksi penyakit ini?",
        a: "Tingkat akurasi deteksi bergantung pada kualitas gambar yang diunggah serta kompleksitas penyakit. Sistem telah dilatih menggunakan ribuan gambar, namun akurasi mungkin bervariasi."
    },
    {
        q: "Apakah saya harus membayar untuk menggunakan layanan ini?",
        a: "Tidak, layanan ini sepenuhnya gratis."
    },
    // {
    //     q: "Apa yang harus dilakukan jika deteksi penyakit tidak akurat atau tidak dapat mengenali penyakit?",
    //     a: "Jika hasil deteksi tidak akurat atau sistem tidak dapat mengenali penyakit, Anda disarankan untuk mengunggah gambar dengan resolusi yang lebih tinggi, memastikan gambar fokus pada daun yang terinfeksi, atau mencari saran dari ahli pertanian."
    // },
    {
        q: "Apakah saya bisa menggunakan website ini di perangkat mobile?",
        a: "Ya, website ini dirancang agar responsif dan dapat diakses dari berbagai perangkat, termasuk ponsel dan tablet."
    },
    // {
    //     q: "Bagaimana cara menjaga agar tanaman apel tetap sehat setelah terdeteksi penyakit?",
    //     a: "Setelah penyakit terdeteksi, website akan memberikan rekomendasi langkah-langkah pengobatan dan pencegahan yang dapat diambil untuk menjaga kesehatan tanaman apel Anda."
    // },
    // {
    //     q: "Apakah data gambar saya akan disimpan atau digunakan?",
    //     a: "Gambar yang diunggah dapat digunakan untuk meningkatkan sistem deteksi kami, tetapi kami memastikan bahwa semua data pribadi Anda tetap aman dan tidak akan dibagikan tanpa izin."
    // },
    // {
    //     q: "Apakah website ini hanya untuk mendeteksi penyakit pada daun apel?",
    //     a: "Saat ini, fokus utama website adalah pada deteksi penyakit daun apel, tetapi kami berencana untuk memperluas layanan ke tanaman lain di masa mendatang."
    // }
];

</script>

<section class="p-4 py-28 bg-gradient-to-b from-emerald-950 via-black to-black text-emerald-100 md:px-[16%]">
  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
    <div class="mb-16 drop-shadow-[0_8px_6px_rgba(34,197,94,1)] bg-clip-text text-transparent bg-gradient-to-r from-teal-400 to-emerald-400">
      <h6 class="text-lg font-medium text-center mb-2">
        FAQs
      </h6>
      <h2
        class="text-4xl font-manrope text-center font-bold leading-[3.25rem]"
      >
        Frequently asked questions
      </h2>
    </div>

    <div class="flex flex-col gap-8">
      {#each qna as q}
        <Accordion question={q.q}>
          {q.a}
        </Accordion>
      {/each}
    </div>
  </div>
</section>