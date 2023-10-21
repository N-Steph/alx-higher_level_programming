-- Script that creates the database hbtn_0d_usa and table cities
-- create database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- access database hbtn_0d_usa
\u hbtn_0d_usa
-- create tabel cities
CREATE TABLE IF NOT EXISTS cities(
	id INT NOT NULL UNIQUE AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(state_id) REFERENCES states(id)
	);
