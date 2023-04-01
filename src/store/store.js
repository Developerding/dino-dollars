import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        cart: [
        ],
        amount: 0,

        user: null
    },
    getters: {
        // somethingChanged: state => {
        //     var somethingChange = state.cart.map( something => {
        //         return {
        //           name: '**' + something.name + "**"
        //         }
        //       });
        
        //       return somethingChange
        // }
        cartTotal: state => {
            state.cart.forEach(item => {
                state.amount += item.price
            })

            return state.amount
        },

        //returning the vuex user state, can be seen in the console log.
        getUser(state){
            console.log(state.user)
            return state.user
        } 
    },
    mutations: {
        // changeName: state => {
        //     state.cart.forEach(something => {
        //         something.name = something.name + "&&&"
        //     })
        // },
        addItemToCart: (state,payload) => {
            state.cart.push({name: payload.ItemName, price:payload.ItemPrice})
        },
        removeAllItems: state => {
            state.cart = []
            state.amount = 0
        },
        // removeItem: (state,payload) => {
        //     item.find()
        // }
        // checkoutCart: state => {
        //     state.cart.forEach(item => {
        //         state.amount += item.price
        //     })
        // }
        logUser (state, payload){
            state.user=payload
        },

        logOut (state){
            state.user=null
        }

        
    },
    actions: {
        // changeName: context => {
        //     setTimeout(function(){
        //         context.commit('changeName')
        //     }, 2000)
        // },
        addItemToCart: (context,payload) => {
            context.commit('addItemToCart', payload)
        },
        removeAllItems: context => {
            context.commit('removeAllItems')
        },
        // removeItem: (context,payload) => {
        //     context.commit('removeItem',payload)
        // }
        // checkoutCart: context => {
        //     context.commit('checkoutCart')
        // },

        pointsUpdate: (context) => {
            axios.put('http://127.0.0.1:5003/point/1', {
                Points:  context.state.amount
            })
            .then(response => {
                console.log(response.data)
            })
            .catch( error => {
                console.log(error.message);
            });
        },
        paypalTest: () => {
            let data = {
                "intent": "CAPTURE",
                "purchase_units": [
                    {
                        "amount": {
                            "currency_code": "USD",
                            "value": "100"
                        }
                    }
                ]
            } 

            let config = {
                headers: {
                    "Content-Type": "application/json",
                    "Prefer": "return=representation",
                    "Authorization": "Bearer A21AAKC4Zz9p1F_noCLaWiAivHj7HowA8Z3D-FwHi-ae0dZuJU0RqMZItgP_uuyW2eI6fkGKXECNuQ9yGdQwB8UnTm2AMqwdA"
                }
              }

            axios.post('https://api-m.sandbox.paypal.com/v2/checkout/orders', 
                data, config
            )
            .then(response => {
                console.log(response)
            })
            .catch(error => {
                console.log(error)
            })
        },

        signUserIn( {commit}, payload){
            let email=payload.email
            let password=payload.password
            let url="http://127.0.0.1:5003/user/"+ email+'/'+password 
            return axios.get(url, payload)
            .then(response => {
                //if user logs in
                console.log(response.data)
                const loggedUser= response.data.data
                commit('logUser',loggedUser)

            })
            .catch( error => {
                // if user fails to log in
                // console.log(error)
                console.log(error.response.data);
                return error.response.data

            });
         
        },

        logUserOut( {commit}){
            commit('logOut')
        }
    },
}
);