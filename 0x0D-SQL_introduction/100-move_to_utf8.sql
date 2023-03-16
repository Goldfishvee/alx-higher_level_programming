-- This script will convert `hbtn_0c_0`, `first_table` and `name` to:

-- 'UTF8', 'utf8mb4', and `utf8mb4_unicode_ci'

USE `hbtn_0c_0` 

ALTER TABLE `first_table` 

CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
