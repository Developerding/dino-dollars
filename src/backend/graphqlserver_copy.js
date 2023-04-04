// import axios from 'axios'
const axios = require('axios')
const express = require('express')

const {buildSchema} = require('graphql')
const {graphqlHTTP} = require('express-graphql')


const app=express()


const schema=buildSchema(`

    type Item{
        name: String
        price: Int
        url: String
    }

   



    type Query{
        hello: String
        welcomeMessage(name:String): String
        getItem: Item
        getItems: [Item]
    }
`)


const root={
    hello: ()=>{
        return "hello world"
    },

    welcomeMessage: (args)=>{
        return `Hey, ${args.name} how's life`
    },

    getItems: ()=>{
        const parameters={
            method: "GET",
  url: "https://asos2.p.rapidapi.com/products/v2/list",
  params: {
    store: "US",
    offset: "0",
    categoryId: "4209",
    limit: "3",
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

        axios.request(parameters)
        .then( (response)=>{
            // console.log(response.data.products)
            items_list=response.data.products
            items_list=items_list.map(function(item){
                const temp={
                    name:item.name,
                    price:item.price.current.value,
                    url: item.imageUrl
                }

                return temp
            })
            console.log(items_list)
            
            return items_list

        })
        .catch( (err)=>{
            console.log(err)
        })


         
    }
}


//url is http://localhost:5030/graphql
app.use('/graphql', graphqlHTTP({
    graphiql: true,
    schema: schema,
    rootValue: root,

}))



app.listen(5030, ()=>console.log('Express server running on port 5030'))