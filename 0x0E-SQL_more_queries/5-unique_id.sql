-- This script will create a table `unique_id` with the desc:

--  `id` INT def value 1 and unique

--  `name` VARCHAR(256)

-- Script should not fail if table already exists

-- db name will be passed as an arg of the mysql command

CREATE TABLE IF NOT EXISTS `unique_id`

(`id` INT DEFAULT 1 UNIQUE, `name` VARCHAR(256));
