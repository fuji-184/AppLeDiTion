<script>
  import { createEventDispatcher } from 'svelte';

  let isOpen = false;
  const dispatch = createEventDispatcher();

  export let question;

  function toggleAccordion() {
    isOpen = !isOpen;
    dispatch('toggle', { isOpen });
  }
</script>

<div
  class="text-md bg-gradient-to-br from-emerald-500 via-emerald-800 to-black accordion py-8 px-6 transition-all duration-500 rounded-2xl hover:bg-emerald-500 shadow-lg shadow-emerald-500"
>
  <button
    class="accordion-toggle group inline-flex items-center justify-between leading-8 w-full transition duration-500 text-left hover:text-emerald-100 accordion-active:text-emerald-100"
    aria-expanded={isOpen}
    on:click={toggleAccordion}
  >
    <h5 class="font-semibold">{question}</h5>
    <svg
      class="transition duration-500 group-hover:text-emerald-100 accordion-active:text-emerald-100 accordion-active:rotate-180"
      width="22"
      height="22"
      viewBox="0 0 22 22"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      style="transform: rotate({isOpen ? '180deg' : '0'})"
    >
      <path
        d="M16.5 8.25L12.4142 12.3358C11.7475 13.0025 11.4142 13.3358 11 13.3358C10.5858 13.3358 10.2525 13.0025 9.58579 12.3358L5.5 8.25"
        stroke="currentColor"
        stroke-width="1.6"
        stroke-linecap="round"
        stroke-linejoin="round"
      ></path>
    </svg>
  </button>
  <div
    class="accordion-content w-full px-0 overflow-hidden transition-max-height"
    style="max-height: {isOpen ? '250px' : '0'}"
  >
    <p class="text-sm leading-6">
      <slot></slot>
    </p>
  </div>
</div>

<style>
  .accordion-active {
    background-color: #d1f7d8; /* Ubah warna sesuai keinginan */
  }
</style>
