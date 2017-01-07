#####
#   # 
#####

curl http://localhost:8000/v1/contact | python -m json.tool

O/P:
===
 % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   229  100   229    0     0  11091      0 --:--:-- --:--:-- --:--:-- 11450
[
    {
        "contactId": 1,
        "email": "sudip.khadka@domain.com",
        "firstName": "Sudip",
        "lastName": "Khadka",
        "phone": "901-543-8907"
    },
    {
        "contactId": 2,
        "email": "parash.panadi@domain.com",
        "firstName": "Parash",
        "lastName": "Panadi",
        "phone": "901-246-8618"
    }
]
===
To get a particular record
curl http://localhost:8000/v1/contact/1 | python -m json.tool
O/P:
===
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   112  100   112    0     0   4120      0 --:--:-- --:--:-- --:--:--  4307
{
    "contactId": 1,
    "email": "sudip.khadka@domain.com",
    "firstName": "Sudip",
    "lastName": "Khadka",
    "phone": "901-543-8907"
}

===
We can send some data using post
curl -i -X POST -H 'Content-Type:application/json' http://localhost:3000/v1/contact -d '{"firstName":"Kul", "lastName":"Subedi","email":"subedi.kulprasad@gmail.com","phone":"901-833-3271"}'

O/P:
===
curl -i -X POST -H 'Content-Type:application/json' http://localhost:8000/v1/contact -d '{"firstName":"Kul", "lastName":"Subedi","email":"subedi.kulprasad@gmail.com","phone":"901-833-3271"}'
HTTP/1.1 201 Created
X-Powered-By: Express
Content-Type: application/json; charset=utf-8
Content-Length: 30
ETag: W/"1e-+1sCBWzQwwTTtXpoa4pAVw"
Date: Fri, 06 Jan 2017 18:22:50 GMT
Connection: keep-alive

{"message":"Record appended!"}


===
We can PUT some data

$curl http://localhost:8000/v1/contact/1 | python -m json.tool
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   113  100   113    0     0   8740      0 --:--:-- --:--:-- --:--:--  9416
{
    "contactId": 1,
    "email": "subedi.kulprasad@gmail.com",
    "firstName": "Kul",
    "lastName": "Subedi",
    "phone": "901-833-5454"
}


$curl -i -X PUT -H 'Content-Type:application/json' http://localhost:8000/v1/contact/1 -d '{"contactId":1, "firstName":"Kul", "lastName":"Subedi","email":"subedi.kulprasad@gmail.com","phone":"901-833-5000"}'
HTTP/1.1 201 Created
X-Powered-By: Express
Content-Type: application/json; charset=utf-8
Content-Length: 27
ETag: W/"1b-Ul/V1Xr9yFCk+NgL3hEkMw"
Date: Fri, 06 Jan 2017 18:29:44 GMT
Connection: keep-alive

{"message":"Record saved!"}

$curl http://localhost:8000/v1/contact/1 | python -m json.tool  

% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   113  100   113    0     0   5592      0 --:--:-- --:--:-- --:--:--  5947
{
    "contactId": 1,
    "email": "subedi.kulprasad@gmail.com",
    "firstName": "Kul",
    "lastName": "Subedi",
    "phone": "901-833-5000"
}

===
We can use DELETE 

$ curl -i -X DELETE http://localhost:8000/v1/contact/1 

HTTP/1.1 204 No Content
X-Powered-By: Express
ETag: W/"1d-VtfDn6w0sLEUfRItmbdUwA"
Date: Fri, 06 Jan 2017 18:33:16 GMT
Connection: keep-alive

$ curl -i -X DELETE http://localhost:8000/v1/contact/1 

HTTP/1.1 404 Not Found
X-Powered-By: Express
Content-Type: text/html; charset=utf-8
Content-Length: 24
ETag: W/"18-Q5tydbjbTHu2yhJ6il7GbQ"
Date: Fri, 06 Jan 2017 18:33:21 GMT
Connection: keep-alive

Record does not exist!!!

$ curl -i -X GET http://localhost:8000/v1/contact/1 
HTTP/1.1 404 Not Found
X-Powered-By: Express
Content-Type: text/html; charset=utf-8
Content-Length: 24
ETag: W/"18-Q5tydbjbTHu2yhJ6il7GbQ"
Date: Fri, 06 Jan 2017 18:36:29 GMT
Connection: keep-alive

Record does not exist!!!

===
$ curl -v -i  http://localhost:8000/v1/contact/1 
*   Trying 127.0.0.1...
* Connected to localhost (127.0.0.1) port 8000 (#0)
> GET /v1/contact/1 HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.47.0
> Accept: */*
> 
< HTTP/1.1 404 Not Found
HTTP/1.1 404 Not Found
< X-Powered-By: Express
X-Powered-By: Express
< Content-Type: text/html; charset=utf-8
Content-Type: text/html; charset=utf-8
< Content-Length: 24
Content-Length: 24
< ETag: W/"18-Q5tydbjbTHu2yhJ6il7GbQ"
ETag: W/"18-Q5tydbjbTHu2yhJ6il7GbQ"
< Date: Fri, 06 Jan 2017 19:04:59 GMT
Date: Fri, 06 Jan 2017 19:04:59 GMT
< Connection: keep-alive
Connection: keep-alive

< 
* Connection #0 to host localhost left intact
Record does not exist!!!
===
