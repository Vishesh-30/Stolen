<template>
    <div class="hidden xl:block xl:w-1/4 h-screen bg-white p-5 border-r border-gray-200 shadow-lg">
      <!-- Top Card with Total Investment -->
      <div class="bg-green-700 text-white rounded-xl shadow-md p-5 mb-8 shadow-lg hover:shadow-2xl transition duration-300 ease-in-out cursor-pointer">
        <p class="text-sm font-semibold">Your Investments</p>
        <p class="text-2xl font-bold">$5380,90</p>
        <p class="text-sm text-green-400 mt-1">+18,10% <i class="fas fa-arrow-up"></i></p>
      </div>
  
      <!-- Navigation Menu -->
      <nav>
        <ul>
          <li class="mb-4">
            <router-link to="/home" exact-active-class="active-tab" class="flex items-center text-gray-700 hover:text-green-600 transition-colors pl-7 transition duration-300 ease-in-out">
              <i class="fas fa-home text-xl mr-4"></i>
              <span class="text-lg">Home</span>
            </router-link>
          </li>
          <li class="mb-4">
            <router-link to="/dashboard" exact-active-class="active-tab" class="flex items-center text-gray-700 hover:text-green-600 transition-colors pl-7 transition duration-300 ease-in-out">
              <i class="fas fa-th-large text-xl mr-4"></i>
              <span class="text-lg">Dashboard</span>
            </router-link>
          </li>
          <li class="mb-4">
            <router-link to="/wallet" exact-active-class="active-tab" class="flex items-center text-gray-700 hover:text-green-600 transition-colors pl-7 transition duration-300 ease-in-out">
              <i class="fas fa-wallet text-xl mr-4"></i>
              <span class="text-lg">Wallet</span>
            </router-link>
          </li>
          <li class="mb-4">
            <router-link to="/news" exact-active-class="active-tab" class="flex items-center text-gray-700 hover:text-green-600 transition-colors pl-7 transition duration-300 ease-in-out">
              <i class="fas fa-newspaper text-xl mr-4"></i>
              <span class="text-lg">News</span>
            </router-link>
          </li>
        </ul>
      </nav>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SideBar',
  }
  </script>
  
  <style scoped>
  .active-tab {
    padding: 7px;
    background-color: #d1fae5; /* light green background */
    color: #065f46; /* dark green text */
    border-radius: 0.5rem; /* optional: rounded corners */
    transition: background-color 0.3s ease-in-out;
  }
  </style>
  