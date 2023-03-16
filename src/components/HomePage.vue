<template>
  
    <v-app id="inspire">
  
      <v-main class="blue lighten-4" >
        <v-container>
          <v-div align="center">
            <h1>Dino Dollars</h1>
            <h2 class="font-weight-medium">Spend. Redeem. Save.</h2>
            <h3 class="font-weight-light">Dino Dollars is a voucher system that helps consumers save with every dollar spent!</h3>
          </v-div>

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
          <br>

          <v-div>
            <h2 font-weight-medium align="center">How to earn Dino Dollars?</h2>
            <v-row>
              <v-img src=""></v-img>
              <v-card>Link</v-card>
            </v-row>
            
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