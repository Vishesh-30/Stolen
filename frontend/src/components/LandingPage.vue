<template>
    <div>
      <header class="w-full bg-white shadow-md bg-green-50">
        <div class="container mx-auto">
          <LandingNav />
        </div>
      </header>
      <main class="flex-grow container mx-auto text-left flex mb-64">
        <div class="hidden xl:block xl:w-3/5">
          <div class="ml-10 mt-20">
            <h2 class="text-6xl font-bold ml-10 pt-20 text-gray-800">Welcome to Stolen</h2>
            <p class="mt-4 text-lg ml-10 text-gray-600">
              The Stock Learn Project, This is a simple Web app that allows you to learn stock market.
            </p>
            <router-link to="/about" class="mt-8 ml-10 mb-4 inline-block bg-green-600 text-white text-lg font-semibold py-3 px-6 rounded-lg hover:bg-green-700">
              Learn More
            </router-link>
          </div>
        </div>
        <div class="hidden xl:block xl:w-2/5">
          <LottieAnimation :animationData="animationData" />
        </div>
      </main>
      <LandingFooter />
    </div>
  </template>
  
  <script setup>
  import LandingNav from './LandingNav.vue';
  import LandingFooter from './LandingFooter.vue';
  import LottieAnimation from '@/components/LottieAnimation.vue';
  import animationData from '../assets/stock-market.json';
  
  </script>
  
  <style>
  /* Add any additional styling if necessary */
  </style>
  