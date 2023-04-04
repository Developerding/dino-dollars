<template>

    <v-card class="mx-auto rounded-lg" variant="outlined">

        <v-card-text class="py-0">
            <v-row align="center" gutter>

                <v-col
                cols="2"
                >
                <v-img src="../assets/asos.jpg" width="100" height="100" justify="centre" align="left" class="rounded-xl elevation-5"></v-img>
                </v-col>

                <v-col
                cols="8"
                >
                    <v-list-item three-line>
                        <v-list-item-content>
                            <v-list-item-title class="mb-1 shop" >$5 OFF</v-list-item-title>
                            <v-list-item-title class="body">75 points</v-list-item-title>
                            <v-list-item-subtitle class="body">Expires in 2 hours</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                </v-col>
                
                <v-col
                cols="2"
                >
                <PopUp_ShopNow/>
                </v-col>

            </v-row>
        </v-card-text>

        <br/>
        
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


<style>
.shop {
  font-family: glacial_bold;
  font-size: 25px
}

h3, .body {
  font-family: glacial;
}
</style>