<template>
    <v-app id="inspire" class="font">
      <v-app-bar app color="black" max-height="200">
        <router-link to="/AsosWebsite">
            <v-avatar class="mr-8" size="60"><img src="../assets/asos.jpg"></v-avatar>
        </router-link>
        <v-responsive align="center" justify="center" class="mr-4">
        <v-text-field dense flat hide-details rounded solo-inverted label="Search for Categories or Stores" background-color="white"></v-text-field>
        </v-responsive>

        <router-link to="/ShoppingCart"><v-icon color="white">mdi-cart-outline</v-icon></router-link>
      </v-app-bar>
  
      <v-main>
        <v-container>
          <!-- <v-row>
            <AsosHomeCarousel/>
          </v-row> -->
          <v-row align="center" justify="center">
            <v-img src="../assets/AsosWebsite1.png"></v-img>
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

            <ItemCard
            v-for="(product, key) in products"
            :key="key"
            :item-name="product.name"
            :item-image="require(`@/assets/${product.image}`)"
            :item-price="product.price"
          />

          </v-row><br><br>
        </v-container>
      </v-main>
    </v-app>
  </template>
  
<script>
// import AsosHomeCarousel from './AsosHomeCarousel.vue'
import ItemCard from "@/components/ItemCard.vue";
import {mapActions, mapGetters} from 'vuex'
import axios from 'axios'

  export default {
    components: {
      // AsosHomeCarousel,
      ItemCard
    },
    data: () => ({ drawer: null },
    {
      products: {
        item1: {
          name: "Cargo Trousers",
          price: 48.15,
          image: "asos1.png"
        },
        item2: {
          name: "Cotton Jacket",
          price: 58.85,
          image: "asos2.png"
        },
        item3: {
          name: "Linen Jumpsuit",
          price: 101.64,
          image: "asos3.png"
        },
        item4: {
          name: "Midi Dress",
          price: 97.36,
          image: "asos4.png"
        }
      }
    }),
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
  },

  created(){
    const graphqlurl="http://localhost:5030/graphqlserver"
    const graphqlQuery = {
    "operationName": "Query",
    "query": `query Query { items { name price imageUrl } }`,
    "variables": {}
};
axios({url: graphqlurl, method:'get', data:graphqlQuery})
.then((response)=>{
  console.log(response)
})
.catch((err)=>{
  console.log(err)
})

}
  }
  
</script>