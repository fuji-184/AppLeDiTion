<script>
  export let setting = {
    warna_background: 'bg-green-600',
    warna_teks: 'text-white',
    teks: 'tombol',
    klik: null
  }
</script>

<button on:click={setting.klik} class={`${setting.warna_background} ${setting.warna_teks} block w-[100px] m-auto bg-green-600 text-white rounded-md`} >{setting.teks}</button>