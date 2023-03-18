import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        cart: [
            // {name: 'Something1'},
            // {name: 'Something2'},
            // {name: 'Something3'},
            // {name: 'Something4'}
        ],
        amount: 0
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
        },
        // removeItem: (state,payload) => {
        //     item.find()
        // }
        checkoutCart: state => {
            state.cart.forEach(item => {
                state.amount += item.price
            }) 
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
        checkoutCart: context => {
            context.commit('checkoutCart')
        },

        pointsUpdate({commit}){
            Vue.axios.put('http://127.0.0.1:5003/point/3', {
                total:  commit.checkoutCart
            })
                .then(response => {
                    commit('pointsUpdate', response.data)
                })
                .catch( error => {
                    console.log(error.message);
                });
        }
    },
}
);