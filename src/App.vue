<template>
  <v-app>

    <v-main class="blue lighten-4">


    <!-- <AsosUI/> -->

    <!-- <NavBar/> -->
    
    <router-view></router-view>
    <!-- <Axiostest/> -->
    </v-main>
  </v-app>
</template>

<script>
// import AsosUI from  './components/AsosWebsite.vue';
// import Axiostest from './components/axios-testing.vue'

export default {
  name: 'App',

  components: {
    // AsosUI
  },

  data() {
    return {
      // asos: true
    };
  }
};
</script>
