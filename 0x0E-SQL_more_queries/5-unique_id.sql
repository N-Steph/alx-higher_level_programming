-- Script that creates the table unique_id
-- creates a table with unique_id with attribute id with default value 1
-- and must be unique
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
	);
