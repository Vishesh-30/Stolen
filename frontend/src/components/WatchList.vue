<template>
  <div>
    <Navbar />
    <div class="flex bg-green-100">
      <Sidebar />
      <main class="flex-grow container justify-between mx-auto px-8 py-8 text-left">
        <div class="p-6 bg-white mt-6 rounded-lg">
          <h2 class="text-2xl mb-6 font-bold">Your Watch List</h2>
          <div v-if="watchlist.length > 0">
            <ul>
              <li v-for="(item, index) in watchlist" :key="index" class="rounded-xl hover:shadow-lg hover:bg-green-50 items-center transition duration-500 ease-in-out cursor-pointer">
                <div class="flex items-center justify-between p-4">
                  <span class="font-bold text-xl ml-5">{{ item.stock_name }}</span>
                  <span class="ml-2">Rs {{ item.current_price }}</span>
                </div>
                <hr class="w-full border-gray-200" />
              </li>
            </ul>
          </div>
          <div v-else>
            <p class="text-gray-500">Your watchlist is empty.</p>
          </div>
          </div>
        <h2 class="text-2xl m-5 font-bold text-gray-800">Add To Watchlist</h2>
        <div class="p-6 bg-white mt-6 rounded-lg">
          <form @submit.prevent="addToWatchlist">
            <select v-model="selectedStock" name="stock" id="stock" class="w-full p-4 mb-4 bg-gray-100 rounded-lg">
              <option disabled value="">Select a stock</option>
              <option v-for="(name, ticker) in stocks" :key="ticker" :value="ticker">{{ name }}</option>
            </select>
            <button type="submit" class="bg-green-500 hover:bg-green-600 text-white font-semibold py-2 px-4 rounded-lg focus:outline-none focus:ring focus:ring-green-500 focus:ring-offset-2 transition duration-300 ease-in-out cursor-pointer">
              Add to Watchlist
            </button>
          </form>
          <div v-if="message" :class="{'text-green-500': messageType === 'success', 'text-red-500': messageType === 'error'}" class="mt-4">
            {{ message }}
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import Navbar from '@/components/NavBar.vue';
import Sidebar from '@/components/SideBar.vue';
import tickerToNameMappings from '@/assets/mapping.json';
import axios from 'axios';

export default {
  name: 'WatchList',
  components: {
    Navbar,
    Sidebar,
  },
  data() {
    return {
      stocks: tickerToNameMappings,
      selectedStock: '',
      username: localStorage.getItem('username'), // Assuming you store the username in local storage
      watchlist: [], // Initialize watchlist as an empty array
      message: '',
      messageType: ''
    };
  },
  methods: {
    async addToWatchlist() {
      try {
        const response = await axios.post(`http://localhost:5000/api/watchlist/${this.username}/${this.selectedStock}`);
        console.log(response.data);
        this.message = 'Stock added to watchlist!';
        this.messageType = 'success';
        this.fetchWatchList(); // Refresh the watchlist after adding a stock
      } catch (error) {
        console.error('Error adding stock to watchlist:', error);
        this.message = 'Failed to add stock to watchlist or Already in Watchlist.';
        this.messageType = 'error';
      }
    },
    async fetchWatchList() {
      try {
        const response = await axios.get(`http://localhost:5000/api/watchlist/${this.username}`);
        const data = response.data;
        // Transform watchlist data
        const transformedWatchlist = data.map(item => ({
          id: item.id,
          user_id: item.user_id,
          stock_id: item.stock_id,
          stock_name: item.stock_name,
          current_price: parseFloat(item.current_price).toFixed(2) // Ensure current_price is formatted correctly
        }));
        // Update the component's state
        this.watchlist = transformedWatchlist;
      } catch (error) {
        console.error("Error fetching watchlist:", error);
      }
    }
  },
  mounted() {
    this.fetchWatchList(); // Fetch watchlist data when component mounts
  }
};
</script>

<style scoped>
/* Add your styles here */
</style>
