<script>
	import NavDashboard from "$lib/NavDashboard.svelte"
</script>

<div class="block lg:flex">
	<div class="lg:w-[20%]">
		<NavDashboard/>
	</div>
	<div class="lg:w-[80%]">
		<slot />
	</div>
</div>