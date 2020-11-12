CREATE TABLE IF NOT EXISTS warehouses (
	id INT AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    prefix VARCHAR(25) NOT NULL,
    description TEXT,
    address_id INT NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (address_id) REFERENCES addresses(id)
);