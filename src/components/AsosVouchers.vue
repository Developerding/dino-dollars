<template>
    <v-app id="inspire">
        <v-main class="blue lighten-4">
            <NavBar/>
            <v-container align="center">
               
            <v-row>
                <v-col>
                <v-card class="rounded-lg py-0" max-width="300">
                    <v-list-item two-line align="center">
                    <v-list-item-content>
                        <div><img src="https://www.theclimatepledge.com/content/dam/amazonclimatepledge/signatory-logo/ASOS.png" width="200"></div>
                        <v-list-item-title class="text-h6 mb-1 font-weight-light">
                        Discover shopping online.
                        </v-list-item-title><br><br>
                        <div>
                            <v-btn max-width="200" class="text-center white--text" color="blue lighten-2" align="center" justify="center" router to="/AsosWebsite" @click="asos = true">Shop now!</v-btn> <!-- link to asos website -->
                        </div><br>
                    </v-list-item-content>
                    </v-list-item>
                </v-card><br>

                <v-card class="rounded-lg py-0" max-width="300">
                    <v-list-item align="center">
                    <v-list-item-content>
                        <v-list-item class="text-h6 mb-1 font-weight-medium py-2">
                            To ensure voucher eligibility
                        </v-list-item>
                        <v-list-item class="text-h6 mb-1 font-weight-medium py-2">
                        DOs:
                        </v-list-item>
                        <v-list-item>
                            - Check the expiry date<br>
                        </v-list-item>
                    </v-list-item-content>
                    </v-list-item>
                </v-card>
            </v-col>
            <v-col>
                <v-div>
                    <h2>Available Vouchers:</h2><br>
                    <!-- implement code to determine number of vouchers to display -->
                    <Voucher_Purchase/><br>
                    <Voucher_Purchase/><br>
                    <Voucher_Purchase/>
                </v-div>
            </v-col>
            </v-row>
            </v-container>
            

        </v-main>
    </v-app>

</template>

<script>
import Voucher_Purchase from './Voucher_Purchase.vue'
import NavBar from './NavBar'

export default {
  name: 'AsosVouchers',

  components: {
    Voucher_Purchase,
    NavBar
  },

  data () {
    return {
      asos: false,
    }
  },
};
</script>