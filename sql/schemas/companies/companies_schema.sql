CREATE TABLE IF NOT EXISTS companies (
	id INT AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    website_url VARCHAR(255),
    address_id INT NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (address_id) REFERENCES addresses(id)
);
