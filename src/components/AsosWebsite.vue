<template>
    <v-app id="inspire">
      <v-app-bar app>
        <v-avatar class="mr-10" color="white" size="60" tile><img src="../assets/asos.jpg"></v-avatar>
        <v-responsive align="center" justify="center">
        <v-text-field dense flat hide-details rounded solo-inverted label="Search for categories or stores" ></v-text-field>
        </v-responsive>
      </v-app-bar>
<!--   
      <v-navigation-drawer
        v-model="drawer"
        fixed
        temporary
      >
      </v-navigation-drawer> -->
  
      <v-main class="grey lighten-2">
        <v-container>
          <v-row>
            <template v-for="n in 4">
              <v-col
                :key="n"
                class="mt-2"
                cols="12"
              >
                <strong>Category {{ n }}</strong>
              </v-col>
  
              <v-col
                v-for="j in 6"
                :key="`${n}${j}`"
                cols="6"
                md="2"
              >
                <v-sheet height="150"></v-sheet>
              </v-col>
            </template>
          </v-row>
        </v-container>
      </v-main>
    </v-app>
  </template>
  
  <script>
    export default {
      data: () => ({ drawer: null }),
    }
  </script>