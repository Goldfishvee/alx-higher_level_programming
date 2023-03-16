-- This script will create db `hbtn_0d_usa` and table `cities` 

-- `cities` will have the desc:

--	`id`--	`state_id`

--	`name`

-- script should not fail if db and table already exists

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

USE `hbtn_0d_usa`;

CREATE TABLE IF NOT EXISTS

`cities` (`id` INT UNIQUE NOT NULL AUTO_INCREMENT,

	`state_id` INT NOT NULL,

	`name` VARCHAR(256) NOT NULL,

	PRIMARY KEY (`id`),

	FOREIGN KEY (`state_id`) REFERENCES `states` (`id`)

);
