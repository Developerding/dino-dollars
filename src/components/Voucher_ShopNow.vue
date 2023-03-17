<template>

    <v-card class="mx-auto rounded-lg" outlined>

        <v-list-item three-line>
        <v-list-item-content>
            <v-list-item-title class="text-h5 mb-1" >$5 OFF</v-list-item-title>
            <v-list-item-title>75 points</v-list-item-title>
            <v-list-item-subtitle>Expires in 2 hours</v-list-item-subtitle>
        </v-list-item-content>

        <PopUp_ShopNow/>
        
        <!-- <v-btn class="rounded-lg" color="primary" outlined text>Shop Now!</v-btn> -->
        </v-list-item>
    </v-card>
</template>

<script>
import PopUp_ShopNow from './PopUp_ShopNow.vue';

export default {
    components: {
        PopUp_ShopNow 
    },
    data() {
        return {
            drawer: false
        }
    }
}

</script>