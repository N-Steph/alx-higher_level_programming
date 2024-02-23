-- This script converts hbtn_0c_0 database to UTF8
-- connect to hbtn_0c_0 database
connect hbtn_0c_0
-- convert hbtn_0c_0 to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- convert first_table to UTF8
ALTER TABLE first_table CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- convert name column to UTF8
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;
