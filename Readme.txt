# goodbits-finance-test
Goodbits interview round 2 

Working

1. Takes the input form with the following inputs, 
  a.	Invoice Number:Alphanumeric ID  
  b.	Client name 
  c.	Client email ID 
  d.	Project Name 
  e.	Amount to be charged 
  these details are stored in the database

 2. An url is gernerted using stripe paymentIntent and is send to the email inputed.
 
 
 Validations
 
 1. email field will be unique
 2. Alphanumeric check is done on invoice number


---------Front end source code is included as a zip file--------------
node version - v16.13.1

 Postman documentation
 published link - https://documenter.getpostman.com/view/15623430/UVXbvLT1

 end-point - http://localhost:8000/invoice/