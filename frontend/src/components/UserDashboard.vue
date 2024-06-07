<template>
    <div>
      <Navbar />
      <div class="flex">
        <Sidebar />
        <main class="flex-grow container mx-auto px-6 py-6 text-left bg-gray-100">
          <h2 class="text-2xl font-bold mb-6">Top Stocks</h2>
          <div class="p-6 bg-white rounded-lg">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              <div v-for="stock in stocks" :key="stock.id" class="bg-white rounded-xl hover:shadow-lg hover:bg-green-50 p-6 flex flex-col items-center transition duration-300 ease-in-out cursor-pointer">
                <div class="mb-4">
                  <img :src="stock.logo" alt="Company Logo" class="h-12 w-12">
                </div>
                <h3 class="text-lg font-semibold mb-2">{{ stock.name }}</h3>
                <p class="text-gray-500">Total Shares</p>
                <p class="text-2xl font-bold mb-2">Rs.{{ stock.price }}</p>
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
  
  export default {
    name: 'UserDashboard',
    components: {
      Navbar,
      Sidebar,
    },
    data() {
    return {
      stocks: [
        {
          id: 1,
          name: 'Apple',
          logo: 'https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg',
          price: '310,40',
          return: '-1.10'
        },
        {
          id: 2,
          name: 'Meta',
          logo: 'https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg',
          price: '140,45',
          return: '-0.10'
        },
        {
          id: 3,
          name: 'Microsoft',
          logo: 'https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg',
          price: '240,98',
          return: '+0.85'
        },
        {
          id: 4,
          name: 'Google',
          logo: 'https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg',
          price: '99,12',
          return: '-0.04'
        }
      ]
    }
  }
  }
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
  