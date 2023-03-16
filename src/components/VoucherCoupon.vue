<template>
    <v-card class="mx-auto rounded-lg" outlined>
        <v-list-item three-line>
        <v-list-item-content>
            <v-list-item-title class="text-h5 mb-1" >$5 OFF</v-list-item-title>
            <v-list-item-title>75 points</v-list-item-title>
            <v-list-item-subtitle>Expires in 2 hours</v-list-item-subtitle>
        </v-list-item-content>

        <PopUp/>
        
        <!-- <v-btn class="rounded-lg" color="primary" outlined text>Purchase</v-btn> -->
        </v-list-item>
    </v-card>
</template>

<script>
import PopUp from './PopUp.vue';

export default {
    components: {
        PopUp 
    },
    data() {
        return {
            drawer: false
        }
    }
}

</script>