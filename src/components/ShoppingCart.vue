<template>
  <v-app>
    <div>
        <ol>
            <li v-for="item in cartItems" :key="item.name">
                {{ item.name }}
                {{ item.price }}

                <!-- <v-btn
                    v-on:click="removeItem(item)"
                >
                Remove this damn item
                </v-btn> -->
            </li>
        </ol>

        <v-btn
        v-on:click="removeAllItems"
        >clear cart</v-btn>

        <v-btn
        v-on:click="checkoutCart"
        large
        >checkout</v-btn>
    </div>
  </v-app>
</template>

<script>
export default {
  name: "ShoppingCart",
  computed: {
    cartItems() {
      return this.$store.state.cart;
    },
  },
  methods: {
    removeAllItems: function() {
        this.$store.dispatch('removeAllItems')
    },
    checkoutCart: function() {
      this.$store.dispatch('checkoutCart')
    }
    // removeItem: function(item) {
    //     this.$store.dispatch('removeItem', item)
    // }
  }
};
</script>
