<template>
  <v-card elevation="2" outlined class="pa-4" tile>
    <v-card-title>
      <!-- Needs to be dynamic -->
      {{ ItemName }}
    </v-card-title>

    <v-card-subtitle>
      {{ ItemPrice }}
    </v-card-subtitle>

    <v-btn
      elevation="5"
      large
    >
    Add to cart now!
    </v-btn>

  </v-card>
</template>

<script>
export default {
    name: "ItemCard",
    props: {
      ItemName: String,
      ItemPrice: Number
    }
}
</script>
