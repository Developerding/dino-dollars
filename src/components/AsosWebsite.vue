<template>
    <v-app id="inspire">
      <v-app-bar app color="black" max-height="200">
        <v-avatar class="mr-12" size="60"><img src="../assets/asos.jpg"></v-avatar>
        <v-responsive align="center" justify="center">
        <v-text-field dense flat hide-details rounded solo-inverted label="Search for Categories or Stores" background-color="white"></v-text-field>
        </v-responsive>
        <v-icon color="white">mdi-domain</v-icon>
      </v-app-bar>
  
      <v-main>
        <v-container>
          <v-row>
            <AsosHomeCarousel/>
          </v-row>
          <v-row>
            <!-- <template v-for="n in 4">
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
            </template> -->

            <v-col v-for="n in 12" :key="n" cols="4">
              <ItemCard
                item-name="testing"
                :item-price=10
              />
            </v-col>

            <v-btn router to="/ShoppingCart">To the Cart</v-btn>
          </v-row>
        </v-container>
      </v-main>
    </v-app>
  </template>
  
<script>
import AsosHomeCarousel from './AsosHomeCarousel.vue'
import ItemCard from "@/components/ItemCard.vue";
import {mapActions, mapGetters} from 'vuex'

  export default {
    components: {
      AsosHomeCarousel,
      ItemCard
    },
    data: () => ({ drawer: null }),
    computed: {
    // something() {
    //   return this.$store.state.cart
    // },
    // somethingChanged(){
    //   return this.$store.getters.somethingChanged
    // }
    ...mapGetters([
      'somethingChanged'
    ])
  },
  methods: {
    // changeName: function() {
    //   // this.$store.state.cart.forEach(something => {
    //   //   something.name = something.name + "&&&"
    //   // })

    //   this.$store.dispatch('changeName')
    // }
    ...mapActions([
      'changeName'
    ])
  }
  }
</script>