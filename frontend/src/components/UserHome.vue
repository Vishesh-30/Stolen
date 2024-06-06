<template>
    <div>
      <Navbar />
      <div class="flex">
        <Sidebar />
        <main class="flex-grow container mx-auto px-6 py-12 text-left">
          <h2 class="text-6xl font-bold ml-10 pt-20 text-gray-800">Welcome to Stolen</h2>
          <p class="mt-4 text-lg ml-10 text-gray-600">
            The Stock Learn Project, This is a simple Web app that allows you to learn stock market.
          </p>
          <router-link to="/about" class="mt-8 ml-10 mb-4 inline-block bg-green-600 text-white text-lg font-semibold py-3 px-6 rounded-lg hover:bg-green-700">
            Learn More
          </router-link>
        </main>
      </div>
    </div>
  </template>
  
  <script>
  import Navbar from '@/components/NavBar.vue';
  import Sidebar from '@/components/SideBar.vue';
  
  export default {
    name: 'UserHome',
    components: {
      Navbar,
      Sidebar,
    },
  }
  </script>
  