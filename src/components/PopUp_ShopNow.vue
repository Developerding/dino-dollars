<template>
    <v-row justify="center">
      <v-btn color="primary" class="rounded-lg" outlined text @click.stop="dialog = true">
        Shop Now
      </v-btn>
  
      <v-dialog v-model="dialog" max-width="290">
        <v-card class="px-5 pt-5 pb-5 mx-auto text-center d-inline-block" variant="outlined">
          <v-card-title class="text-h5 text-center" style="word-break: break-word">
            Leave site to shop at ASOS?
          </v-card-title>
  
          <v-card-actions class="d-flex align-center justify-center">
            <v-btn color="grey lighten-3" class="ma-1" @click="dialog = false">
              Cancel</v-btn>
  
            <v-btn color="blue lighten-2" class="ma-1" light @click="dialog = true" router to="/AsosWebsite"> 
              Yes</v-btn>
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

