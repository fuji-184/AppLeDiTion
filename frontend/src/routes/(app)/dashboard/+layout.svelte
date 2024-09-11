<script>
    import Nav_Dashboard_User from "$lib/Nav_Dashboard_User.svelte"
    
</script>

<div class="flex min-h-screen">
    <div class="w-[10%] flex justify-end">
        <Nav_Dashboard_User />
    </div>
    <div class="w-[90%] bg-gradient-to-r from-teal-400 via-teal-700 to-teal-950 p-12 min-h-screen">
        <slot />
    </div>
</div>