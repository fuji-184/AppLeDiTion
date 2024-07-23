<div class="flex h-screen justify-center items-center">
  <form class="flex flex-col gap-2 bg-black text-white p-5 rounded-md">
    <input bind:value={nama} type="text" placeholder="Nama" class="bg-white text-black p-2 rounded-md focus:outline-none" />
    <input bind:value={username} type="text" placeholder="Username" class="bg-white text-black p-2 rounded-md focus:outline-none" />
    <input bind:value={password} type="text" placeholder="Password" class="bg-white text-black p-2 rounded-md focus:outline-none" />
    <button on:click={submit} type="submit" class="mt-3 bg-green-600 p-2 rounded-md">Daftar</button>
    <p>Sudah punya akun? Masuk di <a href="/masuk" class="text-green-400 font-bold">sini</a>
  </form>
</div>

<Notif pesan={pesan} muncul={notif} />

<script>
  import { fetcher } from "$lib/utils/fetcher.js"
  import Notif from "$lib/Notif.svelte"
  import { onMount } from "svelte"
  import { goto } from "$app/navigation"

  onMount(() => {
    if (localStorage.getItem("token")){
      goto("/")
    }
  })
  
  let nama = "", username = "", password = "", is_admin = false
  let notif = false
  let pesan = ""

  async function submit(){
    const res = await fetcher({
      method: "POST",
      path: "/daftar",
      body: {
        nama: nama,
        username: username,
        password: password,
        is_admin: is_admin,
      }
    })

    console.log(res.pesan)
    if (res.token){
      localStorage.setItem("token", JSON.stringify(res.token))
      localStorage.setItem("id", JSON.stringify(res.id))
      localStorage.setItem("nama", JSON.stringify(res.nama))
    }

    if (res.pesan === "berhasil"){
      pesan = "Pendaftaran berhasil"
      notif = true
      goto("/")
    }
  }
</script>