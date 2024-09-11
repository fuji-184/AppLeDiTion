<script>
	import NavDashboard from "$lib/NavDashboard.svelte"
	import Breadcrumb from "$lib/Breadcrumb.svelte"
</script>

<div class="block lg:flex min-h-screen">
	<div class="lg:w-[20%]">
		<NavDashboard/>
	</div>
	<div class="lg:w-[80%] bg-gradient-to-br from-teal-700 to-teal-900 p-8">
		<Breadcrumb />
		<slot />
	</div>
</div>