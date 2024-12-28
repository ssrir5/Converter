-- Writing script to build database --
-- Creating user to access mySQL database --
CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'Aauth123';


CREATE DATABASE auth;

GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'localhost';

USE auth;

CREATE TABLE user(
   id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
   email VARCHAR(255) NOT NULL UNIQUE,
   password VARCHAR(255) NOT NULL
);

-- CREATES USER THAT GOES INTO DATABASE THAT HAS ACCESS TO GATEWAY API --
INSERT INTO user(email, password) VALUES ('shreyassriram@gmail.com', 'theadmin');