/* Assignment1 -> 1 nested (inner) query, 2 Group By clause and 1 SUM operation */
 SELECT t1.country, t1.state, SUM(t1.price)
     FROM (SELECT * FROM `salesjan2009_1`
	 WHERE payment_type = 'Visa’)t1
GROUP BY t1.country, t1.state

/* Assignment2 -> 1 sort (Order By) clause, 1 Group By clause and 1 AVG operation */
SELECT country, AVG(price)
    FROM `salesjan2009_1`
GROUP BY country ORDER BY country, AVG(Price)
