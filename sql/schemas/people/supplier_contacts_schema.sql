CREATE TABLE IF NOT EXISTS supplier_contacts (
	id INT AUTO_INCREMENT,
    contact_id INT NOT NULL,
    supplier_id INT NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (contact_id) REFERENCES contacts(id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);