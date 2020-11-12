CREATE TABLE IF NOT EXISTS locations (
	id INT AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    warehouse_id INT NOT NULL,
    description TEXT,
    occupied BOOL DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(id)
);