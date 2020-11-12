CREATE TABLE IF NOT EXISTS locations_occupied (
	id INT AUTO_INCREMENT,
    location_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity_in_location INT NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (location_id) REFERENCES locations(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);