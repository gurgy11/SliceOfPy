CREATE TABLE IF NOT EXISTS outgoing_orders (
	id INT AUTO_INCREMENT,
    order_id INT NOT NULL,
    client_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price_per_unit DOUBLE NOT NULL,
    price_shipping DOUBLE,
    warehouse_start_id INT NOT NULL,
    due_date DATETIME,
    eta DATETIME,
    delivery_status VARCHAR(100) NOT NULL,
    notes TEXT,
    user_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    CONSTRAINT FK_order_id FOREIGN KEY (order_id) REFERENCES orders(id),
    CONSTRAINT FK_client_id FOREIGN KEY (client_id) REFERENCES clients(id),
    CONSTRAINT FK_product_id FOREIGN KEY (product_id) REFERENCES products(id),
    CONSTRAINT FK_warehouse_id FOREIGN KEY (warehouse_start_id) REFERENCES warehouses(id),
    CONSTRAINT FK_user_id FOREIGN KEY (user_id) REFERENCES users(id)
);