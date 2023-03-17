<template>



<v-col cols="12">
          <v-card
            color="#1F7087"
            theme="dark"
          >
            <div class="d-flex flex-no-wrap justify-space-between">
              <div>
                <v-card-title class="text-h5">
                  Supermodel
                </v-card-title>

                <v-card-subtitle>Foster the People</v-card-subtitle>

                <v-card-actions>
                  <v-btn
                    class="ms-2"
                    variant="outlined"
                    size="small"
                  >
                    START RADIO
                  </v-btn>
                </v-card-actions>
              </div>

              <v-avatar
                class="ma-3"
                size="125"
                rounded="0"
              >
                <v-img src="https://cdn.vuetifyjs.com/images/cards/foster.jpg"></v-img>
              </v-avatar>
            </div>
          </v-card>
        </v-col>






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