<div class="flex h-screen justify-center items-center">
  <form class="flex flex-col gap-2 bg-black text-white p-5 rounded-md">
    <input bind:value={username} type="text" placeholder="Username" class="bg-white text-black p-2 rounded-md focus:outline-none" />
    <input bind:value={password} type="text" placeholder="Password" class="bg-white text-black p-2 rounded-md focus:outline-none" />
    <button on:click={submit} type="submit" class="mt-3 bg-green-600 p-2 rounded-md">Masuk</button>
    <p>Belum punya akun? Daftar di <a href="/daftar" class="text-green-400 font-bold">sini</a></p>
  </form>
</div>

<Notif muncul={muncul} pesan={pesan} />

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

  let username = "", password = ""
  let muncul = false, pesan = ""

  async function submit(){
    const res = await fetcher({
      path: "/masuk",
      method: "POST",
      body: {
        username: username,
        password: password
      }
    })

    console.log(res)
    if (res.token){
      localStorage.setItem("token", JSON.stringify(res.token))
      localStorage.setItem("id", JSON.stringify(res.id))
      localStorage.setItem("nama", JSON.stringify(res.nama))
    }
    
    if (res.pesan === "berhasil"){
      pesan = "Login berhasil"
      muncul = true
      window.location.href = "/"
    }

  }
</script>