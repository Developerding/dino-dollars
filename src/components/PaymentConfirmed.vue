<template>
    <v-app id="inspire" class="font">
      <v-app-bar app color="black" max-height="200">
        <router-link to="/AsosWebsite">
            <v-avatar class="mr-8" size="60"><img src="../assets/asos.jpg"></v-avatar>
        </router-link>
        <v-responsive align="center" justify="center" class="mr-4">
        <v-text-field dense flat hide-details rounded solo-inverted label="Search for Categories or Items" background-color="white"></v-text-field>
        </v-responsive>

        <router-link to="/ShoppingCart"><v-icon color="white">mdi-cart-outline</v-icon></router-link>
      </v-app-bar>
  
      <v-main>
        <v-row align="center" justify="center" style="align-items: center; font-size:25px; font-weight:bold" class="pt-10 mt-10">
            Your order has been confirmed!
        </v-row>
        <v-row align="center" justify="center">
            <v-icon color="green" style="font-size:80px" class="mt-3">mdi-checkbox-marked-circle</v-icon>
        </v-row>
        <v-row align="center" justify="center" style="font-size:23px" class="pt-3">
            Total Spent: $ 
        </v-row>
        <v-row align="center" justify="center" style="font-size:23px" class="pt-3 green--text">
            Dino Dollars Earned: 
        </v-row>
        <v-row align="center" justify="center" style="font-size:23px" class="pt-3">
            Dino Dollars Balance: 
        </v-row>
        <br><br><br>
        <v-row align="center" justify="center">
            <router-link to="/AsosWebsite" tag="v-btn" class="body">
                <v-btn>Continue Shopping</v-btn>
            </router-link>
            <v-col cols="1"></v-col>            
            <router-link to="/" tag="v-btn" class="body">
                <v-btn>Return to Dino Dollars</v-btn>
            </router-link>
        </v-row>
      </v-main>
    </v-app>
</template>


<!-- 
<template>
    <v-app id="inspire">
      <NavBar/>
  
      <v-main class="blue lighten-4" :style="{ background: 'linear-gradient(to bottom, #95C4CB, #214F84)', minHeight: '100vh' }" >
        </v-main>
        </v-app>
</template>


<script>
import NavBar from './NavBar.vue'
// import axios from 'axios'

export default {
  components: {
    NavBar
  },
  data () {
  }
}
</script> -->