<template>
    <v-app id="inspire">
      <NavBar/>
  
      <v-main class="blue lighten-4" >
        <v-container>
          <v-row>
            <v-col align="center" justify="center">
              <h1>Dino Dollars</h1>
              <h2 class="font-weight-medium">Spend. Redeem. Save.</h2>
              <h3 class="font-weight-light">Dino Dollars is a voucher system that helps consumers save with every dollar spent!</h3>
            </v-col>
            <v-col align="center" justify="center" >
              <v-img src="../assets/dinodollar logo.jpg" width="200" height="200"></v-img> <!-- change image -->
            </v-col>
            
          </v-row>

          <br><br>

          <!-- carousel of partners -->

          <v-div align="center" justify="center">
            <h2 class="font-weight-medium">Earn Dino Dollars with our Partners!</h2><br>

            <v-carousel hide-delimiters v-model="model" width="300" height="320" align="center">
              <v-carousel-item reverse-transition="fade-transition" transition="fade-transition">
                <router-link to="/AsosVouchers">
                  <v-img src="../assets/asos.jpg" width="300" height="300" justify="center" align="center" class="rounded-xl elevation-5"></v-img>
                </router-link>

              </v-carousel-item>

              <v-carousel-item reverse-transition="fade-transition" transition="fade-transition" align-center justify>
                <v-img src="../assets/adidas.jpg" width="300" height="300" justify="center" align="center" class="rounded-xl elevation-5"></v-img>
              </v-carousel-item>
              <v-carousel-item reverse-transition="fade-transition" transition="fade-transition" align-center justify>
                <v-img src="../assets/nike.jpg" width="300" height="300" justify="center" align="center" class="rounded-xl elevation-5"></v-img>
              </v-carousel-item>
              <v-carousel-item reverse-transition="fade-transition" transition="fade-transition" align-center justify>
                <v-img src="../assets/apple.jpg" width="300" height="300" justify="center" align="center" class="rounded-xl elevation-5"></v-img>
              </v-carousel-item>
              <v-carousel-item reverse-transition="fade-transition" transition="fade-transition" align-center justify>
                <v-img src="../assets/puma.jpg" width="300" height="300" justify="center" align="center" class="rounded-xl elevation-5"></v-img>
              </v-carousel-item>
            </v-carousel>
          </v-div>

          <!-- instructions -->
          <br><br>

          <v-div>
            <h2 font-weight-medium align="center">How to earn Dino Dollars?</h2><br>
            <v-row>
              <v-col class="col-3">
                <v-card height="180" class="rounded-xl">
                  <v-card-title class="justify-center">Link</v-card-title>
                  <v-card-text class="justify-center">Connect your DinoDollars account with our partner companies to get started.</v-card-text>
                </v-card>
              </v-col>
              <v-col class="col-3">
                <v-card height="180" class="rounded-xl">
                  <v-card-title class="justify-center">Spend</v-card-title>
                  <v-card-text>Make a purchase from one of our partner companies and receive DinoDollars for every dollar spent. $1 = 10 DinoDollars!</v-card-text>
                </v-card>
              </v-col>
              <v-col class="col-3">
                <v-card height="180" class="rounded-xl">
                  <v-card-title class="justify-center">Redeem</v-card-title>
                  <v-card-text>Choose from a wide range of Dino vouchers from your favourite brands and redeem them using your DinoDollars.</v-card-text>
                </v-card>
              </v-col>
              <v-col class="col-3">
                <v-card height="180" class="rounded-xl">
                  <v-card-title class="justify-center">Save</v-card-title>
                  <v-card-text>Use Dino vouchers to save money on your purchases and enjoy exclusive discounts that you won't find anywhere else.</v-card-text>
                </v-card>
              </v-col>
            </v-row>
            
          </v-div>
          
          
        </v-container>
  
      </v-main>
    </v-app>
  </template>

<script>
import NavBar from './NavBar.vue'

export default {
  components: {
    NavBar
  },
  data () {
    return {
      partners: [
        {name: 'Asos', src:'../assets/asos.jpg'},
        {name: 'Adidas', src:'../assets/adidas.jpg'},
        {name: 'Nike', src:'../assets/nike.jpg'},
        {name: 'Apple', src:'../assets/apple.jpg'},
        {name: 'Puma', src:'../assets/puma.jpg'},
      ],
    }
  },
}
</script>

<style>
h1 {
  font-family: fredoka;
}

</style>