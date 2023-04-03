<template>

    <v-card class="mx-auto rounded-lg" variant="outlined" color="blue-grey">
    
        <v-card-text class="py-0">
            <v-row align="center" gutter>

                <v-col
                cols="2"
                >
                <router-link to="/AsosVouchers">
                <v-img src="../assets/asos.jpg" width="100" height="100" justify="centre" align="left" class="rounded-xl elevation-5"></v-img>
                </router-link>
                </v-col>

                <v-col
                cols="7"
                >
                    <v-list-item three-line>
                        <v-list-item-content>
                            <v-list-item-title class="text-h5 mb-1" >$5 OFF</v-list-item-title>
                            <v-list-item-title>75 points</v-list-item-title>
                            <v-list-item-subtitle>Expires in 2 hours</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                </v-col>

                <v-col
                cols="3"
                >
                    <h1>REDEEMED</h1>
                </v-col>
                
            </v-row>
        </v-card-text>

    <br/>
    </v-card>

    
</template>


<script>

export default {
    components: {
        
    },
    data() {
        return {
            drawer: false
        }
    }
}

</script>