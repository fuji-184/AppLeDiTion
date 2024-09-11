<script>
    export let data = [];

    import { onMount } from 'svelte';
    import Chart from 'chart.js/auto';

    let displayMode = 'bulan'; // Default mode 'bulan' (bulan atau tahun)
    let chartInstance;

    // Mengelompokkan data berdasarkan nama penyakit
    function groupData(mode) {
        let groupedData = {};
        let labels = new Set();

        data.forEach(item => {
            let key = mode === 'bulan' ? item.bulan : item.bulan.slice(0, 4); // Ambil tahun jika mode 'tahun'
            if (!groupedData[item.nama]) {
                groupedData[item.nama] = {};
            }
            if (!groupedData[item.nama][key]) {
                groupedData[item.nama][key] = 0;
            }
            groupedData[item.nama][key] += item.jumlah;
            labels.add(key);
        });

        return {
            labels: [...labels],
            datasets: Object.keys(groupedData).map(penyakit => {
                return {
                    label: penyakit,
                    data: [...labels].map(label => groupedData[penyakit][label] || 0),
                    borderColor: getRandomColor(),
                    backgroundColor: 'rgba(0, 0, 0, 0)',
                    fill: true
                };
            })
        };
    }

    function getRandomColor() {
        const letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }

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

    onMount(() => {
        updateChart();
    });

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
