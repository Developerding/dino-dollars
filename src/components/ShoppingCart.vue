<template>
  <v-app>
    <v-app-bar app color="black" max-height="200">
      <router-link to="/AsosWebsite">
          <v-avatar class="mr-12" size="60"><img src="../assets/asos.jpg"></v-avatar>
      </router-link>
      <v-responsive align="center" justify="center">
      <v-text-field dense flat hide-details rounded solo-inverted label="Search for Categories or Stores" background-color="white"></v-text-field>
      </v-responsive>

      <router-link to="/ShoppingCart"><v-icon color="white">mdi-cart-outline</v-icon></router-link>
    </v-app-bar>

    <v-main v-if="cartItems.length == 0">
        <v-container>
            <v-row align="center" justify="center">
                <v-icon color="black">mdi-basket-fill</v-icon>
            </v-row>
            <v-row align="center" justify="center" >
                Your cart is empty.
            </v-row>
            <v-row align="center" justify="center" >
                <v-btn router to="/AsosWebsite">Start shopping!</v-btn>
            </v-row><br><br>
            <v-row align="center" justify="center" >
                Connnect to Dino Dollars to redeem vouchers!
            </v-row>
            <v-row align="center" justify="center" >
                <v-btn :to="{name: 'LoginSignup'}">Link my Dino Dollars account</v-btn>
            </v-row>
        </v-container>
    </v-main>

    <v-main v-else>
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

      <v-btn v-on:click="removeAllItems">Clear Cart</v-btn>

      <!-- <v-btn v-on:click="pointsUpdate" large>checkout</v-btn> -->

      <v-btn v-on:click="checkoutCart" large>Checkout</v-btn>

      <!-- <v-btn
        v-on:click="validatingVoucher"
        large
        >test validation</v-btn> -->
    </v-main>

  </v-app>
</template>

<script>
import axios from "axios";

export default {
  name: "ShoppingCart",
  data: () => ({
    token: ""
  }),
  computed: {
    cartItems() {
      return this.$store.state.cart;
    },
    cartTotal() {
      let state = this.$store.state

      state.cart.forEach(item => {
        state.amount += item.price
      })

      return state.amount
    },
    
  },
  methods: {
    removeAllItems: function () {
      this.$store.dispatch("removeAllItems");
    },
    pointsUpdate: function () {
      this.$store.dispatch("pointsUpdate");
    },
    currentUser() {
      return this.$store.getters.getUser;
    },
    checkoutCart: function () {
      // this.$store.dispatch('paypalTest')
      let authToken = "Bearer " + this.token
      let value = this.cartTotal
    
      let data = {
          "intent": "CAPTURE",
          "purchase_units": [
              {
                  "amount": {
                      "currency_code": "USD",
                      "value": value
                  }
              }
          ]
      } 

      let config = {
          headers: {
              "Content-Type": "application/json",
              "Prefer": "return=representation",
              "Authorization": authToken
          }
        }

      axios.post('https://api-m.sandbox.paypal.com/v2/checkout/orders', 
          data, config
      )
      .then(response => {
          // console.log(response)
          let amountSpent = response.data.purchase_units[0].amount.value
          this.pointsAccumulation(amountSpent)
      })
      .catch(error => {
          console.log(error)
      })
    },
    async paypalAuth(){
      return axios({
        url: 'https://api.sandbox.paypal.com/v1/oauth2/token',
        method: 'post',
        headers: { 
            'Accept': 'application/json', 
            'Accept-Language': 'en_US',
            'Content-Type':'application/x-www-form-urlencoded',
            'Access-Control-Allow-Origin': '*', 
        },
        data: { 'grant_type':'client_credentials' },
        auth: {
          username: 'AfhfcAANPYIAq90OTmgdpm11kw9wYoiQU635f5NinRCJa5yXRU1f3UaXTTpRYwvpyjrb5fjyiaMkixUp',
          password: 'EFEP1zHTJlER95z51Vu4xUvMgqz3NBaXEYsXRTbxdLcy5ziX4Jt-N1dUMV86dW4t0dxN-WDbMm-m6x8I'
        }
      })
      .then(response => {
        // console.log(response.data.access_token)
        return response.data.access_token
      })
      .catch(error => {
        console.log(error)
      })
    },

    getToken: async function() {
      let response = await this.paypalAuth()
      this.token = response
    },

    pointsAccumulation: function(amountSpent) {
      let currentUser = this.currentUser()
      let currentUID = currentUser.UID
      // console.log(currentUID.UID)

      let url = "http://localhost:6003/add_points/" + currentUID
      let data = {"Points": amountSpent}

      axios.post(url,data)
      .then(response => {
        console.log(response)
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
  mounted: function() {
    this.getToken();
  }
};
</script>
