CREATE TABLE suppliers (
SNO TEXT PRIMARY KEY,
SNAME TEXT,
STATUS INTEGER,
CITY TEXT
);

INSERT INTO suppliers (SNO, SNAME, STATUS, CITY) VALUES
('S1', 'Smith', 20, 'London'),
('S2', 'Jack', 35, 'New York'),
('S3', 'Sara', 21, 'Paris'),
('S4', 'Mandy', 41, 'Rome'),
('S5', 'Ibrahim', 32, 'Lahore');

SELECT * FROM suppliers;
