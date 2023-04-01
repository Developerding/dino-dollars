<template>
    <v-app id="inspire">
      <v-app-bar app color="black" max-height="200">
        <router-link to="/AsosWebsite">
            <v-avatar class="mr-12" size="60"><img src="../assets/asos.jpg"></v-avatar>
        </router-link>
        <v-responsive align="center" justify="center">
        <v-text-field dense flat hide-details rounded solo-inverted label="Search for Categories or Stores" background-color="white"></v-text-field>
        </v-responsive>

        <router-link to="/AsosCart"><v-icon color="white">mdi-cart</v-icon></router-link>
      </v-app-bar>


      <v-main>
        <v-container>
            <v-row align="center" justify="center">
                <v-icon color="black">mdi-basket-fill</v-icon>
            </v-row>
            <v-row align="center" justify="center" >
                Your cart is empty.
            </v-row><br><br>
            <v-row align="center" justify="center" >
                Connnect to Dino Dollars to redeem vouchers!
            </v-row>
            <v-row align="center" justify="center" >
                <v-btn>Link my Dino Dollars account</v-btn>
            </v-row>
        </v-container>
      </v-main>
  </v-app>

