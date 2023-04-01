<template>
  <v-card elevation="2" outlined class="pa-4" tile>
    <v-img :src="ItemImage">
    </v-img>
    <v-card-title>
      <!-- Needs to be dynamic -->
      {{ ItemName }}
    </v-card-title>

    <v-card-subtitle>
      {{ ItemPrice }}
    </v-card-subtitle>

    <v-btn
      elevation="5"
      v-on:click="addItemToCart( ItemName, ItemPrice )">
    Add to cart now!
    </v-btn>

  </v-card>
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
      addItemToCart: function(ItemName, ItemPrice) {
        this.$store.dispatch('addItemToCart', {ItemName, ItemPrice})
      }
    }
}
</script>
