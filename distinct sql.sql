CREATE TABLE IF NOT EXISTS PRODUCTS (
PRODUCT_ID TEXT PRIMARY KEY,
PRODUCT_NAME TEXT,
SUPPLIER TEXT,
CATEGORY TEXT,
UNIT_TEXT TEXT,
PRICE TEXT
);

INSERT INTO PRODUCTS (PRODUCT_ID, PRODUCT_NAME, SUPPLIER, CATEGORY, UNIT_TEXT, PRICE) VALUES
('1', 'Chai', 'Exotic Liquids', 'Beverages', '10 boxes x 20 bags', '18.00'),
('2', 'Chang', 'Exotic Liquids', 'Beverages', '24 - 12 oz bottles', '19.00'),
('3', 'Aniseed Syrup', 'Exotic Liquids', 'Condiments', '12 - 550 ml bottles', '10.00'),
('4', "Chef Anton's Cajun Seasoning", "New Orleans Cajun Delights", "Condiments", "48 - 6 oz jars", "22.00"),
('5', "Chef Anton's Gumbo Mix", "New Orleans Cajun Delights", "Condiments", "36 boxes", "21.35");

SELECT * FROM PRODUCTS;

SELECT COUNT(PRODUCT_ID) AS PRODUCT_COUNT FROM PRODUCTS;

SELECT AVG(PRICE) AS AVERAGE_PRICE FROM PRODUCTS;

SELECT SUM(PRICE) AS TOTAL_PRICE FROM PRODUCTS;