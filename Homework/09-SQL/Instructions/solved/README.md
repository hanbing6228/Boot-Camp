# Employee Database: A Mystery in Two Parts

![sql.png](sql.png)

## Background

It is a beautiful spring day, and it is two weeks since you have been hired as a new data engineer at Pewlett Hackard. Your first major task is a research project on employees of the corporation from the 1980s and 1990s. All that remain of the database of employees from that period are six CSV files.

In this assignment, you will design the tables to hold data in the CSVs, import the CSVs into a SQL database, and answer questions about the data. In other words, you will perform:

1. Data Modeling

2. Data Engineering

3. Data Analysis

## Instructions

#### Data Modeling

Inspect the CSVs and sketch out an ERD of the tables.
![dbd.png](dbd.png)

#### Data Engineering

* Use the information you have to create a table schema for each of the six CSV files. Remember to specify data types, primary keys, foreign keys, and other constraints.

* Import each CSV file into the corresponding SQL table.

-- Data Engineering

-- ----------------------------
--  Table structure for departments
-- ----------------------------
DROP TABLE IF EXISTS "public"."departments";
CREATE TABLE "public"."departments" (
	"dept_no" varchar(255) NOT NULL COLLATE "default",
	"dept_name" varchar(255) COLLATE "default"
)
WITH (OIDS=FALSE);
ALTER TABLE "public"."departments" OWNER TO "postgres";

-- ----------------------------
--  Table structure for dept_emp
-- ----------------------------
DROP TABLE IF EXISTS "public"."dept_emp";
CREATE TABLE "public"."dept_emp" (
	"emp_no" int4 NOT NULL,
	"dept_no" varchar(255) NOT NULL COLLATE "default",
	"from_date" varchar(255) COLLATE "default",
	"to_date" varchar(255) COLLATE "default"
)
WITH (OIDS=FALSE);
ALTER TABLE "public"."dept_emp" OWNER TO "postgres";

-- ----------------------------
--  Table structure for dept_manager
-- ----------------------------
DROP TABLE IF EXISTS "public"."dept_manager";
CREATE TABLE "public"."dept_manager" (
	"dept_no" varchar(255) NOT NULL COLLATE "default",
	"emp_no" int4 NOT NULL,
	"from_date" varchar(255) COLLATE "default",
	"to_date" varchar(255) COLLATE "default"
)
WITH (OIDS=FALSE);
ALTER TABLE "public"."dept_manager" OWNER TO "postgres";

-- ----------------------------
--  Table structure for employees
-- ----------------------------
DROP TABLE IF EXISTS "public"."employees";
CREATE TABLE "public"."employees" (
	"emp_no" int4 NOT NULL,
	"birth_date" varchar(255) COLLATE "default",
	"first_name" varchar(255) COLLATE "default",
	"last_name" varchar(255) COLLATE "default",
	"gender" varchar(255) COLLATE "default",
	"hire_date" varchar(255) COLLATE "default"
)
WITH (OIDS=FALSE);
ALTER TABLE "public"."employees" OWNER TO "postgres";

-- ----------------------------
--  Table structure for salaries
-- ----------------------------
DROP TABLE IF EXISTS "public"."salaries";
CREATE TABLE "public"."salaries" (
	"emp_no" int4 NOT NULL,
	"salary" int4,
	"from_date" varchar(255) COLLATE "default",
	"to_date" varchar(255) COLLATE "default"
)
WITH (OIDS=FALSE);
ALTER TABLE "public"."salaries" OWNER TO "postgres";

-- ----------------------------
--  Table structure for titles
-- ----------------------------
DROP TABLE IF EXISTS "public"."titles";
CREATE TABLE "public"."titles" (
	"emp_no" int4 NOT NULL,
	"title" varchar(255) COLLATE "default",
	"from_date" varchar(255) COLLATE "default",
	"to_date" varchar(255) COLLATE "default"
)
WITH (OIDS=FALSE);
ALTER TABLE "public"."titles" OWNER TO "postgres";

-- ----------------------------
--  Primary key structure for table departments
-- ----------------------------
ALTER TABLE "public"."departments" ADD PRIMARY KEY ("dept_no") NOT DEFERRABLE INITIALLY IMMEDIATE;

-- ----------------------------
--  Primary key structure for table dept_emp
-- ----------------------------
ALTER TABLE "public"."dept_emp" ADD PRIMARY KEY ("emp_no", "dept_no") NOT DEFERRABLE INITIALLY IMMEDIATE;

-- ----------------------------
--  Primary key structure for table dept_manager
-- ----------------------------
ALTER TABLE "public"."dept_manager" ADD PRIMARY KEY ("dept_no", "emp_no") NOT DEFERRABLE INITIALLY IMMEDIATE;

-- ----------------------------
--  Primary key structure for table employees
-- ----------------------------
ALTER TABLE "public"."employees" ADD PRIMARY KEY ("emp_no") NOT DEFERRABLE INITIALLY IMMEDIATE;

-- ----------------------------
--  Primary key structure for table salaries
-- ----------------------------
ALTER TABLE "public"."salaries" ADD PRIMARY KEY ("emp_no") NOT DEFERRABLE INITIALLY IMMEDIATE;


#### Data Analysis

Once you have a complete database, do the following:

1. List the following details of each employee: employee number, last name, first name, gender, and salary.

SELECT
	"public".employees."emp_no",
	"public".employees."last_name",
	"public".employees."first_name",
	"public".salaries."salary"
FROM
	"public".employees
JOIN
    "public".salaries
ON
    "public".employees."emp_no" = "public".salaries."emp_no";
    
    

2. List employees who were hired in 1986.
SELECT
	"public".employees."emp_no",
	"public".employees."last_name",
	"public".employees."first_name",
	"public".employees."hire_date"
FROM
	"public".employees
WHERE
	"public".employees."hire_date" BETWEEN '1986-01-01'
AND '1986-12-31';


3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.

SELECT
"public"."dept_manager"."dept_no",
"public"."dept_manager"."emp_no",
"public".departments."dept_name",
"public"."dept_manager"."from_date",
"public"."dept_manager"."to_date",
"public".employees."last_name",
"public".employees."first_name"
FROM
"public".departments
JOIN
"public".dept_manager
ON
"public".departments.dept_no = "public".dept_manager.dept_no
JOIN 
"public".employees
ON
"public".dept_manager.emp_no = "public".employees.emp_no;

4. List the department of each employee with the following information: employee number, last name, first name, and department name.

SELECT
"public".departments."dept_no",
"public".departments."dept_name",
"public"."dept_emp"."emp_no",
"public".employees."first_name",
"public".employees."last_name"
FROM
"public".dept_emp
JOIN employees
ON 
"public".dept_emp.emp_no = "public".employees.emp_no
JOIN 
"public".departments
ON 
"public".dept_emp.dept_no = "public".departments.dept_no;


5. List all employees whose first name is "Hercules" and last names begin with "B."

SELECT
	"public".employees."first_name",
	"public".employees."last_name"
FROM
	"public".employees	
WHERE
	"public".employees."first_name" = 'Hercules' 
AND
	"public".employees."last_name" like 'B%';
    
    

6. List all employees in the Sales department, including their employee number, last name, first name, and department name.

SELECT
	"public".departments."dept_name",
	"public".employees."emp_no",
	"public".employees."first_name",
	"public".employees."last_name"
FROM
	"public".dept_emp    
JOIN 
	"public".employees
ON 
	"public".dept_emp.emp_no = "public".employees.emp_no
JOIN 
	"public".departments
ON 
	"public".dept_emp.dept_no = "public".departments.dept_no    
WHERE
	"public".departments."dept_name" = 'Sales';
    
    

7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

SELECT
	"public".departments."dept_name",
	"public".employees."emp_no",
	"public".employees."first_name",
	"public".employees."last_name"
FROM
	"public".dept_emp    
JOIN 
	"public".employees
ON 
	"public".dept_emp.emp_no = "public".employees.emp_no
JOIN 
	"public".departments
ON 
	"public".dept_emp.dept_no = "public".departments.dept_no  
WHERE
	"public".departments."dept_name" = 'Sales' OR
	"public".departments."dept_name" = 'Development';
    

8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

SELECT
COUNT("public".employees."last_name") AS "Total Last Name",
"public".employees."last_name"
FROM
"public".employees
GROUP BY
"public".employees."last_name"
ORDER BY
"Total Last Name" DESC;


## Bonus (Optional)

As you examine the data, you are overcome with a creeping suspicion that the dataset is fake. You surmise that your boss handed you spurious data in order to test the data engineering skills of a new employee. To confirm your hunch, you decide to take the following steps to generate a visualization of the data, with which you will confront your boss:

1. Import the SQL database into Pandas. 

2. Create a bar chart of average salary by title.


![average_sales_titles.png](average_sales_titles.png)

3. You may also include a technical report in markdown format, in which you outline the data engineering steps taken in the homework assignment.

## Technical Report Outlining Data Engineering Steps Taken:
#Sketched out Entity Relationship Diagram (ERD) of employee database tables; specifying data types, primary keys and foreign keys.
#Exported ERD to PostgreSQL thus creating table schemas and contraints for each of the six CSV files.
#Imported CSV files to each corresponding SQL table.

## Epilogue

Evidence in hand, you march into your boss's office and present the visualization. With a sly grin, your boss thanks you for your work. On your way out of the office, you hear the words, "Search your ID number." You look down at your badge to see that your employee ID number is 499942.


* (Optional) Create a Jupyter Notebook of the bonus analysis.

* Create and upload a repository with the above files to GitHub and post a link on BootCamp Spot.
