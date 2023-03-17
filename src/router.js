import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from './components/HomePage.vue'
import BuyVouchers from './components/BuyVouchers.vue'
import MyVouchers from './components/MyVouchers.vue'
import RedemptionHistory from './components/RedemptionHistory.vue'
import AsosVouchers from './components/AsosVouchers.vue'
import PopUp_Purchase from './components/PopUp_Purchase.vue' 
import PopUp_ShopNow from './components/PopUp_ShopNow.vue' 
import LoginSignup from './components/LoginSignup.vue'
import AsosUI from "./components/AsosUI.vue"
import AsosWebsite from './components/AsosWebsite.vue'

Vue.use(VueRouter)

export default new VueRouter ({ 
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path:'/',
            name: 'HomePage',
            component: HomePage
        },
        {
            path: '/BuyVouchers',
            name: 'BuyVouchers',
            component: BuyVouchers
        },
        {
            path: '/MyVouchers',
            name: 'MyVouchers',
            component: MyVouchers
        },
        {
            path: '/RedemptionHistory',
            name: 'RedemptionHistory',
            component: RedemptionHistory
        },
        {
            path: '/AsosVouchers',
            name: 'AsosVouchers',
            component: AsosVouchers
        },
        {
            path: '/PopUp_Purchase',
            name: 'PopUp_Purchase',
            component: PopUp_Purchase
        },
        {
            path: '/PopUp_ShopNow',
            name: 'PopUp_ShopNow',
            component: PopUp_ShopNow
        },
        {
            path: '/LoginSignup',
            name: 'LoginSignup',
            component: LoginSignup
        },
        {
            path: '/AsosUI',
            name: 'AsosUI',
            component: AsosUI
        },
        {
            path: '/AsosWebsite',
            name: 'AsosWebsite',
            component: AsosWebsite
        }
    ]
})