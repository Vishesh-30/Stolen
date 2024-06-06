<template>
    <nav class="flex justify-between p-6 px-4 bg-green-50">
      <div class="flex justify-between items-center w-full">
        <div class="xl:w-1/4">
          <a class="flex items-center max-w-max ml-8" href="/dashboard">
            <img src="../assets/Logo_transp.png" alt="Stolen Logo" class="h-12">
            <span class="self-center text-2xl font-extrabold whitespace-nowrap dark:text-Gray pl-2">STOLEN</span>
          </a>
        </div>
        <div class="hidden xl:block xl:w-2/4">
          <ul class="flex justify-center">
            <li>
              <form @submit.prevent="search" class="relative flex items-center">
                <input type="text" v-model="searchQuery" name="search" placeholder="What are you looking for?" @keyup.enter="search"
                  class="rounded-3xl w-96 h-12 pl-5 pr-10 text-sm text-gray-600 placeholder-gray-400 bg-white border border-gray-300 focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-green-500 focus:ring-offset-2 transition duration-300 ease-in-out">
                <i class="absolute right-4 text-gray-400 fa-solid fa-magnifying-glass"></i>
              </form>
            </li>
          </ul>
        </div>
        <div class="hidden xl:block xl:w-1/4">
          <div class="flex items-center justify-end">
            <ul class="flex justify-center items-center">
              <li class="mr-10 cursor-pointer">
                <i class="fa-regular fa-bell text-2xl text-green-900 pt-0.5 hover:text-green-700 focus:text-green-700 transition duration-300 ease-in-out"></i>
              </li>
              <li class="mr-10 cursor-pointer">
                <i class="fa-solid fa-cart-shopping text-2xl text-green-900 pt-0.5 hover:text-green-700 focus:text-green-700 transition duration-300 ease-in-out"></i>
              </li>
              <li class="relative mr-10 cursor-pointer" @click="toggleDropdown">
                <i class="fa-regular fa-circle-user text-3xl text-green-900 hover:text-green-700 focus:text-green-700 transition duration-300 ease-in-out mr-7"></i>
                <ul v-if="dropdownOpen" class="absolute right-0 mt-2 w-48 bg-white border border-gray-300 rounded-lg shadow-lg z-10">
                  <li class="px-4 py-2 hover:bg-green-100 cursor-pointer transition duration-300 ease-in-out">
                    <i class="fa-regular fa-circle-user mr-3"></i>{{ username }}
                  </li>
                  <li class="px-4 py-2 hover:bg-green-100 cursor-pointer transition duration-300 ease-in-out"><i class="fa-solid fa-gear mr-3"></i>Settings</li>
                  <li @click="logout" class="px-4 py-2 hover:bg-green-100 cursor-pointer transition duration-300 ease-in-out">
                    <i class="fa-solid fa-arrow-right-from-bracket mr-3"></i>Logout
                  </li>
                </ul>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </nav>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  
  const username = localStorage.getItem('username');
  const router = useRouter();
  
  const dropdownOpen = ref(false);
  
  const toggleDropdown = () => {
    dropdownOpen.value = !dropdownOpen.value;
  };
  
  const logout = () => {
    localStorage.removeItem('username');
    localStorage.removeItem('access_token');
    router.push('/');
  };
  </script>
  