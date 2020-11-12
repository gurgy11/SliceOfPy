CREATE TABLE IF NOT EXISTS sub_categories (
	id INT AUTO_INCREMENT,
    name varchar(100),
    parent_category_id int,
    PRIMARY KEY (id),
    FOREIGN KEY (parent_category_id) REFERENCES categories(id)
);
