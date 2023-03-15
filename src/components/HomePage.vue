<template>
  
    <v-app id="inspire">
  
      <v-main class="blue lighten-4">
        <v-container>
          <v-div align="center" justify="center">
            <h1>Dino Dollars</h1>
            <h2 class="font-weight-medium">Spend. Redeem. Save.</h2>
            <h3 class="font-weight-light">Dino Dollars is a voucher system that helps consumers save with every dollar spent!</h3>
          </v-div>

          <br><br>

          <v-div align="center" justify="center">
            <h2 class="font-weight-medium">Earn Dino Dollars with our Partners!</h2>

            <v-carousel v-model="model">
              <v-carousel-item v-for="partner in partners" :key="partner.name" :src="partner.src"
              reverse-transition="fade-transition"
              transition="fade-transition"
            ></v-carousel-item>
            </v-carousel>
          </v-div>

          
          
        </v-container>
  
      </v-main>
    </v-app>
  </template>

<script>
export default {
  data () {
    return {
      partners: [
        {name: 'Asos', src: 'https://1000logos.net/wp-content/uploads/2021/04/Asos-logo.png'},
        {name: 'Adidas', src:''},
        {name: 'Nike', src:''},
      ],
    }
  },
}
</script>