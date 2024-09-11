<script>
    export let notif = {}

    function tombol(){
        notif.muncul = !notif.muncul
    }

    $: if (notif.muncul){
            setTimeout(() => {
                notif.muncul = false
            }, 3000)
        }
</script>

{#if notif.muncul}
    <div class="p-4 absolute rounded-lg bg-gradient-to-r from-emerald-500 to-teal-500 absolute top-[16px] right-[16px] text-emerald-100 text-md font-semibold">
        <div class="flex gap-4 justify-between">
            <p class="break-all">{notif.pesan}</p>
            <button on:click={tombol} class="p-4 bg-emerald-950 rounded-lg font-semibold w-[32px] h-[32px] flex justify-center items-center text-md">X</button>
        </div>
    </div>
{/if}
