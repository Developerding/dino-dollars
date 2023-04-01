<template>
  <v-app id="inspire">
    <v-content>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="8">
            <v-card class="elevation-12">
              <v-window v-model="step">
                <v-window-item :value="1">
                  <v-row>
                    <v-col cols="12" md="8">
                      <v-card-text class="mt-12">

                      <!-- Error tag -->

                        <div v-if="error">
                            <v-alert
                                type="error"
                              
                              >
                              {{ error }}
                              </v-alert>
                      </div>


                        <h1
                          class="text-center display-2 green--text text--darken-2"
                        >Log in to Dino Dollars!</h1>

                        
                        <v-form>
                          <v-text-field v-model="email"
                            label="Email"
                            name="Email"
                            type="email"
                            color="teal accent-3"
                          />

                          <v-text-field v-model="password"
                            id="password"
                            label="Password"
                            name="password"
                            
                            type="password"
                            color="teal accent-3"
                          />
                        </v-form>
                        <h3 class="text-center mt-4">Forgot your password?</h3>
                      </v-card-text>

                     

                      <div class="text-center mt-3">
                        <v-btn class="btn" rounded color="green darken-2" type="submit" :disabled="!signInValid" @click="logIn" >SIGN IN</v-btn>

                      </div>
                    </v-col>
                    <v-col cols="12" md="4" class="green darken-2">
                      <v-card-text class="white--text mt-12">
                        <h1 class="text-center display-1">Hello there!</h1>
                        <h5
                          class="text-center"
                        >Enter your details and start your journey with us!</h5>
                      </v-card-text>
                      <div class="text-center">
                        <v-btn rounded outlined dark  @click="stepper">SIGN UP</v-btn>
                      </div>
                    </v-col>
                  </v-row>
                </v-window-item>
                <v-window-item :value="2">
                  <v-row class="fill-height">
                    <v-col cols="12" md="4" class="green darken-2">
                      <v-card-text class="white--text mt-12">
                        <h1 class="text-center display-1">Welcome Back!</h1>
                        <h5
                          class="text-center"
                        >If you already have an account, log in here.</h5>
                      </v-card-text>
                      <div class="text-center">

                        <!-- reduce step -->
                        <v-btn rounded outlined dark @click="stepper">Sign in</v-btn>
                      </div>
                    </v-col>

                    <v-col cols="12" md="8">
                      <v-card-text class="mt-12">

                        <!-- alert -->

                        <div v-if="error">
                            <v-alert
                                type="error"
                              
                              >
                              {{ error }}
                              </v-alert>
                      </div>


                        <h1 class="text-center display-2 green--text text--darken-2">Create Account</h1>
                        
                        <h4 class="text-center mt-4">Ensure your email for registration</h4>
                        <v-form>
                          <v-text-field v-model="name"
                            label="Name"
                            name="Name"
                            type="text"
                            color="teal accent-3"
                          />
                          <v-text-field v-model="email"
                            label="Email"
                            name="Email"
                            type="text"
                            color="teal accent-3"
                          />

                          <v-text-field v-model="password"
                            id="password"
                            label="Password"
                            name="password"
                            type="password"
                            color="teal accent-3"
                          />
                        </v-form>
                      </v-card-text>
                      <div class="text-center mt-n5">
                        <v-btn rounded color="green-darken-2" :disabled="!signUpValid" @click="signUp">SIGN UP</v-btn>
                      </div>
                    </v-col>
                  </v-row>
                </v-window-item>
              </v-window>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import axios from 'axios';

export default {
  data: () => ({
    step: 1,
    name:'',
    email:'',
    password:'',

    error:false,
  }),

  computed:{
    signInValid(){
      return this.email!='' && this.password!='' 
    },

    signUpValid(){
      return this.email!='' && this.password!=''&& this.name!='' 
    },
    user(){
      return this.$store.getters.getUser
    }
  },

  watch:{
    user(value){
      if(value!=null && value!=undefined){
        this.$router.push('/')
      }
    }
  },

  methods:{

    stepper(){
      this.error=false
      if(this.step==2){
        this.step=1
      }
      else{
        this.step=2
      }
    },

    logIn(){
      this.error=false
      let payload={
        'email':this.email,
        'password':this.password
      }
      this.$store.dispatch("signUserIn", payload)
      .then( (res)=>{
        if(res.status!=='success'){
          console.log(res)
        this.error=res.message
        }
      })
    //   catch((err)=>{
    //     console.log(err)
    //     this.error=err.message
    //   })
      
    },


    signUp(){
      this.error=false
      let payload={
        'Name':this.name,
        'Email':this.email,
        'Password':this.password
      }

      // committing to signup action:
      let url="http://127.0.0.1:5003/user"
      axios.post(url, payload)
      .then((response)=>{
        console.log(response)
        this.$router.push('/LoginSignup')
      })
      .catch( (err)=>{
        console.log(err)
        this.error=err.response.data.message
      })
    }
  },

  props: {
    source: String
  }
};
</script>





