CREATE TABLE IF NOT EXISTS suppliers (
	id INT AUTO_INCREMENT,
    company_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (company_id) REFERENCES companies(id)
);
