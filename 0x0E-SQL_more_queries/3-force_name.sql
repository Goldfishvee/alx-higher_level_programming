-- This script will create a table `force_name` in db

-- db name will be supplied as an arg of the mysql command

-- Script should not fail is table exists already

CREATE TABLE IF NOT EXISTS `force_name` 

(`id` INT, `name` VARCHAR(256) NOT NULL);
