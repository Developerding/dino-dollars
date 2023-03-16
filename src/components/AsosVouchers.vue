<template>
    <v-app id="inspire">
        <v-main class="blue lighten-4">
            <v-container align="center">
               
            <v-row>
                <v-col>
                <v-card>
                    asos
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

export default {
  name: 'AsosVouchers',

  components: {
    Voucher_Purchase
  },

  data: () => ({
    //
  }),
};
</script>