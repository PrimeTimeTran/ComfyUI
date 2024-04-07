---
tags: 
Review_Count: "1"
---
# LC SQL 50

- Select:
- Basic Joins:
- Basic Aggregate Functions:
- Sorting and Grouping:
- Advanced Select and Joins:
- Subqueries:
- Advanced String Functions / Regex / Clause:
## Sorting & Grouping

### 2356. Number of Unique Subjects Taught By Each

- Use `DISTINCT` to ensure we get unique subjects and `COUNT` them.
- Use `GROUP BY` which is required by `COUNT`.

  ```sql
		select teacher_id, count(distinct subject_id) as cnt
		from teacher
		group by teacher_id
	```

### 1141. User Activity for the Past 30 Days I

- `DATE_SUB`  & `INTERVAL` to query a range
  ```sql
		select activity_date as day, count(distinct user_id) as active_users
		from activity
		WHERE activity_date >= DATE_SUB('2019-07-27', INTERVAL 29 DAY)
		AND activity_date <= '2019-07-27'
		group by activity_date
	```

### 1070. Product Sales Analysis III

- Use subquery to filter for just one year
  ```sql
		select sales.product_id, year as first_year, quantity, price 
		from sales 
		where (sales.product_id, year) in ( 
			select sales.product_id, min(year) 
			from sales join product on sales.product_id = product.product_id 
			group by product_id 
		)
	```

### 596. Classes More Than 5 Students

- Use `USING` to filter classes which don't meet requirements.
  ```sql
		select class from courses group by class having count(student) >= 5
	```

### 1729. Find Followers Count

- Count distinct follower_id's for the individual users
  ```sql
		select user_id, count(distinct follower_id) as followers_count
		from followers
		group by user_id
	```

### 619. Biggest Single Number

- Combine a subquery with group by & having to meet requirements
  ```sql
		select max(num) as num
		from (select num from mynumbers group by num having count(num) = 1)
		as unique_numbers
	```

### 1045. Customers Who Bought All Products

- Use subquery to collect all product keys and compare that to disticnt product_key's of each customer.
  ```sql
		SELECT customer_id FROM Customer GROUP BY customer_id
		HAVING COUNT(distinct product_key) = (SELECT COUNT(product_key) FROM Product)
	```

## Advanced Select & Joins

### 1731. The Number of Employees Which Report to

- Reuse the table to compare the fields we need per requirements
  ```sql
		select m.employee_id as employee_id, m.name,
		count(*) as reports_count,
		round(avg(sub.age), 0) as average_age
		from employees m
		join employees sub
		on m.employee_id = sub.reports_to
		group by employee_id
		order by employee_id
	```

### 1789. Primary Department for Each Employee

- Use `WHERE IN` with `OR` to specify two differing criteria(which match the two requested)
  ```sql
		SELECT DISTINCT employee_id, department_id
		FROM Employee
		WHERE employee_id IN (
			SELECT employee_id
			FROM Employee
			GROUP BY employee_id
			HAVING COUNT(*) = 1
		)
		OR primary_flag = 'Y'
		ORDER BY employee_id;
	```
- Use `UNION` to join two seperate selects works too.
	```sql
		select employee_id, department_id from employee
		group by employee_id
		having count(employee_id) = 1
		union
		select employee_id, department_id from employee where primary_flag = 'Y'
	```

### 610. Triangle Judgement

- Memorize the properties of a triangle.
- Two sides must sum to greater than the lenth of the 3rd.
  ```sql
		SELECT *, IF(x+y>z and y+z>x and z+x>y, "Yes", "No") as triangle FROM Triangle
	```

### 180. Consecutive Numbers

- f

  ```sql

	```

### 1164. Product Price at a Given Date

- f

  ```sql

	```

### 1204. Last Person to Fit in the Bus

- f

  ```sql

	```

### 1907. Count Salary Categories

- f

  ```sql

	```

## Subqueries

### 1978. Employees Whose Manager Left the Company

- f

  ```sql

	```

### 626. Exchange Seats

- f

  ```sql

	```

### 1341. Movie Rating

- f

  ```sql

	```

### 1321. Restaurant Growth

- f

  ```sql

	```

### 602. Friend Requests II: Who Has The Most Friends Requests

- f

  ```sql

	```

### 585. Investments in 2016

- f

  ```sql

	```

### 185. Department Top Three Salaries

- f

  ```sql

	```

## Advanced String Functions / Regex / Clause

### 1667. Fix Names in a Table

- f

  ```sql

	```

### 1527. Patients With a Condition

- f

  ```sql

	```

### 196. Delete Duplicate Emails

- f

  ```sql

	```

### 176. Second Highest Salary

- f

  ```sql

	```

### 1484. Group Sold Products By Date

- f

  ```sql

	```

### 1327. List the Products Ordered in a Period

- f

  ```sql

	```

### 1517. Find Users with Valid E-Mails

- f

  ```sql

	```
