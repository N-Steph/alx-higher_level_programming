-- Script that creates the database hbtn_0d_usa and table states
-- create the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- access database hbtn_0d_usa
\u hbtn_0d_usa
-- create the table states
CREATE TABLE IF NOT EXISTS states(
	id INT UNIQUE AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id)
	);
