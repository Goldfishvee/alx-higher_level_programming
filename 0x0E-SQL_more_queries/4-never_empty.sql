-- This script will create a table `id_not_null`

-- Table will have the ff desc:

--  id INT with default value 1

--  name VARCHAR(256)

-- Script should not fail if table name already exists

-- db name will be passed as an arg to the mysql command

CREATE TABLE 

IF NOT EXISTS `id_not_null` (`id` INT DEFAULT 1, `name` VARCHAR(256));
