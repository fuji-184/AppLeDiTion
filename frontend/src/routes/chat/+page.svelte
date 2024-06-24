<!-- Chat.svelte -->
<script>
    import { onMount } from 'svelte';
    import io from 'socket.io-client';

    let messages = ["hello"];
    let socket;

    onMount(() => {
        socket = io('http://localhost:5000'); // Sesuaikan dengan alamat server Flask

        socket.on('message', msg => {
            console.log(messages)
            messages = [...messages, msg];
        });

        return () => {
            socket.disconnect();
        };
    });

    function sendMessage(event) {
        if (event.key === 'Enter') {
            socket.emit('message', event.target.value);
            event.target.value = '';
        }
    }
</script>

<div class="text-white">
    <ul>
        {#each messages as message}
            <li>{message}</li>
        {/each}
    </ul>
    <input type="text" placeholder="Type your message..." on:keydown={sendMessage} class="text-black" />
</div>
