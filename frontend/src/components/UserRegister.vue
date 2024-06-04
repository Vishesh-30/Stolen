<template>
    <div class="bg-green-100">
      <LandingNav />
      <div class="container mx-auto px-6 py-12 text-left">
        <div class="flex justify-center">
          <img src="../assets/Logo_transp.png" alt="Stolen Logo" class="h-12">
        </div>
  
        <div class="container mx-auto px-6 mt-5 py-12 text-left shadow-md bg-white rounded-lg h-auto w-1/2">
          <div class="flex justify-center mt-10">
            <h2 class="font-bold text-2xl">Create New User Account</h2>
          </div>
          <form @submit.prevent="submitForm" class="mt-8 space-y-6">
            <div class="rounded-md shadow-sm -space-y-px">
              <div>
                <label for="username" class="sr-only">Username</label>
                <input id="username" v-model="username" name="username" type="text" autocomplete="username" required
                  class="appearance-none mt-5 rounded relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-green-500 focus:border-green-500 focus:z-10 sm:text-sm" placeholder="Username">
              </div>
              <div>
                <label for="email" class="sr-only">Email address</label>
                <input id="email" v-model="email" name="email" type="email" autocomplete="email" required
                  class="appearance-none rounded mt-5 relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-green-500 focus:border-green-500 focus:z-10 sm:text-sm" placeholder="Email address">
              </div>
              <div>
                <label for="password" class="sr-only">Password</label>
                <div class="relative">
                  <input :type="passwordVisible ? 'text' : 'password'" id="password" v-model="password" name="password" required
                    class="appearance-none rounded mt-5 relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-green-500 focus:border-green-500 focus:z-10 sm:text-sm" placeholder="Password">
                  <button type="button" @click="togglePasswordVisibility" class="absolute inset-y-0 right-0 px-3 flex items-center">
                    <i :class="passwordVisible ? 'fa-regular fa-eye-slash' : 'fa-regular fa-eye'"></i>
                  </button>
                </div>
              </div>
            </div>
            <div class="flex items-center justify-between mt-4">
              <div class="flex items-center">
                <input id="remember_me" name="remember_me" type="checkbox" class="h-4 w-4 text-green-600 focus:ring-green-500 border-gray-300 rounded">
                <label for="remember_me" class="ml-2 block text-sm text-gray-900">
                  Remember me
                </label>
              </div>
              <div class="text-sm">
                <a href="/LogIn" class="font-medium text-green-600 hover:text-green-500 align">
                  Already a User?
                </a>
              </div>
            </div>
            <div>
              <button type="submit" class="group mt-5 relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500 transition duration-300 ease-in-out">
                Sign Up
              </button>
            </div>
          </form>
          <div class="flex items-center justify-center mt-4">
            <hr class="w-1/3 border-gray-300 mr-5">Or continue with<hr class="ml-5 w-1/3 border-gray-300">
          </div>
          <div class="flex items-center justify-center">
            <button class="group mt-5 relative w-full flex justify-center py-2 px-4 border border-green-600 text-sm font-medium rounded-md text-green-600 bg-white hover:bg-green-100 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500 transition duration-300 ease-in-out">
              <a href="#" class="flex items-center justify-center h-full">
                <img src="../assets/Google.png" alt="Google Logo" class="h-6">
                <span class="ml-2">Google</span>
              </a>
            </button>
          </div>
          <p class="mt-2 text-sm pt-8 text-gray-500">By creating an account, you agree to the <a href="#" class="font-medium text-gray-900 hover:text-gray-600">Terms of Service</a> and <a href="#" class="font-medium text-gray-900 hover:text-gray-600">Privacy Policy</a>.</p>
        </div>
      </div>
      <LandingFooter />
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import LandingNav from './LandingNav.vue';
  import LandingFooter from './LandingFooter.vue';
  
  const username = ref('');
  const email = ref('');
  const password = ref('');
  const passwordVisible = ref(false);
  const router = useRouter();
  
  const togglePasswordVisibility = () => {
    passwordVisible.value = !passwordVisible.value;
  };
  
  const submitForm = async () => {
    const formData = {
      username: username.value,
      email: email.value,
      password: password.value,
    };
    
    try {
      const response = await fetch('http://localhost:5000/api/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      const data = await response.json();
      console.log(data);
      localStorage.setItem('username', username.value);
      localStorage.setItem('token', data.access_token);
      router.push('/dashboard');
    } catch (error) {
      console.error('Error:', error);
    }
  };
  </script>
  
  <style>
  /* Add any additional styles if needed */
  </style>
  