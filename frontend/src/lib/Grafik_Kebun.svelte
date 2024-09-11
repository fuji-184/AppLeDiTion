<script>
    export let data = [];

    import { onMount } from 'svelte';
    import Chart from 'chart.js/auto';

    let displayMode = 'bulan'; // Default mode 'bulan' (bulan atau tahun)
    let chartInstance;

    // Fungsi untuk memformat bulan dalam format "YYYY-MM"
    function formatMonth(date) {
        const [year, month] = date.split('-');
        return `${year}-${month}`;
    }

    // Mengelompokkan data berdasarkan id_kebun (menggantikan nama penyakit)
    function groupData(mode) {
        let groupedData = {};
        let labels = new Set();

        data.forEach(item => {
            // Ambil key berdasarkan mode (bulan atau tahun)
            let key = mode === 'bulan' ? formatMonth(item.tgl) : item.tgl.slice(0, 4);
            
            // Menggunakan id_kebun sebagai identifier (pengganti nama penyakit)
            if (!groupedData[item.id_kebun]) {
                groupedData[item.id_kebun] = {};
            }
            if (!groupedData[item.id_kebun][key]) {
                groupedData[item.id_kebun][key] = 0;
            }
            groupedData[item.id_kebun][key] += item.jumlah;
            labels.add(key);
        });

        // Mengembalikan data dalam format yang bisa digunakan oleh chart.js
        return {
            labels: [...labels].sort(),  // Sort label untuk urutan yang rapi
            datasets: Object.keys(groupedData).map(id_kebun => {
                return {
                    label: `Kebun ${id_kebun}`,  // Label dengan id kebun
                    data: [...labels].sort().map(label => groupedData[id_kebun][label] || 0),
                    borderColor: getRandomColor(),
                    backgroundColor: 'rgba(0, 0, 0, 0)',
                    fill: true
                };
            })
        };
    }

    // Fungsi untuk menghasilkan warna acak
    function getRandomColor() {
        const letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }

    // Fungsi untuk memperbarui chart
    function updateChart() {
        const ctx = document.getElementById('visitorChart').getContext('2d');
        const chartData = groupData(displayMode);

        if (chartInstance) {
            chartInstance.destroy(); // Hapus grafik lama
        }

        chartInstance = new Chart(ctx, {
            type: 'line',
            data: {
                labels: chartData.labels,
                datasets: chartData.datasets
            },
            options: {
                plugins: {
                    legend: {
                        labels: {
                            color: 'white'
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: (context) => {
                                return `${context.dataset.label}: ${context.raw}`;
                            }
                        },
                        titleColor: 'white',
                        bodyColor: 'white'
                    }
                },
                scales: {
                    x: {
                        beginAtZero: true,
                        ticks: {
                            color: 'white'
                        },
                        grid: {
                            color: 'rgba(255, 255, 255, 0.2)'
                        }
                    },
                    y: {
                        beginAtZero: true,
                        ticks: {
                            color: 'white'
                        },
                        grid: {
                            color: 'rgba(255, 255, 255, 0.2)'
                        }
                    }
                }
            }
        });
    }

    // Dipanggil saat komponen dimount
    onMount(() => {
        updateChart();
    });

    // Fungsi untuk mengganti mode tampilan antara bulan dan tahun
    function toggleDisplayMode(mode) {
        displayMode = mode;
        updateChart();
    }
</script>

<div class="px-8 lg:px-56 py-24 bg-gradient-to-b from-black via-emerald-950 to-black flex flex-col gap-16 justify-center items-center">
    <h2 class="text-3xl md:text-5xl tracking-loose text-center drop-shadow-[0_8px_6px_rgba(34,197,94,1)] bg-clip-text text-transparent bg-gradient-to-r from-teal-400 to-emerald-400 font-bold">
        Jumlah Penyakit Per {displayMode === 'bulan' ? 'Bulan' : 'Tahun'}
    </h2>
    <div class="flex gap-4 mb-4">
        <button on:click={() => toggleDisplayMode('bulan')} class="text-white px-3 py-2 rounded text-sm font-semibold" class:bg-emerald-500={displayMode === "bulan"} class:bg-emerald-800={displayMode === "tahun"}>Per Bulan</button>
        <button on:click={() => toggleDisplayMode('tahun')} class="text-white px-3 py-2 rounded text-sm font-semibold" class:bg-emerald-500={displayMode === "tahun"} class:bg-emerald-800={displayMode === "bulan"}>Per Tahun</button>
    </div>
    <canvas id="visitorChart" width="400" height="200"></canvas>
</div>

<style>
    canvas {
        background: transparent;
    }
    button {
        cursor: pointer;
    }
</style>
