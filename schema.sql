DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	comment TEXT NOT NULL
);
