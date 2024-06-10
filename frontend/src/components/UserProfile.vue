<template>
    <div>
      <Navbar />
      <div class="flex">
        <Sidebar />
        <main class="flex-grow container mx-auto px-6 py-12 text-left">
          <h2 class="text-2xl font-bold mb-6">Your Profile</h2>
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