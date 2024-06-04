
<template>
    <nav class="flex justify-between p-6 px-4 bg-green-50">
                <div class="flex justify-between items-center w-full">
                    <div class="xl:w-1/3">
                        <a class="flex items-center max-w-max ml-8" href="/">
                            <img src="../assets/Logo_transp.png" alt="Stolen Logo" class="h-12">
                            <span class="self-center text-2xl font-extrabold whitespace-nowrap dark:text-Gray pl-2">STOLEN</span>
                        </a>
                    </div>
                    <div class="hidden xl:block xl:w-1/3">
                        <ul class="flex justify-center">
                            <li class="mr-12"><a class="text-coolGray-500 hover:text-coolGray-900 font-medium" href="#">Why us?</a></li>
                            <li class="mr-12"><a class="text-coolGray-500 hover:text-coolGray-900 font-medium" href="#">Our Vision</a></li>
                            <li class="mr-12"><a class="text-coolGray-500 hover:text-coolGray-900 font-medium" href="#">Our Mission</a></li>
                            <li><a class="text-coolGray-500 hover:text-coolGray-900 font-medium" href="#">Stolen Coins</a></li>
                        </ul>
                    </div>
                    <div class="hidden xl:block xl:w-1/3">
                        <div class="flex items-center justify-end">
                            <a class="inline-block py-2 px-4 mr-2 leading-5 text-coolGray-500 hover:text-coolGray-900 bg-transparent font-medium rounded-md" href="/LogIn">Log In</a>
                            <a class="inline-block py-2 px-4 text-sm leading-5 text-green-50 bg-green-500 hover:bg-green-600 font-medium focus:ring-2 focus:ring-green-500 focus:ring-opacity-50 rounded-md transition duration-300 ease-in-out" href="/SignUp">Sign Up</a>
                        </div>
                    </div>
                </div>
            </nav>
</template>

<script>
export default {
    name: 'LandingNav',
}
</script>