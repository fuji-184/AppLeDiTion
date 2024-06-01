<script>
  let nama, password
  
  async function daftar(){
    await fetch(`${import.meta.env.VITE_BACKEND_URL}/daftar`, {
      method: "post",
      headers: {
        "content-type": "application/json"
      },
      body: JSON.stringify(nama)
    })
  }
</script>

<div class="flex h-screen justify-center items-center">
  <form class="flex flex-col gap-2 bg-black text-white p-5 rounded-md">
    <input type="text" placeholder="Nama" bind:value={nama} class="bg-white text-black p-2 rounded-md focus:outline-none" />
    <input type="text" placeholder="Password" bind:value={password} class="bg-white text-black p-2 rounded-md focus:outline-none" />
    <button type="submit" on:click={daftar} class="mt-3 bg-green-600 p-2 rounded-md">Daftar</button>
    <p>Sudah punya akun? Masuk di <a href="/masuk" class="text-green-400 font-bold">sini</a>
  </form>
</div>