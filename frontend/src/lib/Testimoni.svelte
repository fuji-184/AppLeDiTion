<script>
  import { onMount, onDestroy } from 'svelte';

  let testimoni = [
    {
      nama: "Fuji",
      teks: "Deteksinya bagus, akurat, dan membantu petani apel"
    },
    {
      nama: "Satria",
      teks: "Sangat membantu dalam menyelesaikan masalah sehari-hari"
    },
    {
      nama: "Budi",
      teks: "Produk ini sangat direkomendasikan bagi pengguna yang mencari kemudahan"
    },
    {
      nama: "Dewi",
      teks: "Pelayanan konsumen yang baik dan cepat"
    }
  ];

  let currentIndex = 0; // Indeks testimonial saat ini
  let maxVisible = 1; // Jumlah testimonial maksimal untuk perangkat mobile

  // Fungsi untuk mengatur jumlah testimonial yang ditampilkan berdasarkan lebar layar
  const updateMaxVisible = () => {
    if (window.innerWidth >= 768) { // Lebar untuk desktop (contoh 768px)
      maxVisible = 3;
    } else {
      maxVisible = 1; // Untuk perangkat mobile
    }

    // Memastikan currentIndex tidak melebihi jumlah testimoni yang tersedia
    if (currentIndex + maxVisible > testimoni.length) {
      currentIndex = Math.max(testimoni.length - maxVisible, 0);
    }
  };

  // Fungsi untuk menampilkan testimonial berikutnya
  const nextTestimonial = () => {
    currentIndex = Math.min(currentIndex + maxVisible, testimoni.length - maxVisible);
  };

  // Fungsi untuk menampilkan testimonial sebelumnya
  const prevTestimonial = () => {
    currentIndex = Math.max(currentIndex - maxVisible, 0);
  };

  // Panggil fungsi saat komponen dimuat
  onMount(() => {
    updateMaxVisible(); // Pertama kali, update berdasarkan lebar layar saat ini
    window.addEventListener('resize', updateMaxVisible); // Update saat layar diubah ukurannya
    return () => {
      window.removeEventListener('resize', updateMaxVisible); // Hapus listener saat komponen di-unmount
    };
  });
</script>

<div class="p-8 py-24 bg-gradient-to-b from-black via-emerald-950 to-emerald-950 text-emerald-100">
  <h2 class="text-3xl md:text-5xl tracking-loose text-center drop-shadow-[0_8px_6px_rgba(34,197,94,1)] bg-clip-text text-transparent bg-gradient-to-r from-teal-400 to-emerald-400 font-bold mb-16">Testimoni</h2>

  <div class="relative flex justify-center items-center overflow-x-auto scrollbar-hide">
    <button class="absolute left-0 top-1/2 transform -translate-y-1/2 text-4xl z-10" on:click={prevTestimonial} hidden={currentIndex === 0}>
      <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="1.5em" width="1.5em"><path fill="currentColor" d="m25.45 31.45-6.4-6.4q-.25-.25-.35-.5-.1-.25-.1-.55 0-.3.1-.55.1-.25.35-.5l6.4-6.4q.7-.7 1.625-.325Q28 16.6 28 17.6v12.8q0 1-.925 1.375t-1.625-.325Z"/></svg>
    </button>
    
    <div class="w-1/2 md:w-full flex space-x-4 md:space-x-8">
      {#each testimoni.slice(currentIndex, currentIndex + maxVisible) as t}
        <div class="w-full md:w-[33%] text-center px-4">
          <img class="rounded-full w-24 m-auto" src="https://via.placeholder.com/150" alt="{t.nama}">
          <p class="mt-4 text-md font-semibold">{t.nama}</p>
          <p class="mt-2 text-sm italic text-justify">{t.teks}</p>
        </div>
      {/each}
    </div>

    <button class="absolute right-0 top-1/2 transform -translate-y-1/2 text-4xl z-10" on:click={nextTestimonial} hidden={currentIndex >= testimoni.length - maxVisible}>
      <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="1.5em" width="1.5em"><path fill="currentColor" d="M22.55 31.45q-.7.7-1.625.325Q20 31.4 20 30.4V17.6q0-1 .925-1.375t1.625.325l6.4 6.4q.25.25.35.5.1.25.1.55 0 .3-.1.55-.1.25-.35.5Z"/></svg>
    </button>
  </div>
</div>

<style>
  /* CSS untuk scrollbar horizontal yang bisa di-hide */
  .scrollbar-hide::-webkit-scrollbar {
    display: none;
  }
</style>
