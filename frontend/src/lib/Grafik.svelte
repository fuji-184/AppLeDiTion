<script>
    export let setting_grafik = {};
  
    import { onMount } from 'svelte';
    import Chart from 'chart.js/auto';
    
    let labels = setting_grafik.data.map(d => d.tanggal);
    let dataPoints = setting_grafik.data.map(d => d.pengunjung);
  
    onMount(() => {
      const ctx = document.getElementById('visitorChart').getContext('2d');
      new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [{
            label: setting_grafik.label,
            data: dataPoints,
            borderColor: 'white', // Warna garis putih
            backgroundColor: 'white', // Warna background grafik putih transparan
            fill: true
          }]
        },
        options: {
          plugins: {
            legend: {
              labels: {
                color: 'white' // Warna teks legenda putih
              }
            },
            tooltip: {
              callbacks: {
                label: (context) => {
                  return `${context.dataset.label}: ${context.raw}`;
                }
              },
              titleColor: 'white', // Warna teks judul tooltip putih
              bodyColor: 'white'   // Warna teks konten tooltip putih
            }
          },
          scales: {
            x: {
              beginAtZero: true,
              ticks: {
                color: 'white' // Warna teks sumbu X putih
              },
              grid: {
                color: 'white' // Warna grid sumbu X putih transparan
              }
            },
            y: {
              beginAtZero: true,
              ticks: {
                color: 'white' // Warna teks sumbu Y putih
              },
              grid: {
                color: 'white' // Warna grid sumbu Y putih transparan
              }
            }
          }
        }
      });
    });
  </script>
  
  <h1 class="text-md font-semibold text-white">{setting_grafik.judul}</h1>
  <canvas id="visitorChart" width="400" height="200"></canvas>
  