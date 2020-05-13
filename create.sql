CREATE TABLE IF NOT EXISTS users (
id SERIAL PRIMARY KEY,
username VARCHAR NOT NULL,
password VARCHAR NOT NULL);

CREATE TABLE IF NOT EXISTS books (
isbn INT PRIMARY KEY,
title VARCHAR NOT NULL,
author VARCHAR NOT NULL,
year VARCHAR NOT NULL);

CREATE TABLE IF NOT EXISTS reviews (
id SERIAL PRIMARY KEY,
user_id INT NOT NULL,
book_isbn INT NOT NULL,
rating INT NOT NULL,
review_text VARCHAR NOT NULL);

# needed to be inserted from the command line
# (env) [dwood@dw01 project1]$ psql postgres://kajyrhucwqwtdx:7027643b5384b13e7187854e0999702e10adfcb6285e# f5c98f81d9cfe0646710@ec2-54-247-72-30.eu-west-1.compute.amazonaws.com:5432/drkmkun2prsam -f create.sql

# Also inserted a single user to begin with

(env) [dwood@dw01 project1]$ psql postgres://kajyrhucwqwtdx:7027643b5384b13e7187854e0999702e10adfcb6285ef5c98f81d9cfe0646710@ec2-54-247-72-30.eu-west-1.compute.amazonaws.com:5432/drkmkun2prsam
psql (12.2, server 11.7 (Ubuntu 11.7-2.pgdg16.04+1))
SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
Type "help" for help.

drkmkun2prsam=> INSERT INTO users (username, password) VALUES ('admin','admin');
INSERT 0 1
drkmkun2prsam=> select * from users;
 id | username | password 
----+----------+----------
  1 | admin    | admin
(1 row)

