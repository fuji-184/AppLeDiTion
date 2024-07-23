<script>
    export let pesan = ""

    export let muncul = false

    function tombol(){
        muncul = !muncul
    }
</script>

{#if muncul}
    <div class="p-4 w-[20%] rounded-lg bg-gradient-to-r from-emerald-500 to-teal-500 absolute top-[16px] right-[16px] text-emerald-100 text-md font-semibold">
        <div class="flex gap-4 justify-between">
            <p class="break-all">{pesan}</p>
            <button on:click={tombol} class="p-4 bg-emerald-950 rounded-lg font-semibold w-[32px] h-[32px] flex justify-center items-center text-md">X</button>
        </div>
    </div>
{/if}
