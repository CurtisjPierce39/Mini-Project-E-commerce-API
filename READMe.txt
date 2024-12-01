Welcome to the E-Commerce-Database!!

In order to accurately use the system you must use Postman wWorkspace in order to interface with the system.

1. Customer and CustomerAccount Management: Here you are able to use the CRUD routes(Create, Read, Update and Delete) Customers and Customer Accounts.

Create Customer: Open the Postman App, type in HTTP address "example, http://127.0.0.1:5000/customers" for database. Click on "Headers" and add a key of "Content-Type" and a value of "application/json". Than in the "Body" and click on "raw". Than input specified column data in between curly braces {}. Set the request type tp "POST" and click "Send".

Read Customer: Open the Postman App, type in HTTP address for database "example, http://127.0.0.1:5000/customers". Set the request type to "GET" and click "Send".

Update Customer: Open the Postman App, type in HTTP address with specified data indicator "example, http://127.0.0.1:5000/customers/5" for database. Click on "Headers" and add a key of "Content-Type" and a value of "application/json". Than in the "Body" and click on "raw". Than input specified column data in between curly braces {}. Set the request type to "PUT" and click "Send".

Delete Customer: Open the Postman App, type in HTTP address with specified data indicator "example, http://127.0.0.1:5000/customers/5" for database. Set the request type to "DELETE" and click "Send".

Create CustomerAccount: Open the Postman App, type in HTTP address with specified data indicator "example, http://127.0.0.1:5000/customers/5" for database. Click on "Headers" and add a key of "Content-Type" and a value of "application/json". Than in the "Body" and click on "raw". Than input specified column data in between curly braces {}. Set the request type to "POST" and click "Send".

Read CustomerAccount: Open the Postman App, type in HTTP address for database. Set the request type to "GET" and click "Send".

Update CustomerAccount: Open the Postman App, type in HTTP address with specified data indicator "example, http://127.0.0.1:5000/customer_accounts/1" for database. Click on "Headers" and add a key of "Content-Type" and a value of "application/json". Than in the "Body" and click on "raw". Than input specified column data in between curly braces {}. Set the request type to "PUT" and click "Send".

Delete CustomerAccount: Open the Postman App, type in HTTP address with specified data indicator "example, http://127.0.0.1:5000/customer_accounts/1" for database. Set the request type to "DELETE" and click "Send".

2. Product Catalog: Here you are able to use the CRUD routes(Create, Read, Update and Delete) to manage products in the system.

Create Product: Open the Postman App, type in HTTP address "example, http://127.0.0.1:5000/products" for database. Click on "Headers" and add a key of "Content-Type" and a value of "application/json". Than in the "Body" and click on "raw". Than input specified column data in between curly braces {}. Set the request type to "POST" and click "Send".

Read Product: Open the Postman App, type in HTTP address with specified data indicator "example, http://127.0.0.1:5000/products/1" for database. Set the request type to "GET" and click "Send".

Update Product: Open the Postman App, type in HTTP address with specified data indicator "example, http://127.0.0.1:5000/products/1" for database. Click on "Headers" and add a key of "Content-Type" and a value of "application/json". Than in the "Body" and click on "raw". Than input specified column data in between curly braces {}. Set the request type to "PUT" and click "Send".

Delete Product: Open the Postman App, type in HTTP address with specified data indicator "example, http://127.0.0.1:5000/products/1" for database. Set the request type to "DELETE" and click "Send".

List Products:Open the Postman App, type in HTTP address for database "example, http://127.0.0.1:5000/products". Set the request type to "GET" and click "Send".

3. Order Processing:

Place Order: Open the Postman App, type in HTTP address for database. Click on "Headers" and add a key of "Content-Type" and a value of "application/json". Than in the "Body" and click on "raw". Than input specified column data in between curly braces {}. Set the request type tp "POST" and click "Send".

Retrieve Order: Open the Postman App, type in HTTP address with specified data indicator "example, http://127.0.0.1:5000/orders/1" for database. Set the request type to "GET" and click "Send".

