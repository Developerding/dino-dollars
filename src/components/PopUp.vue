<template>
    <v-row justify="center">
      <v-btn color="primary" class="rounded-lg" outlined text @click.stop="dialog = true">
        Purchase
      </v-btn>
  
      <v-dialog
        v-model="dialog"
        max-width="290"
      >
        <v-card>
          <v-card-title class="text-h6">
            Purchase this voucher?
          </v-card-title>
  
          <v-card-text>
            <v-btn>
                
            </v-btn>
          </v-card-text>
  
          <v-card-actions>
            <v-spacer></v-spacer>
  
            <v-btn
              color="green darken-1"
              text
              @click="dialog = false"
            >
              Disagree
            </v-btn>
  
            <v-btn
              color="green darken-1"
              text
              @click="dialog = false"
            >
              Agree
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
</template>

<script>
export default {
  data () {
    return {
      dialog: false,
    }
  },
}
</script>