from invokes import invoke_http
from os import environ

user_URL = environ.get('userURL') or input("Enter user service URL: ")  

# invoke book microservice to get all books
results = invoke_http(user_URL, method='GET')

print( type(results) )
print()
print( results )

# invoke book microservice to create a book
uid = '1000'
user_details = { "Name": "test", "Email": "test@gmail.com", "Points": 0 }
create_results = invoke_http(
        user_URL + "/" + uid, method='POST',
        json=user_details
    )

print()
print( create_results )
