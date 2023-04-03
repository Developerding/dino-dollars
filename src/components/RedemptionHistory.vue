<template>
    <v-app id="inspire">
        <v-main class="blue lighten-4" :style="{ background: 'linear-gradient(to bottom, #214F84, #95C4CB)', minHeight: '100vh' }" >

        <NavBar/>

            <v-container align="center" class="white--text">

                <v-div align="center">
                    <h1>Vouchers Redemption History</h1>
                </v-div><br>

                <v-div>
                    <v-responsive>
                    <v-text-field dense flat hide-details rounded label="Search for categories or stores" height="50" class="white"></v-text-field>
                    </v-responsive>
                </v-div><br><br>

            <v-row>
            <v-col>
                <v-div>
                    <h2>Redeemed Vouchers:</h2><br>
                    <!-- implement code to determine number of vouchers to display -->
                    <Voucher_Redeemed/><br>
                    <Voucher_Redeemed/><br>
                    <Voucher_Redeemed/>
                </v-div>
            </v-col>
            </v-row>

     
            </v-container>            

        </v-main>
    </v-app>

</template>

<script>
import Voucher_Redeemed from './Voucher_Redeemed.vue'
import NavBar from './NavBar.vue'

export default {
  name: 'MyVouchers',

  components: {
    NavBar,
    Voucher_Redeemed,
  },

  data: () => ({
    //
  }),
};
</script>