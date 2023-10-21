-- Script that creates the database hbtn_0d_2 and user user_0d_2
-- This command creates hbtn_0d_2 database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create user user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grant SELECT privilege to user_0d_2
GRANT SELECT ON htbn_0d_2 TO 'user_0d_2'@'localhost';
