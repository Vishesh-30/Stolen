<template>
    <div>
      <Navbar />
      <div class="flex">
        <Sidebar />
        <main class="flex-grow container mx-auto px-6 py-6 text-left bg-gray-100">
          <h2 class="text-2xl font-bold mb-6">{{ stockName }} ({{ ticker }})</h2>
          <div class="p-6 bg-white rounded-lg">
            <apexchart v-if="chartData" type="line" :options="chartOptions" :series="chartSeries" height="350"></apexchart>
            <div class="flex justify-between mt-6 ml-20 mr-20">
              <button v-for="period in periods" :key="period" @click="updateChart(period)" class="m-4 ml-8 mr-8 bg-white ring ring-green-100 hover:bg-green-200 text-gray-800 font-bold py-2 px-4 rounded-xl focus:outline-none focus:ring focus:ring-green-500 focus:ring-offset-0 focus:bg-white transition duration-300 ease-in-out cursor-pointer">
                {{ period }}
              </button>
            </div>
          </div>
          <div class="p-6 bg-white mt-6 rounded-lg">
            <h3 class="text-xl font-bold mb-4">Stock Information</h3>
            <p>{{ stockInfo }}</p>
          </div>
        </main>
      </div>
    </div>
  </template>
  
  <script>
  import Navbar from '@/components/NavBar.vue';
  import Sidebar from '@/components/SideBar.vue';
  import VueApexCharts from 'vue3-apexcharts';
  import dayjs from 'dayjs';
  
  export default {
    name: 'StockPage',
    components: {
      Navbar,
      Sidebar,
      apexchart: VueApexCharts
    },
    props: ['ticker'],
    data() {
      return {
        stockName: 'Random Company',
        stockInfo: 'This is some information about the stock.',
        periods: ['1D', '1W', '1M', '6M', '1Y', '5Y', 'all'],
        chartData: this.generateRandomData('1D'),
        chartOptions: {
          chart: {
            type: 'line',
            zoom: {
              enabled: false
            }
          },
          colors: ['#008000'], // Green color for the line
          xaxis: {
            type: 'datetime'
          },
          yaxis: {
            labels: {
              formatter: function (value) {
                return value.toFixed(2);
              }
            }
          },
        },
        chartSeries: [{
          name: 'Random Ticker',
          data: []
        }]
      };
    },
    methods: {
      updateChart(period) {
        this.chartData = this.generateRandomData(period);
        this.chartSeries = [{
          name: this.ticker,
          data: this.chartData
        }];
      },
      generateRandomData(period) {
        const data = [];
        const now = dayjs();
        let start;
  
        switch (period) {
          case '1D':
            start = now.subtract(1, 'day');
            for (let i = 0; i < 24; i++) {
              data.push([start.add(i, 'hour').valueOf(), (Math.random() * 100).toFixed(2)]);
            }
            break;
          case '1W':
            start = now.subtract(1, 'week');
            for (let i = 0; i < 7; i++) {
              data.push([start.add(i, 'day').valueOf(), (Math.random() * 100).toFixed(2)]);
            }
            break;
          case '1M':
            start = now.subtract(1, 'month');
            for (let i = 0; i < 30; i++) {
              data.push([start.add(i, 'day').valueOf(), (Math.random() * 100).toFixed(2)]);
            }
            break;
          case '6M':
            start = now.subtract(6, 'months');
            for (let i = 0; i < 180; i++) {
              data.push([start.add(i, 'day').valueOf(), (Math.random() * 100).toFixed(2)]);
            }
            break;
          case '1Y':
            start = now.subtract(1, 'year');
            for (let i = 0; i < 365; i++) {
              data.push([start.add(i, 'day').valueOf(), (Math.random() * 100).toFixed(2)]);
            }
            break;
          case '5Y':
            start = now.subtract(5, 'years');
            for (let i = 0; i < 5 * 365; i++) {
              data.push([start.add(i, 'day').valueOf(), (Math.random() * 100).toFixed(2)]);
            }
            break;
          case 'all':
            start = now.subtract(10, 'years');
            for (let i = 0; i < 10 * 365; i++) {
              data.push([start.add(i, 'day').valueOf(), (Math.random() * 100).toFixed(2)]);
            }
            break;
        }
  
        return data;
      }
    },
    mounted() {
      this.updateChart('1d'); // Default period
    }
  };
  </script>
  
  <style scoped>
  /* Add any custom styles here */
  </style>
  