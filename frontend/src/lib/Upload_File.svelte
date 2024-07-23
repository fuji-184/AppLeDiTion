<script>
  import axios from 'axios';
  import { createEventDispatcher } from 'svelte'
  
  import Tombol from '$lib/Tombol.svelte'
  
  const dispath = createEventDispatcher()

  let files;
  // let base64_img
  let base64_img = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlHeavMGuSDnzymxaNqqTBHUP4sS7hnop2m6ZaodkfQ_u17keaBp7cqn8&s=10';
  
  function toBase64() {
    if (files && files.length > 0) {
      let reader = new FileReader();
      reader.onload = function() {
        base64_img = reader.result;
      };
      reader.readAsDataURL(files[0]);
    }
  }

  async function kirimGambar() {
    if (files && files.length > 0) {
      try {
        let gambar = new FormData();
        gambar.append('gambar', files[0]);

        const response = await axios.post(`${import.meta.env.VITE_BACKEND_URL}/klasifikasi`, gambar, {
          headers: {
            'Content-Type': 'multipart/form-data'
          },
          // withCredentials: true
        });

        response.data;
        dispath('message', response.data)
      } catch (err) {
        console.error(err);
      }
    }
  }
</script>

<div class="bg-gradient-to-b from-black via-emerald-950 to-black p-8 pt-24 md:px-[16%] h-screen flex justify-center items-center">
<div class="md:w-1/2 m-auto bg-gradient-to-b from-teal-500 via-emerald-950 to-black text-emerald-100 border border-emerald-500 p-8 rounded-3xl shadow-lg shadow-emerald-500">
  
  <svg class="block mx-auto" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" height="1.5em" width="1.5em"><path fill="currentColor" d="M13.3 34.15h21.45q.5 0 .7-.4.2-.4-.1-.8l-5.85-7.8q-.25-.3-.6-.3t-.6.3l-6 7.75-4.05-5.55q-.25-.3-.6-.3t-.6.3l-4.3 5.6q-.25.4-.075.8t.625.4ZM9 42q-1.2 0-2.1-.9Q6 40.2 6 39V9q0-1.2.9-2.1Q7.8 6 9 6h30q1.2 0 2.1.9.9.9.9 2.1v30q0 1.2-.9 2.1-.9.9-2.1.9Zm0-3h30V9H9v30ZM9 9v30V9Z"/></svg>
  
  <input type="file" bind:files on:change={toBase64} class="block w-[50%] m-auto mb-5 rounded-md bg-gradient-to-r from-teal-500 to-emerald-500 shadow-lg shadow-emerald-500 text-emerald-100" />
  
  {#if base64_img}
    <img src={base64_img} class="block w-[50%] m-auto mb-5 rounded-md shadow-lg shadow-emerald-500" />
  {/if}

  <Tombol setting={{ klik: kirimGambar, teks: 'Kirim' }} />

</div>
</div>