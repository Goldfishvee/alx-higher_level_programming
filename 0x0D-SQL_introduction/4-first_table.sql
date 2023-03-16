-- This script will create a table called `first_table` in an

-- existing db	hbtn_0c_0`.-- `first_table` will have:

-- `id` INT

-- `name` VARCHAR(256)

-- The dbname will be passed as an argument to the command

-- if table already exists, script should not fail

CREATE TABLE IF NOT EXISTS `first_table` (

	`id` INT,

	`name` VARCHAR(256)

	);
