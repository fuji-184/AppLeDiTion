<script>
    import Formulir from "$lib/Formulir.svelte"

    let formulir = {
        nama: "",
        alamat: "",
        id_user: {
            tipe: "hidden",
            isi: localStorage.getItem("id")
        }
    }
    let setting_fetcher = {
        path: "/kebun",
        method: "POST",
        body: true
    }
</script>

<Formulir {formulir} {setting_fetcher} />