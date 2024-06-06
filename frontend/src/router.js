import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from './components/LandingPage.vue';
import HelloWorld from './components/HelloWorld.vue';
import UserRegister from './components/UserRegister.vue';
import UserLogin from './components/UserLogin.vue';
import UserDashboard from './components/UserDashboard.vue';
import UserHome from './components/UserHome.vue';
import StolenCoins from './components/StolenCoins.vue';


const routes = [
    {
        path: '/',
        name: 'LandingPage',
        component: LandingPage
    },
    {
        path: '/hello',
        name: 'HelloWorld',
        component: HelloWorld
    },
    {
        path: '/SignUp',
        name: 'UserRegister',
        component: UserRegister
    },
    {
        path: '/LogIn',
        name: 'UserLogin',
        component: UserLogin
    },
    {
        path: '/dashboard',
        name: 'UserDashboard',
        component: UserDashboard
    },
    {
        path: '/home',
        name: 'UserHome',
        component: UserHome
    },
    {
        path: '/wallet',
        name: 'StolenCoins',
        component: StolenCoins
    }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
