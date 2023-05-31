DROP TABLE one_day_posts;
DROP TABLE all_posts;
DROP TABLE give_posts;

CREATE TABLE one_day_posts
(
	id SERIAL NOT NULL PRIMARY KEY,
	full_name TEXT NOT NULL,
	description TEXT,
	img_src TEXT[],
	adding_time TIMESTAMP  ,
  	post_link text

);
CREATE TABLE give_posts
(
	id SERIAL NOT NULL PRIMARY KEY,
	full_name TEXT NOT NULL,
	description TEXT,
	img_src TEXT[],
	adding_time TIMESTAMP  ,
  	post_link text

);
CREATE TABLE all_posts
(
	id SERIAL NOT NULL PRIMARY KEY,
	full_name TEXT NOT NULL,
	description TEXT,
	img_src TEXT[],
	adding_time TIMESTAMP  ,
  	post_link text

);