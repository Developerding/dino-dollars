// import axios from 'axios'


export function callASOS(){
    const axios = require('axios')


//change fields to query different properties from GraphQL, refer to graphqlserver.js
const graphqlurl="http://localhost:5030/graphql"
const graphqlQuery = {
    "operationName": "Query",
    "query": `query Query { items { name price imageUrl } }`
    
};

// let items_list

// const items_list = async()=>{
//     let response= await axios({url: graphqlurl, method:'post', data:graphqlQuery})
//     if (response){
//         response=response.map(function(item){
//             const temp={
//                 name:item.name,
//                 price: item.price,
//                 imageUrl: "http://" + item.imageUrl
//             }
//             return temp
//         }
//     )
//     return response
// }
// }


 axios({url: graphqlurl, method:'post', data:graphqlQuery})
.then((response)=>{
  console.log(response)
  let items_list
  items_list=response.data.data.items
  items_list= items_list.map(function(item){
    const temp={
      name:item.name,
      price: item.price,
      imageUrl: "http://" + item.imageUrl
    }
    return temp
  })
  console.log(items_list)
  return items_list
})
.catch((err)=>{
  console.log(err)
})
}



