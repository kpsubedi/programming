curl -i -X POST -H 'Content-Type:application/json' http://localhost:3000/v1/contact -d '{"firstName":"Kul", "lastName":"Subedi","email":"subedi.kulprasad@gmail.com","phone":"901-833-3271"}'


curl -i -X PUT -H 'Content-Type:application/json' http://localhost:3000/v1/contact/1 -d '{"contactId":1, "firstName":"Kul", "lastName":"Subedi","email":"subedi.kulprasad@gmail.com","phone":"901-833-5400"}'
