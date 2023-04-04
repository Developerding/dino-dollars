<template>
  <v-col class="col-md-3">
  <v-card elevation="2" outlined class="pa-4" tile>

    <v-img :src="ItemImage" :width="250">
    </v-img>
    <v-card-title>
      <!-- Needs to be dynamic -->
      {{ ItemName }}
    </v-card-title>

    <v-card-subtitle>
      {{ ItemPrice }}
    </v-card-subtitle>

    <v-btn
    color="blue-darken-4"
      v-on:click="addItemToCart( ItemName, ItemPrice, ItemImage )">
    ADD TO CART
    </v-btn>

  </v-card>
</v-col>
</template>

<script>
// import {mapActions, mapGetters} from 'vuex'

export default {
    name: "ItemCard",
    props: {
      ItemImage: String,
      ItemName: String,
      ItemPrice: Number,
      // ItemID: Number
    },
    methods: {
      addItemToCart: function(ItemName, ItemPrice,ItemImage) {
        this.$store.dispatch('addItemToCart', {ItemName, ItemPrice, ItemImage})
      }
    },
    created(){
  
    }
}
</script>
