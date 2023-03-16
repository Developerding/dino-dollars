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
                    <VoucherCoupon/><br>
                    <VoucherCoupon/><br>
                    <VoucherCoupon/>
                </v-div>
            </v-col>
            </v-row>
            </v-container>
            

        </v-main>
    </v-app>

</template>

<script>
import VoucherCoupon from './VoucherCoupon.vue'

export default {
  name: 'AsosVouchers',

  components: {
    VoucherCoupon
  },

  data: () => ({
    //
  }),
};
</script>