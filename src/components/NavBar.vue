<template>

<v-app-bar app color="white" flat>
    <v-container class="py-0 fill-height">
        <router-link to="/">
            <img src="../assets/dinodollar logo transparent.png" height="50" class="d-flex justify-center align-center">
        </router-link><space></space>

        <!-- <v-btn text>About</v-btn>

        <v-menu offset-y>
            <template v-slot:activator="{ on, attrs }">
                <v-btn color="primary" dark v-bind="attrs" v-on="on" text>Vouchers</v-btn>
            </template>
            
            <v-list>
                <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
                    <v-list-item-title>
                        {{ link.text }}
                    </v-list-item-title>
                </v-list-item>
            </v-list>
        </v-menu> -->

        <v-btn text>About</v-btn>
        <v-btn text>How to earn?</v-btn> 

        <v-menu offset-y v-if="userLoggedIn">
            <template v-slot:activator="{ on, attrs }">
                <v-btn color="primary" dark v-bind="attrs" v-on="on" text>Vouchers</v-btn>
            </template>
            
            <v-list>
                <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
                    <v-list-item-title>
                        {{ link.text }}
                    </v-list-item-title>
                </v-list-item>
            </v-list>
        </v-menu>
         
<!--         
        <v-btn text>How to earn?</v-btn>
  
        <v-spacer></v-spacer> -->
        
        <!-- links for the navbar -->
        <!-- <span v-for="(link,i) in linkss" :key="i">
            <v-btn text router :to="link.route">{{ link.text }}</v-btn>
        </span> -->
        <!--  -->
        <v-spacer></v-spacer>

        <v-btn v-if="userLoggedIn" depressed @click="signUserOut" class="btn white--text" color="green darken-2">Sign Out</v-btn>
        <v-btn v-else depressed :to="{name: 'LoginSignup'}" class="btn white--text" color="green darken-2">Log In</v-btn>


    </v-container>
    </v-app-bar>

    

</template>


<script>
    export default {
      data: () => ({
        links: [
            {text: 'Buy Vouchers', route:'/BuyVouchers'},
            {text: 'My Vouchers', route:'/MyVouchers'},
            {text: 'Redemption History', route:'/RedemptionHistory'},
            // {text: 'Rapie Testing Corner', route:'/AsosUI'},
        ],
      }),

      computed:{
            // linkss(){
            //     let linkitems=[
            //     {text: 'ABOUT', route:'/'},
            //     {text: 'HOW TO EARN?', route:'/'},
            //     ]

            // if(this.userLoggedIn){
            //     linkitems=[
            //     {text: 'ABOUT', route:'/'},
            //     {text:'VOUCHERS', route:'/'},
            //     {text: 'HOW TO EARN?'},
            //     ]

            // }
            // return linkitems
            // },

            userLoggedIn(){
                return this.$store.getters.getUser!=null && this.$store.getters.getUser!=undefined
            }
      },
      methods: {
        signUserOut(){
            this.$store.dispatch('logUserOut')
            this.$router.push('/')
        }
      }
    }
</script>