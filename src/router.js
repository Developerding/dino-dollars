import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from './components/HomePage.vue'
import BuyVouchers from './components/BuyVouchers.vue'
import MyVouchers from './components/MyVouchers.vue'
import RedemptionHistory from './components/RedemptionHistory.vue'
import AsosVouchers from './components/AsosVouchers.vue'
import PopUp from './components/PopUp.vue'

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
            path: '/PopUp',
            name: 'PopUp',
            component: PopUp
        }
    ]
})