<script>
    import { onMount } from 'svelte';
    import { Chart, registerables } from 'chart.js';
  
    // Daftarkan semua elemen yang diperlukan untuk Chart.js
    Chart.register(...registerables);
  
    // Data yang digunakan
    const chartData = [
      {
        "alamat_kebun": "depok",
        "hasil": "Apple Scab",
        "kebun": "kebun 10",
        "tanggal": "Wed, 10 Jul 2024 00:00:00 GMT"
      },
      {
        "alamat_kebun": "aaaaa",
        "hasil": "Healthy",
        "kebun": "a",
        "tanggal": "Sun, 01 Sep 2024 00:00:00 GMT"
      },
      {
        "alamat_kebun": "a",
        "hasil": "Healthy",
        "kebun": "kebun",
        "tanggal": "Sun, 01 Sep 2024 00:00:00 GMT"
      },
      {
        "alamat_kebun": "a",
        "hasil": "Healthy",
        "kebun": "kebun",
        "tanggal": "Mon, 02 Sep 2024 00:00:00 GMT"
      }
    ];
  
    let chart;
  
    onMount(() => {
      const ctx = document.getElementById('myChart').getContext('2d');
  
      // Format data untuk Chart.js
      const labels = Array.from(new Set(chartData.map(item => item.tanggal)));
      const results = Array.from(new Set(chartData.map(item => item.hasil)));
      
      const datasets = results.map(hasil => ({
        label: hasil,
        data: labels.map(tanggal => {
          const item = chartData.find(d => d.tanggal === tanggal && d.hasil === hasil);
          return item ? item.kebun : '';
        }),
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1
      }));
  
      chart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: datasets
        },
        options: {
          responsive: true,
          plugins: {
            legend: {
              position: 'top',
            },
            tooltip: {
              callbacks: {
                label: function(tooltipItem) {
                  return tooltipItem.raw || '';
                }
              }
            }
          },
          scales: {
            x: {
              type: 'category',
              title: {
                display: true,
                text: 'Tanggal'
              }
            },
            y: {
              title: {
                display: true,
                text: 'Hasil Deteksi'
              },
              ticks: {
                callback: function(value) {
                  // Mengatur label sumbu Y
                  return value;
                }
              }
            }
          }
        }
      });
    });
  </script>
  
  <canvas id="myChart" width="400" height="200"></canvas>
  