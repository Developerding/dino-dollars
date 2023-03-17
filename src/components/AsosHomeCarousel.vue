<template>
    <!-- <v-carousel cycle height="400" hide-delimiter-background hide-delimiters show-arrows-on-hover>
        <v-carousel-item
        v-for="(slide, i) in slides"
        :key="i"
        >
        <v-sheet
            height="100%"
            class="brown lighten-2"
        >
        
        <v-container>
            <v-row>
                <v-col cols="12">
                <v-card color="#385F73" dark>
                    <v-card-title class="text-h5">Winter-Fall Collection 2023</v-card-title>

                    <v-card-subtitle>Shop Dino Dollars new Collection for the slayest looks of the year!</v-card-subtitle>

                    <v-card-actions>
                        <v-btn text>Shop Now</v-btn>
                    </v-card-actions>
                </v-card>
                </v-col>

                <v-col v-for="(item, i) in items" :key="i" cols="12">
                <v-card :color="item.color" dark>
                    <div class="d-flex flex-no-wrap justify-space-between">
                    <div>
                        <v-card-title class="text-h5" v-text="item.title"></v-card-title>

                        <v-card-subtitle v-text="item.artist"></v-card-subtitle>

                        <v-card-actions>
                        <v-btn v-if="item.artist === 'Ellie Goulding'" class="ml-2 mt-3" fab icon height="40px" right width="40px">
                            <v-icon>mdi-play</v-icon>
                        </v-btn>

                        <v-btn v-else class="ml-2 mt-5" outlined rounded small>
                            START RADIO
                        </v-btn>
                        </v-card-actions>
                    </div>

                    <v-avatar
                        class="ma-3"
                        size="125"
                        tile
                    >
                        <v-img :src="item.src"></v-img>
                    </v-avatar>
                    </div>
                </v-card>
                </v-col>
            </v-row>
            </v-container>

        </v-sheet>
        </v-carousel-item>
    </v-carousel> -->
    <v-app id="inspire">
        <v-div align="center" justify="center">
            <!-- <h2 class="font-weight-medium">Earn Dino Dollars with our Partners!</h2><br> -->
            <v-carousel cycle height="500" hide-delimiter-background hide-delimiters show-arrows-on-hover>
                <v-carousel-item>
                        <v-card color="#385F73" dark>
                            <v-row class="fill-height" align="center" justify="center">
                                <v-col cols="6" class="pl-20">
                                    <v-card-title class="text-h5">Winter-Fall Collection 2023</v-card-title>
                                    <v-card-subtitle class="text-h7">Shop Dino Dollars new Collection for the slayest looks of the year!</v-card-subtitle>
                                    <v-card-actions>
                                        <v-btn text>Shop Now</v-btn>
                                    </v-card-actions>
                                </v-col>
                                <v-col cols="6">
                                    <v-img width = "800" height="500" src="https://cdn.vuetifyjs.com/images/cards/cooking.png"></v-img>
                                </v-col>
                            </v-row>
                        </v-card>
                </v-carousel-item>
                <v-carousel-item>
                        <v-card color="#385F73" dark>
                            <v-row>
                                <v-col cols="6">
                                    <v-card-title class="text-h5">Winter-Fall Collection 2023</v-card-title>
                                    <v-card-subtitle class="text-h7">Shop Dino Dollars new Collection for the slayest looks of the year!</v-card-subtitle>
                                    <v-card-actions>
                                        <v-btn text>Shop Now</v-btn>
                                    </v-card-actions>
                                </v-col>
                                <v-col cols="6">
                                    <v-img width = "800" height="500" src="https://cdn.vuetifyjs.com/images/carousel/sky.jpg"></v-img>
                                </v-col>
                            </v-row>
                        </v-card>
                </v-carousel-item>
            </v-carousel>
            <!-- <v-carousel hide-delimiters v-model="model" width="vw" height="320" align="center">
            <v-carousel-item reverse-transition="fade-transition" transition="fade-transition">
                <router-link to="/AsosVouchers">
                <v-img src="../assets/asos.jpg" width="100%" height="300" justify="center" align="center" class="rounded-xl elevation-5"></v-img>
                </router-link>

            </v-carousel-item>

            <v-carousel-item reverse-transition="fade-transition" transition="fade-transition" align-center justify>
                <v-img src="../assets/adidas.jpg" width="100%" height="300" justify="center" align="center" class="rounded-xl elevation-5"></v-img>
            </v-carousel-item>
            <v-carousel-item reverse-transition="fade-transition" transition="fade-transition" align-center justify>
                <v-img src="../assets/nike.jpg" width="100%" height="300" justify="center" align="center" class="rounded-xl elevation-5"></v-img>
            </v-carousel-item>
            <v-carousel-item reverse-transition="fade-transition" transition="fade-transition" align-center justify>
                <v-img src="../assets/apple.jpg" width="100%" height="300" justify="center" align="center" class="rounded-xl elevation-5"></v-img>
            </v-carousel-item>
            <v-carousel-item reverse-transition="fade-transition" transition="fade-transition" align-center justify>
                <v-img src="../assets/puma.jpg" width="100%" height="300" justify="center" align="center" class="rounded-xl elevation-5"></v-img>
            </v-carousel-item>
            </v-carousel> -->
        </v-div>
    </v-app>
</template>

<script>
    export default {
        data () {
        return {
            slides: [
            'First',
            'Second',
            'Third',
            'Fourth',
            'Fifth',
            ],
            items: [
                {
                color: '#1F7087',
                src: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
                title: 'Supermodel',
                artist: 'Foster the People',
                },
                {
                color: '#952175',
                src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
                title: 'Halcyon Days',
                artist: 'Ellie Goulding',
                },
            ],
        }
        },
    }
</script>