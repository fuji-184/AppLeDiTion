<script>
    import { page } from '$app/stores';
    import { derived } from 'svelte/store';

    // Membuat store yang memproses path menjadi segmen breadcrumb
    const breadcrumbSegments = derived(page, ($page) => {
        const path = $page.url.pathname;
        return path.split('/').filter(Boolean);
    });

    function formatSegment(segment) {
        return segment.replace(/-/g, ' ').replace(/\b\w/g, char => char.toUpperCase());
    }
</script>

<nav aria-label="breadcrumb">
    <ol class="breadcrumb text-sm text-teal-50">
        {#each $breadcrumbSegments as segment, index}
            <li class="breadcrumb-item">
                <a href={'/' + $breadcrumbSegments.slice(0, index + 1).join('/')}>
                    {formatSegment(segment)}
                </a>
            </li>
        {/each}
    </ol>
</nav>

<style>
    /* Styling sederhana untuk breadcrumb */
    .breadcrumb {
        list-style: none;
        padding: 0;
        display: flex;
    }

    .breadcrumb-item {
        margin-right: 0.5rem;
    }

    .breadcrumb-item::after {
        content: '/';
        margin-left: 0.5rem;
    }

    .breadcrumb-item:last-child::after {
        content: '';
    }
</style>
