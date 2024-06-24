<script>
  import Accordion from '$lib/Accordion.svelte';
</script>

<section class="p-4 py-28 bg-gradient-to-b from-green-950 via-black to-black text-green-100">
  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
    <div class="mb-16">
      <h6 class="text-lg font-medium text-center mb-2">
        FAQs
      </h6>
      <h2
        class="text-4xl font-manrope text-center font-bold leading-[3.25rem]"
      >
        Frequently asked questions
      </h2>
    </div>

    <div class="flex flex-col gap-8">
    <Accordion question="How do I update my billing information?">
      To contact customer support, look for a 'Contact us' or 'Help' button or link on the website or platform. You may be able to email, call, or chat with customer support for assistance.
    </Accordion>

    <Accordion question="How can I contact customer support?">
      To contact customer support, look for a 'Contact us' or 'Help' button or link on the website or platform. You may be able to email, call, or chat with customer support for assistance.
    </Accordion>

    <Accordion question="How do I update my profile information?">
      To contact customer support, look for a 'Contact us' or 'Help' button or link on the website or platform. You may be able to email, call, or chat with customer support for assistance.
    </Accordion>

    <Accordion question="How do I find my purchase history?">
      To contact customer support, look for a 'Contact us' or 'Help' button or link on the website or platform. You may be able to email, call, or chat with customer support for assistance.
    </Accordion>
    </div>
  </div>
</section>