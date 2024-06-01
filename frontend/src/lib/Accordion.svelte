<script>
  import { onMount } from 'svelte';
  import { createEventDispatcher } from 'svelte';

  let isOpen = false;
  const dispatch = createEventDispatcher();
  
  export let question

  onMount(() => {
    const accordion = document.querySelector('.accordion');
    accordion.addEventListener('click', () => {
      isOpen = !isOpen;
      dispatch('toggle', { isOpen });
    });
  });
</script>

<div
  class="accordion py-8 px-6 border-b border-solid border-gray-200 transition-all duration-500 rounded-2xl hover:bg-green-50 accordion-active:bg-green-50"
>
  <button
    class="accordion-toggle group inline-flex items-center justify-between leading-8 text-gray-900 w-full transition duration-500 text-left hover:text-green-600 accordion-active:text-green-600"
    aria-expanded="{isOpen}"
  >
    <h5>{question}</h5>
    <svg
      class="text-gray-500 transition duration-500 group-hover:text-green-600 accordion-active:text-green-600 accordion-active:rotate-180"
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
    class="accordion-content w-full px-0 overflow-hidden"
    style="max-height: {isOpen ? '250px' : '0'}"
  >
    <p class="text-base text-gray-900 leading-6">
      <slot></slot>
    </p>
  </div>
</div>
