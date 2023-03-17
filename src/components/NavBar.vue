<template>

<v-app-bar app color="white" flat>
    <v-container class="py-0 fill-height">
        <router-link to="/">
            <v-avatar class="mr-10" color="grey darken-1" size="60" tile><img src="../assets/dinodollar logo.jpg"></v-avatar>
        </router-link>

        <v-btn text>About</v-btn>

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
        </v-menu>

        
        
        <v-btn text>How to earn?</v-btn>
  
        <v-spacer></v-spacer>

        <v-btn depressed rounded :to="{name: 'LoginSignup'}">Log In</v-btn>

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
            {text: 'Rapie Testing Corner', route:'/AsosUI'},
        ],
      }),
    }
</script>