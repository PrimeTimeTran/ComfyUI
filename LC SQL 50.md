---
tags:
---

# LC SQL 50

- Select:
- Basic Joins:
- Basic Aggregate Functions:
- Sorting and Grouping:
- Advanced Select and Joins:
- Subqueries:
- Advanced String Functions / Regex / Clause:

## Select

### 1757. Recyclabe and Low Fat Products

- Return only what's requested.
  ```sql
  	select product_id from Products where low_fats = "Y" and recyclable = "Y";
  ```

### 584. Find Customer Referee

- For including `null` values from field use `is null`.
  ```sql
  	select name from customer c where not c.referee_id = 2 or c.referee_id is null;
  ```

### 595. Big Countries

- "At least" means using `>=` instead of less than or `>`.
  ```sql
  	select name, population, area from world where area >= 3000000 or population >= 25000000;
  ```

### 1148. Article Views

- Filter duplicates.
- Alias result field name.
- Compare fields from same table.
- Order by field.
  ```sql
    select distinct v.author_id as id
    from views v
    where v.viewer_id = v.author_id
    order by v.author_id ASC
  ```

### 1683. Invalid Tweets

- Use arithmetic in where clauses.
  ```sql
  select tweet_id from tweets where length(content) > 15
  ```

## Basic Joins

### 1378. Replace Employee Id with the Unique Identifier

- Return all records from left/first table regardless of if there's a corresponding value in the second table.
  ```sql
  select empu.unique_id, name from employees emp left join employeeuni empu on emp.id = empu.id;
  ```

### 1068. Product Sales Analysis I

- Join on `id`.
  ```sql
    select product_name, year, price
    from sales as s
    join product as p
    on s.product_id = p.product_id
  ```

### 1581. Customer who visited but did not make any transactions

- Find null existance in one table.
- Group results and count records.
  ```sql
    select customer_id, count(v.visit_id) as count_no_trans
    from visits v
    left join transactions t
    on v.visit_id = t.visit_id
    where transaction_id is null
    group by customer_id
  ```

### 197. Rising Temperature

- Alias a table to compare itself with itself.
- Use `DATEDIFF` to compare different dates of records.
  ```sql
    SELECT w1.id
    FROM Weather w2, Weather w1
    WHERE w1.Temperature > w2.Temperature AND DATEDIFF(w1.recordDate, w2.recordDate) = 1
  ```

### 1661. Average Time of Process Per Machine

How to flatten our results into a few rows?

- Alias to reuse table.
- Combine `avg` & `round` for arithmetic.
- Group by to combine results.
  ```sql
  	SELECT s.machine_id, ROUND(AVG(e.timestamp-s.timestamp), 3) AS processing_time
  	FROM Activity s JOIN Activity e ON
  	s.machine_id = e.machine_id AND s.process_id = e.process_id AND
  	s.activity_type = 'start' AND e.activity_type = 'end'
  	GROUP BY s.machine_id
  ```

### 577. Employee Bonus

- f

  ```sql

  ```

### 1280. Students and Examinations

- f

  ```sql

  ```

### 570. Managers with at Least 5 Direct Reports

- f

  ```sql

  ```

### 1934. Confirmation Rate

- f

  ```sql

  ```

# Basic Aggregate Functions

### 620. Not Boring Movies

- f

  ```sql

  ```

### 1251. Average Selling Price

- f

  ```sql

  ```

### 1075. Project Employees I

- f

  ```sql

  ```

### 1633. Percentage of Users Attended a Contest

- f

  ```sql

  ```

### 1211. Queries Quality and Percentage

- f

  ```sql

  ```

### 1193. Monthly Transactions I

- f

  ```sql

  ```

### 1174. Immediate Food Delivery II

- f

  ```sql

  ```

### 550. Game Play Analysis IV

- f

  ```sql

  ```

# Sorting & Grouping

### 2356. Number of Unique Subjects Taught By Each

- f

  ```sql

  ```

### 1141. User Activity for the Past 30 Days I

- f

  ```sql

  ```

### 1070. Product Sales Analysis III

- f

  ```sql

  ```

### 596. Classes More Than 5 Students

- f

  ```sql

  ```

### 1729. Find Followers Count

- f

  ```sql

  ```

### 619. Biggest Single Number

- f

  ```sql

  ```

### 1045. Customers Who Bought All Products

- f

  ```sql

  ```

## Advanced Select & Joins

### 1731. The Number of Employees Whcih Report to

- f

  ```sql

  ```

### 1789. Primary Department for Each Employee

- f

  ```sql

  ```

### 610. Triangle Judgement

- f

  ```sql

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

  ````sql

    	```
  ````

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
