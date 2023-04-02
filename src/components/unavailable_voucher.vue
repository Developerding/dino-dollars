<template>
    <v-card class="rounded-lg" outlined>
        <v-list-item three-line>
        <v-list-item-content>
            <v-list-item-title class="text-h5 mb-1" >{{ voucher_obj.DiscountAmt }}% off</v-list-item-title>
            <v-list-item-title>{{ voucher_obj.DDRequired }} points</v-list-item-title>
            <v-list-item-subtitle>{{ voucher_obj.Platform_Name }} voucher</v-list-item-subtitle>
        </v-list-item-content>

        <unavailableButton/>
        
        <!-- <v-btn class="rounded-lg" color="primary" outlined text>Purchase</v-btn> -->
        </v-list-item>
    </v-card>
</template>

<script>
import unavailableButton from './unavailable_voucher_button.vue';

export default {
    props:['voucher_obj']
    
    ,

    components: {
        unavailableButton
    },
    data() {
        return {
            drawer: false
        }
    }
}

</script>