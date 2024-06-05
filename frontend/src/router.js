import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from './components/LandingPage.vue';
import HelloWorld from './components/HelloWorld.vue';
import UserRegister from './components/UserRegister.vue';
import UserLogin from './components/UserLogin.vue';
import UserDashboard from './components/UserDashboard.vue';



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
    }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
