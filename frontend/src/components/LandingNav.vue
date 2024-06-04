
<template>
    <nav class="flex justify-between p-6 px-4">
                <div class="flex justify-between items-center w-full">
                    <div class="xl:w-1/3">
                        <a class="block max-w-max ml-8" href="/">
                            <img src="../assets/Logo_transp.png" alt="Stolen Logo" class="h-8">
                        </a>
                    </div>
                    <div class="hidden xl:block xl:w-1/3">
                        <ul class="flex justify-center">
                            <li class="mr-12"><a class="text-coolGray-500 hover:text-coolGray-900 font-medium" href="#">Product</a></li>
                            <li class="mr-12"><a class="text-coolGray-500 hover:text-coolGray-900 font-medium" href="#">Features</a></li>
                            <li class="mr-12"><a class="text-coolGray-500 hover:text-coolGray-900 font-medium" href="#">Resources</a></li>
                            <li><a class="text-coolGray-500 hover:text-coolGray-900 font-medium" href="#">Pricing</a></li>
                        </ul>
                    </div>
                    <div class="hidden xl:block xl:w-1/3">
                        <div class="flex items-center justify-end">
                            <a class="inline-block py-2 px-4 mr-2 leading-5 text-coolGray-500 hover:text-coolGray-900 bg-transparent font-medium rounded-md" href="#">Log In</a>
                            <a class="inline-block py-2 px-4 text-sm leading-5 text-green-50 bg-green-500 hover:bg-green-600 font-medium focus:ring-2 focus:ring-green-500 focus:ring-opacity-50 rounded-md" href="#">Sign Up</a>
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