<script>
  export let setting = {
    warna_background: 'bg-emerald-600',
    warna_teks: 'text-white',
    teks: 'tombol',
    klik: null
  }
</script>

<button on:click={setting.klik} class={`${setting.warna_background} ${setting.warna_teks} block w-[100px] m-auto bg-gradient-to-r from-teal-500 to-emerald-500 text-white rounded-md shadow-lg shadow-emerald-500`} >{setting.teks}</button>