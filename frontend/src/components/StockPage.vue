<template>
  <div>
    <Navbar />
    <div class="flex">
      <Sidebar />
      <main class="flex-grow container mx-auto px-6 py-6 text-left bg-gray-100">
        <h2 class="text-2xl font-bold mb-6">{{ stockInfo.name }} ({{ ticker }})</h2>
        <h5 class="text-xl font-bold mb-4">Rs. {{ stockInfo.current_price }}</h5>
        <div class="p-6 bg-white rounded-lg">
          <apexchart v-if="chartData" type="line" :options="chartOptions" :series="chartSeries" height="350"></apexchart>
          <div class="flex justify-between mt-6 ml-20 mr-20">
            <button v-for="period in periods" :key="period" @click="updateChart(period)" class="m-4 ml-8 mr-8 bg-white ring ring-green-200 hover:bg-green-200 text-gray-800 font-bold py-2 px-4 rounded-xl focus:outline-none focus:ring focus:ring-green-500 focus:ring-offset-0 focus:bg-white transition duration-300 ease-in-out cursor-pointer">
              {{ period }}
            </button>
          </div>
        </div>
        <div class="p-6 bg-white mt-6 rounded-lg">
          <h3 class="text-xl font-bold mb-4">Stock Information</h3>
          <ul>
            <li><strong>Sector:</strong> {{ stockInfo.sector }}</li>
            <li><strong>Industry:</strong> {{ stockInfo.industry }}</li>
            <li><strong>Market Cap:</strong> {{ stockInfo.market_cap }}</li>
            <li><strong>Previous Close:</strong> {{ stockInfo.previous_close }}</li>
            <li><strong>Open:</strong> {{ stockInfo.open }}</li>
            <li><strong>Volume:</strong> {{ stockInfo.volume }}</li>
            <li><strong>Average Volume:</strong> {{ stockInfo.average_volume }}</li>
            <li><strong>P/E Ratio:</strong> {{ stockInfo.pe_ratio }}</li>
            <li><strong>Dividend Yield:</strong> {{ stockInfo.dividend_yield }}</li>
          </ul>
          <div class="justify-between">
            <button class="m-5 bg-green-500 hover:bg-green-600 text-white font-semibold py-2 px-4 rounded-lg focus:outline-none focus:ring focus:ring-green-500 focus:ring-offset-2 transition duration-300 ease-in-out cursor-pointer">
              Buy
            </button>
            <button class="m-5 bg-green-500 hover:bg-green-600 text-white font-semibold py-2 px-4 rounded-lg focus:outline-none focus:ring focus:ring-green-500 focus:ring-offset-2 transition duration-300 ease-in-out cursor-pointer">
              Sell
            </button>
            <button @click="addToWatchlist" class="m-5 bg-green-500 hover:bg-green-600 text-white font-semibold py-2 px-4 rounded-lg focus:outline-none focus:ring focus:ring-green-500 focus:ring-offset-2 transition duration-300 ease-in-out cursor-pointer">
              Add to Watchlist
            </button>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import Navbar from '@/components/NavBar.vue';
import Sidebar from '@/components/SideBar.vue';
import VueApexCharts from 'vue3-apexcharts';
import axios from 'axios';


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
      stockInfo: {},
      periods: ['1D', '5D', '1MO', '6MO', '1Y', '5Y', 'MAX'],
      chartData: [],
      chartOptions: {
        chart: {
          type: 'line',
          zoom: {
            enabled: false
          }
        },
        stroke: {
        width: 3 // Set the width of the line to be thinner
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
    async fetchStockInfo() {
      try {
        const response = await axios.get(`http://localhost:5000/api/stockinfo/${this.ticker}`);
        this.stockInfo = response.data;
      } catch (error) {
        console.error('Error fetching stock info:', error);
      }
    },
    async fetchStockHistory(period) {
      try {
        const response = await axios.get(`http://localhost:5000/api/stockhistory/${this.ticker}/${period}`);
        this.chartData = response.data.prices.map(point => [new Date(point.datetime).getTime(), parseFloat(point.price)]);
        this.chartSeries = [{
          name: this.ticker,
          data: this.chartData
        }];
        console.log(this.chartData);
      } catch (error) {
        console.error('Error fetching stock history:', error);
      }
    },
    updateChart(period) {
      this.fetchStockHistory(period.toLowerCase());
    },
    async addToWatchlist() {
      try {
        const username = localStorage.getItem('username');
        const response = await axios.post(`http://localhost:5000/api/watchlist/${username}/${this.ticker}`);
        console.log(response.data);
        alert('Stock added to watchlist!');
      } catch (error) {
        console.error('Error adding stock to watchlist:', error);
        alert('Failed to add stock to watchlist or Already in Watchlist.');
      }
    }
  },
  mounted() {
    this.fetchStockInfo();
    this.updateChart('1d'); // Default period
  }
};
</script>

<style scoped>
/* Add any custom styles here */
alert{
  position: fixed;
  top: 0;
  right: 0;
  background-color: #008000;
  color: white;
  padding: 1rem;
  z-index: 1000;
}
</style>
