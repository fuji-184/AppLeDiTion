<script>
  import axios from 'axios';
  import { createEventDispatcher } from 'svelte'
  
  import Tombol from '$lib/Tombol.svelte'
  
  const dispath = createEventDispatcher()

  let files;
  let base64_img
  // let base64_img = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlHeavMGuSDnzymxaNqqTBHUP4sS7hnop2m6ZaodkfQ_u17keaBp7cqn8&s=10';
  
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

<div class="bg-green-100 border border-green-500 m-5 p-5 rounded-md">
  <input type="file" bind:files on:change={toBase64} class="block w-[50%] m-auto mb-5 rounded-md" />
  
  {#if base64_img}
    <img src={base64_img} class="block w-[50%] m-auto mb-5 rounded-md" />
  {/if}

  <Tombol setting={{ klik: kirimGambar, teks: 'Kirim' }} />

</div>