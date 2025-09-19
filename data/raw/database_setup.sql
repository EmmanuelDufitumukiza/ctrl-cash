-- Create Database
CREATE DATABASE momo_db;
USE momo_db;

-- Users Table
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Transaction Categories
CREATE TABLE Transaction_Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    description TEXT
);

-- Transactions
CREATE TABLE Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(12,2) NOT NULL CHECK (amount > 0),
    currency VARCHAR(10) DEFAULT 'RWF',
    transaction_date DATETIME NOT NULL,
    status ENUM('SUCCESS','FAILED','PENDING') NOT NULL,
    sender_id INT,
    receiver_id INT,
    category_id INT,
    FOREIGN KEY (sender_id) REFERENCES Users(user_id),
    FOREIGN KEY (receiver_id) REFERENCES Users(user_id),
    FOREIGN KEY (category_id) REFERENCES Transaction_Categories(category_id),
    INDEX (transaction_date),
    INDEX (sender_id),
    INDEX (receiver_id)
);

-- System Logs
CREATE TABLE System_Logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_id INT,
    action VARCHAR(100) NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    performed_by VARCHAR(50),
    FOREIGN KEY (transaction_id) REFERENCES Transactions(transaction_id)
);

-- Sample Data Inserts
INSERT INTO Users (full_name, phone_number, email) VALUES
('Alice Umutoni', '+250788111111', 'alice@example.com'),
('John Mugisha', '+250788222222', 'john@example.com'),
('Eric Niyonzima', '+250788333333', NULL),
('Grace Uwimana', '+250788444444', 'grace@example.com'),
('Paul Habimana', '+250788555555', 'paul@example.com');

INSERT INTO Transaction_Categories (category_name, description) VALUES
('Deposit', 'Money deposited into account'),
('Withdrawal', 'Cash withdrawal from account'),
('Bill Payment', 'Utility or service payment'),
('P2P Transfer', 'Person-to-person transfer'),
('Merchant Payment', 'Payment to merchants');

INSERT INTO Transactions (amount, currency, transaction_date, status, sender_id, receiver_id, category_id) VALUES
(5000.00, 'RWF', '2025-09-19 12:00:00', 'SUCCESS', 1, 2, 4),
(15000.00, 'RWF', '2025-09-18 10:30:00', 'SUCCESS', 2, 3, 1),
(2000.00, 'RWF', '2025-09-18 11:15:00', 'FAILED', 3, 4, 2),
(7500.00, 'RWF', '2025-09-17 15:45:00', 'PENDING', 4, 5, 3),
(12000.00, 'RWF', '2025-09-16 09:20:00', 'SUCCESS', 5, 1, 5);

INSERT INTO System_Logs (transaction_id, action, performed_by) VALUES
(1, 'Parsed from XML', 'system'),
(1, 'Inserted to DB', 'etl_service'),
(2, 'Parsed from XML', 'system'),
(3, 'Validation Failed', 'etl_service'),
(5, 'API Served', 'api_gateway');
