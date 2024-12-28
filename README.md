# Converter
# VIDEO TO MP3 CONVERTER


# FLOW DESCRIPTION

# MICROSERVICES WILL BE RUNNING IN A KUBERNETES cluster - cluster's internal network wont be accessible by outside world

client will be making requests fro outside the cluster with the intention of making use of our distributed system deployed within our private kubernetes cluster via our systems gateway.
Our gateway service is the entrypoint to overall application. It is the service that receives requests from clients and communicates with necessarily internal services to fulfill these requests. It is also where we define functionality for overall application. 

How do we determine to use these private clusters?

   Our AUTH service - we use basic authentication.

If user has access - we return a JSON web token to client that client will use for subsequent requests.

JSON web token - 2 json formatted strings  + a signature  - each base64 encoded
   Header - contains signing algorithm and type of token
   PAYLOAD - necessary info (username and whether or not they have access )


ANY SERVER REQUIRES AN IP ADDR TO ALLOW ACCESS FROM OUTSIDE OF THE SERVER

OUR SERVER IS A DOCKER CONTAINER AND THE APP IS RUNNING WITHIN THAT CONTAINER. WHEN WE SPIN UP DOCKER CONTAINER, IT IS GIVEN ITS OWN IP ADDRESS. USING THAT IP ADDRESS, WE CAN SEND REQUESTS TO THAT CONTAINER - which is our server in this case. Tell flask application to listen on container's IP addr, so app can receive these requests. 
