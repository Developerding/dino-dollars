import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        cart: [
            {name: 'Something1'},
            {name: 'Something2'},
            {name: 'Something3'},
            {name: 'Something4'}
        ]
    },
    getters: {
        somethingChanged: state => {
            var somethingChange = state.cart.map( something => {
                return {
                  name: '**' + something.name + "**"
                }
              });
        
              return somethingChange
        }
    },
    mutations: {
        changeName: state => {
            state.cart.forEach(something => {
                something.name = something.name + "&&&"
            })
        }
    },
    actions: {
        changeName: context => {
            setTimeout(function(){
                context.commit('changeName')
            }, 2000)
        }
    }
})