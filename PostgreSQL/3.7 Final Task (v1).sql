Query:
```sql
SELECT u.country, to_char(oi.created_at, 'yyyy-mm') AS year_month_order,
(SUM(oi.sale_price)â€Š-â€ŠLAG(SUM(oi.sale_price)) OVER(PARTITION BY u.country ORDER BY to_char(oi.created_at, 'yyyy-mm'))) / SUM(oi.sale_price) AS sales_increase_persentage
FROM users u RIGHT JOIN order_items oi
ON u.id = oi.user_idÂ 
WHERE (to_char(oi.created_at, 'yyyy-mm') >= '2021â€“09') AND (u.country IN ('Japan', 'South Korea', 'China'))
GROUP BY u.country, year_month_order
ORDER BY u.country
```

Gsheet link:

https://docs.google.com/spreadsheets/d/19hVx0gQoIjDdLflgPJtgFzXF4OauRzybomyq3X_9Zvk/edit?usp=sharing
