<template>
    <v-card class="mx-auto rounded-lg" variant="outlined">
    
        <v-card-text class="py-0">
            <v-row align="center" gutter>


        <v-overlay
          :absolute="absolute"
          :value="overlay"
        >
          <v-btn
            color="success"
            @click="overlay = false"
          >
            Hide Overlay
          </v-btn>
        </v-overlay>

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
                            <v-list-item-title class="text-h5 mb-1" >$5 OFF</v-list-item-title>
                            <v-list-item-title>75 points</v-list-item-title>
                            <v-list-item-subtitle>Expires in 2 hours</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
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