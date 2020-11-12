CREATE TABLE IF NOT EXISTS orders (
	id INT AUTO_INCREMENT,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);