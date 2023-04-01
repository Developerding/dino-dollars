import {store} from 'store.js'
export default(to,from,next)=>{
    if(store.getters.getuser){
        next()
    }
    else{
        next('/LoginSignup')
    }
}