-- Write your PostgreSQL query statement below
SELECT product_name, year, price
FROM Sales
JOIN Product
        ON sales.product_id = product.product_id