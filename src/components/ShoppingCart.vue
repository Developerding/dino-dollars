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
        
        <p>
          {{ cartTotal }}
        </p>
        

        <v-btn
        v-on:click="removeAllItems"
        >clear cart</v-btn>

        <v-btn
        v-on:click="pointsUpdate"
        large
        >checkout</v-btn>

        <v-btn
        v-on:click="paypalTest"
        large
        >test paypal</v-btn>

        <v-btn
        v-on:click="validatingVoucher"
        large
        >test validation</v-btn>
    </div>
  </v-app>
</template>

<script>
import axios from 'axios';

export default {
  name: "ShoppingCart",
  computed: {
    cartItems() {
      return this.$store.state.cart;
    },
    cartTotal() {
      return this.$store.getters.cartTotal
    }
  },
  methods: {
    removeAllItems: function() {
        this.$store.dispatch('removeAllItems')
    },
    pointsUpdate: function() {
      this.$store.dispatch('pointsUpdate')
    },
    paypalTest: function() {
      this.$store.dispatch('paypalTest')
    },
    validatingVoucher: function() {
      axios.get('http://localhost:6001/validate_vouchers/1', {

      })
      .then(response => {
        console.log(response.data)
      })
      .catch(error => {
        console.log(error.message)
      })
    }
    // removeItem: function(item) {
    //     this.$store.dispatch('removeItem', item)
    // }
  }
};
</script>
