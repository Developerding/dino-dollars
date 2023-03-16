<template>
  <v-app>
    <div>
        <ol>
            <li v-for="item in items" :key="item.id">
                {{ item.name }}
                {{ item.price.current.value }}
                <!-- <img :src="getImage(item.imageUrl)" alt=""> -->
                <!-- <v-img :src="getImage(item.imageUrl)"></v-img> -->
                <!-- <v-img :src=require(`${item.imageUrl}`)></v-img> -->
                <!-- <v-img :src=item.imageUrl></v-img> -->
            </li>
        </ol>
    </div>
  </v-app>
</template>

<script>
import axios from "axios";

const options = {
  method: "GET",
  url: "https://asos2.p.rapidapi.com/products/v2/list",
  params: {
    store: "US",
    offset: "0",
    categoryId: "4209",
    limit: "48",
    country: "US",
    sort: "freshness",
    currency: "USD",
    sizeSchema: "US",
    lang: "en-US",
  },
  headers: {
    "X-RapidAPI-Key": "e2131ac1c7mshf037e692363d1d8p1e89cajsn50d1e5e1a4e6",
    "X-RapidAPI-Host": "asos2.p.rapidapi.com",
  },
};



export default {
  name: "Axios-test",
  data() {
    return {
        items: []
    };
  },
  mounted() {
    axios
    .request(options)
    .then((response) => {
        console.log(response.data.products)
        this.items = response.data.products;
    })
    .catch((error) => {
        console.log(error)
    })
  },
  methods: {
    getImage(img){
        return `${img}`;
    }
  }
};
</script>
