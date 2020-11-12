-- Categories Table Schema --
CREATE TABLE IF NOT EXISTS categories (
	id INT AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
	description TEXT NOT NULL,
	notes TEXT,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
);
