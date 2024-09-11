<script>
    import io from 'socket.io-client';
    import { onMount } from 'svelte';
    let socket;
  
    let video;
    let canvas;
    let context;
    let streaming = false;
  
    onMount(() => {
      // Initialize WebSocket connection
      socket = io('http://localhost:5000');
      
      socket.on('connect', () => {
        console.log('WebSocket connected');
      });
  
      socket.on('result', (data) => {
        console.log('Received result:', data);
      });
  
      // Set up camera stream
      video = document.querySelector('video');
      canvas = document.querySelector('canvas');
      
      if (!canvas) {
        console.error('Canvas element not found');
        return;
      }
      
      context = canvas.getContext('2d');
      
      if (!context) {
        console.error('Failed to get canvas context');
        return;
      }
  
      navigator.mediaDevices.getUserMedia({ video: true })
        .then((stream) => {
          video.srcObject = stream;
          video.play();
          streaming = true;
          captureFrame();
        })
        .catch(err => console.error('Error accessing camera:', err));
    });
  
    function captureFrame() {
      if (streaming) {
        context.drawImage(video, 0, 0, canvas.width, canvas.height);
        canvas.toBlob(blob => {
          if (blob) {
            console.log('Sending image blob: ', blob);
            socket.emit('image', blob);
          }
        }, 'image/jpeg');
        requestAnimationFrame(captureFrame);
      }
    }
  </script>
  
  <style>
    video, canvas {
      width: 100%;
      height: auto;
    }
  </style>
  
  <video autoplay playsinline></video>
  <canvas width="640" height="480"></canvas>
  