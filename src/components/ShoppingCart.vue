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

      <v-btn v-on:click="removeAllItems">clear cart</v-btn>

      <v-btn v-on:click="pointsUpdate" large>checkout</v-btn>

      <v-btn v-on:click="paypalTest" large>test paypal</v-btn>

      <!-- <v-btn
        v-on:click="validatingVoucher"
        large
        >test validation</v-btn> -->
    </div>
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
      return this.$store.getters.cartTotal;
    },
  },
  methods: {
    removeAllItems: function () {
      this.$store.dispatch("removeAllItems");
    },
    pointsUpdate: function () {
      this.$store.dispatch("pointsUpdate");
    },
    paypalTest: function () {
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
      // MAKE DYNAMIC BY GETTING UID FROM STATE
      let url = "http://localhost:6003/add_points/1" 
      let data = {"Points": amountSpent}

      axios.post(url,data)
      .then(response => {
        console.log(response)
      })
      .catch(error => {
        console.log(error)
      })
    }

    // validatingVoucher: function() {
    //   axios.get('http://localhost:6001/validate_voucher/1')
    //   .then(response => {
    //     console.log(response.data)
    //   })
    //   .catch(error => {
    //     console.log(error.message)
    //   })
    // }

    // removeItem: function(item) {
    //     this.$store.dispatch('removeItem', item)
    // }
  },
  mounted: function() {
    this.getToken();
  }
};
</script>
