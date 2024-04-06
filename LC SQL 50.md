---
tags:
---

# LC SQL 50

- Select:
  - 1
- Basic Joins:
  - 1
- Basic Aggregate Functions:
  - 1
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

- Include null values.
- Include all of left table regardless of null values in right table.

  ```sql
  	select name, bonus from employee left join bonus on bonus.empId = employee.empId where bonus.bonus < 1000 or bonus is null
  ```

### 1280. Students and Examinations

- Multi table join.
- Count number of records with aggregate `count`.
- Group by student and subject because we want to know how many times each student took each subject's exam.
  ```sql
  	select s.student_id, s.student_name, sub.subject_name, count(e.subject_name) as attended_exams
  	from students s
  	join subjects sub left join examinations e
  	on e.student_id = s.student_id
  	and sub.subject_name = e.subject_name
  	group by student_id, subject_name
  	order by student_id, subject_name
  ```

### 570. Managers with at Least 5 Direct Reports

- Correlated subquery combined with aggregate `count` and filter `having`.
  ```sql
  	select name from employee
  	where id in
  	(select managerId from Employee
  	group by managerId
  	having count(*)>=5)
  ```

### 1934. Confirmation Rate

- Use conditional to assign values.
- Use aggregates to make calculations.
  ```sql
  	select s.user_id, round(avg(if(c.action = 'confirmed', 1, 0)), 2) as confirmation_rate
  	from signups s
  	left join confirmations c
  	on s.user_id = c.user_id
  	group by user_id
  ```

## Basic Aggregate Functions

### 620. Not Boring Movies

- Numeric functions are cool
  ```sql
  	select id, movie, description, rating
  	from cinema
  	where mod(id, 2) = 1 and description != 'boring'
  	order by rating desc
  ```

### 1251. Average Selling Price

- Guard against null
- Use between to ensure dates fall within domain
  ```sql
  	select p.product_id, IFNULL(ROUND(SUM(units*price)/SUM(units), 2), 0) as average_price
  	from prices p LEFT join UnitsSold u
  	on p.product_id = u.product_id and
  	u.purchase_date between start_date and end_date
  	group by product_id
  ```

### 1075. Project Employees I

- Aggregate the totals
  ```sql
  	select project_id, round(avg(e.experience_years), 2) as average_years
  	from project p join employee e on p.employee_id = e.employee_id
  	group by project_id
  ```

### 1633. Percentage of Users Attended a Contest

- Be careful the math matches the requirements
  ```sql
  	select
  	contest_id,
  	round(count(user_id) * 100 / (select count(user_id) from users), 2) as percentage
  	from Register
  	group by contest_id
  	order by percentage desc,contest_id
  ```

### 1211. Queries Quality and Percentage

- Round, avg, sum, cast, case all matter here
  ```sql
  	select
  	query_name,
  	round(avg(cast(rating as decimal) / position), 2) as quality,
  	round(sum(case when rating < 3 then 1 else 0 end) * 100 / count(*), 2) as poor_query_percentage
  	from queries
  	where query_name is not null
  	group by
  	query_name;
  ```

### 1193. Monthly Transactions I

- Sum a ton
  ```sql
  	select
  	substr(trans_date,1,7) as month,
  	country, count(id) as trans_count,
  	sum(case when state = 'approved' then 1 else 0 END) as approved_count,
  	sum(amount) as trans_total_amount,
  	sum(case when state = 'approved' then amount else 0 END) as approved_total_amount
  	from transactions
  	group by month, country
  ```

### 1174. Immediate Food Delivery II

- Use where in to filter out records which would produce errors.
  ```sql
  	select round(avg(order_date = customer_pref_delivery_date) * 100, 2) as immediate_percentage
  	from delivery
  	where (customer_id, order_date) in (
  	select customer_id, min(order_date)
  	from delivery
  	group by customer_id
  	)
  ```

### 550. Game Play Analysis IV

- Use `date_sub` to subtract days from dates.
- Use `interval 1 day` to define how much time.

  ```sql
  	SELECT
  		ROUND(COUNT(DISTINCT player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
  	FROM
  		Activity
  	WHERE
  	(player_id, DATE_SUB(event_date, INTERVAL 1 DAY))
  	IN (
  		SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id
  	)
  ```

## Sorting & Grouping

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
