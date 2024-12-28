import jwt, datetime, os
from flask import Flask, request
from flask_mysqldb import MySQL

server = Flask(__name__)
mysql = MySQL(server)

server.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
server.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
server.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
server.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
server.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT")

# request has an attribute that 
@server.route("/login", methods=["POST"])
def login():
   auth = request.authorization()

   if not auth:
      return "Credentials are missing!", 401

   cur = mysql.connection.cursor()
   result = cur.execute(
      "SELECT email, password FROM user WHERE email=%s", (auth.username,)
   )
   #  IF USER EXISTS
   if result > 0:
      usr, pwd = cur.fetchone()
      if auth.username == usr and auth.password == pwd:
         return generateJWT(auth.username, os.environ.get("JWT_SECRET"), True)
      else:
         return "Credentials are invalid to access Gateway API", 401
   # USER DOES NOT EXIST IN DATABASE - DO NOT HAVE ACCESS
   else:
      return "Credentials are invalid to access Gateway API", 401

@server.route("/validate", methods=["POST"])
def validate():
   encoded_jwt = request.headers["Authorization"]

   if not encoded_jwt:
      return "Credentials are missing. Unable to access Gateway API.", 401

   jwt_secret = os.environ.get("JWT_SECRET")
   token_jwt = encoded_jwt.split(" ")[1]

   try:
      decoded_token = jwt.decode(token_jwt, jwt_secret, algorithm=['HS256'])
      
   except:
      return "Credentials are invalid to access Gateway API", 401

   return decoded_token, 200



   




def generateJWT(username, secret, authority):
   return jwt.encode({"username": username,
    "expiration": datetime.datetime.utcnow() + datetime.timedelta(hours=8),
     "iat": datetime.datetime.utcnow(),
      "admin": authority,
   },
    secret,
     algorithm="HS256",
   )


if __name__ == "__main__":
   # host="0.0.0.0" tells OS to listen on all public IPs - see flask documentation 
   server.run(host="0.0.0.0", port=5000, )



