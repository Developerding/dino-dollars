<template>
    <v-app id="inspire">
        <v-main class="blue lighten-4">
            <NavBar/>
            <v-container align="center">
               
            <v-row>
                <v-col class="col-4">
                <v-card class="rounded-lg py-0 my-0" max-width="300">
                    <v-list-item two-line align="center">
                    <v-list-item-content>
                        <div><img src="https://www.theclimatepledge.com/content/dam/amazonclimatepledge/signatory-logo/ASOS.png" width="200"></div>
                        <v-list-item-title class="text-h6 font-weight-light">
                        Discover shopping online.
                        </v-list-item-title><br><br>
                        <div>
                            <PopUp_ShopNow/>
                        </div><br><br><br>
                    </v-list-item-content>
                    </v-list-item>
                </v-card><br>

                <v-card class="rounded-lg py-0" max-width="300">
                    <v-list-item align="center">
                    <v-list-item-content>
                        <v-list-item class="text-h6 mb-1 font-weight-medium py-1">
                            Ensure voucher eligibility:
                        </v-list-item>
                        <v-list-item align="left">
                            - Check voucher's expiration date
                        </v-list-item>
                        <v-list-item align="left">
                            - Read the terms and conditions
                        </v-list-item>
                    </v-list-item-content>
                    </v-list-item>
                </v-card>
            </v-col>

            <v-col>
                <h2>Available Vouchers:</h2><br>
                <!-- implement code to determine number of vouchers to display -->
                <Voucher_Purchase/><br>
                <Voucher_Purchase/><br>
                <Voucher_Purchase/>
            </v-col>
            </v-row>
            </v-container>

        </v-main>
    </v-app>

</template>

<script>
import Voucher_Purchase from './Voucher_Purchase.vue'
import NavBar from './NavBar'
import PopUp_ShopNow from './PopUp_ShopNow.vue';



export default {
  name: 'AsosVouchers',

  components: {
    Voucher_Purchase,
    NavBar,
    PopUp_ShopNow
  },

  data () {
    return {
      asos: false,
    }
  },
};
</script>