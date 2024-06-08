<template>
  <div>
    <Navbar />
    <div class="flex">
      <Sidebar />
      <main class="flex-grow container mx-auto px-6 py-6 text-left bg-gray-100">
        <h2 class="text-2xl font-bold mb-6">Top Stocks</h2>
        <div class="p-6 bg-white rounded-lg">
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div v-for="(stock, index) in stocks" :key="index" class="bg-white rounded-xl hover:shadow-lg hover:bg-green-50 p-6 flex flex-col items-center transition duration-500 ease-in-out cursor-pointer">
              <div class="mb-4">
                <img :src="stock.logo" alt="Company Logo" class="h-12 w-12" @error="stock.logo = 'path/to/default/logo.png'">
              </div>
              <h3 class="text-lg font-semibold mb-2">{{ stock.name }}</h3>
              <p class="text-gray-500">Total Share Price</p>
              <p class="text-2xl font-bold mb-2">Rs {{ stock.price }}</p>
              <p class="text-gray-500">Total Return</p>
              <p :class="{'text-green-500': stock.return > 0, 'text-red-500': stock.return < 0}">
                {{ stock.return }}% <i :class="{'fas fa-arrow-up': stock.return > 0, 'fas fa-arrow-down': stock.return < 0}"></i>
              </p>
            </div>
          </div>
        </div>
        <div class="flex flex-wrap mt-6 ">
          <div class="xl:w-8/12 pr-4">
            <div class="p-6 bg-white rounded-lg">
              <h2 class="text-2xl font-bold mb-6">Top Gainers</h2>
            </div>
          </div>
          <div class="xl:w-96">
            <div class="p-6 bg-white rounded-lg">
              <h2 class="text-2xl font-bold mb-6">Your Watch List</h2>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import Navbar from '@/components/NavBar.vue';
import Sidebar from '@/components/SideBar.vue';
import axios from 'axios';
import tickerToNameMappings from '@/assets/mapping.json';

const logoMappings = {
  'BHARTIARTL': 'airtel'
};
const tickerOrder = ['RELIANCE', 'TCS', 'HDFCBANK', 'BHARTIARTL'];


export default {
  name: 'UserDashboard',
  components: {
    Navbar,
    Sidebar,
  },
  data() {
    return {
      stocks: []
    }
  },
  methods: {
    async fetchStocksData() {
      try {
        const response = await axios.get('http://localhost:5000/api/top-stocks');
        const data = response.data;

        // Transform and sort the data
        let transformedData = [];
        for (let date in data) {
          for (let ticker in data[date]) {
            const stockData = data[date][ticker];
            const name_ns = ticker.replace('.NS', '');

            const name = tickerToNameMappings[name_ns];

            const logoKey = logoMappings[name_ns] || name_ns.toLowerCase();
            const logoUrl = `https://logo.clearbit.com/${logoKey}.com`;

            transformedData.push({
              name_ns,
              name,
              logo: logoUrl,
              price: stockData.Close.toFixed(2),
              return: ((stockData.Close - stockData.Open) / stockData.Open * 100).toFixed(2)
            });
          }
        }

        // Sort the transformed data according to tickerOrder
        transformedData.sort((a, b) => {
          return tickerOrder.indexOf(a.name_ns) - tickerOrder.indexOf(b.name_ns);
        });

        // Update the component's state
        this.stocks = transformedData;
      } catch (error) {
        console.error("Error fetching stocks data:", error);
      }
    }
  },
  mounted() {
    this.fetchStocksData();
  }
};
</script>

<style scoped>
.grid {
  display: grid;
  gap: 1.5rem;
}

@media (min-width: 768px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .grid {
    grid-template-columns: repeat(4, 1fr);
  }
}
</style>





  