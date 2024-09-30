# What are APIs? How are they used and why are they so popular?
 * API(Application Programming Interface)  `is a set of rules and protocols that allows different software applications to communicate with each other.`


 * Why are APIs popular ? 
   * `They allow for modularity: Developers can reuse services and integrate different applications.`
   * `They enhance collaboration between services and systems.`
   * `APIs power cloud computing and enable mobile and web apps to connect to databases, servers, or third-party services.`

# Create a diagram to showcase the data transfer process in API communication.
![api data transfer.png](..%2F..%2Fimages%2Fapi%20data%20transfer.png)

# What is a REST API? What makes an API RESTful? What are the REST guidelines?

* REST (Representational State Transfer) API `is a software arhitecture that imposes on how an APi should work.  It uses HTTP methods for communication and treats each resource as a unique URL.`

* What makes an API RESTful?
   * _**Stateless**_: `Each request from the client to the server must contain all the information the server needs  to process the request. The server doesn't store client state between requests.Each request is separate and unconnected, and no client information is stored between requests.`
   * **_Uniform Interface_**: `The API uses standard HTTP methods and URLs to represent resources.`
   * **_Client-Server Architecture_**:` Separation of concerns between client and server.`
   * **_Cacheable_**: `Responses must be explicitly marked as cacheable or non-cacheable.`
   * **_Layered System_**:` The client doesn’t need to know whether it’s communicating with the actual server or an intermediary.`


# What is HTTP? (what does it stand for and what is it used for? What is HTTPS?)

* HTTP (HyperText Transfer Protocol): `The protocol used for transmitting data between the client (browser) and the server. It allows fetching resources like HTML pages.`
* HTTPS (HyperText Transfer Protocol Secure): `An extension of HTTP that includes encryption (via SSL/TLS) to secure the communication between client and server.`


# Explain HTTP request structure using the diagrams provided, or your own.

* Request Line:` Includes the HTTP method (GET, POST, etc.), the URL, and the HTTP version`
* Headers:` Metadata about the request, such as Content-Type, Authorization, etc.`
* Body (optional):` The data sent with the request (used in POST, PUT, PATCH).`

![HTTP request.png](..%2F..%2Fimages%2FHTTP%20request.png)



# Explain HTTP response structure using the diagram provided, or your own.

* Status Line: `Includes the HTTP version, status code (e.g., 200 for OK), and status message.`
* Headers: `Information about the response, such as Content-Type, Content-Length.`
* Body: `The actual data returned from the server (e.g., HTML, JSON).`

![HTTP response.png](..%2F..%2Fimages%2FHTTP%20response.png)




# What are the 5 HTTP verbs and what do they do?

## GET →  Requests data from a specified resource(Retrieve information from the server ) .
        Example: Retrieve a list of users.
                http
                GET /users

## POST → Sends data to create a new resource on the server(create a new resource like adding a new user).
        Example: Create a new user.
        http
        POST /users
        Body: {"name": "John", "age": 30}

## PUT → Updates an existing resource with the provided data(like replacing old user data with new).
        Example: Update user information.
        http
        PUT /users/1
        Body: {"name": "John", "age": 31}

## PATCH →  Partially updates an existing resource(only changing part of the data).
        Example: Update only the user’s age.
        http
        PATCH /users/1
        Body: {"age": 31}

## DELETE → Deletes a specified resource.
        Example: Delete a user.
        http
        DELETE /users/1


## What is statelessness? Show examples of “stateless” and stateful http requests.

* Stateless system `each request from a client must contain all the information needed to process it. The server doesn't keep track of previous interactions.`
* Example of Stateless: `When you make a request to an API, the server processes it without remembering previous requests.`
![statelessness.png](..%2F..%2Fimages%2Fstatelessness.png)

* Stateful: `The server keeps track of previous interactions, often using sessions or cookies.`
* Example of Stateful: `When a server remembers your shopping cart in an e-commerce site.`

# What is caching?
* Caching ` is the process of storing copies of data in a temporary storage location (cache) so that future requests for that data can be served faster.`

* Caching is often used in APIs to avoid repeated processing of identical requests, reducing load on the server and improving performance.