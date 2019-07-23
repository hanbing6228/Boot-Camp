-- Data Analysis


--1
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


--2
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

--3
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


--4
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



--5
SELECT
	"public".employees."first_name",
	"public".employees."last_name"
FROM
	"public".employees	
WHERE
	"public".employees."first_name" = 'Hercules' 
AND
	"public".employees."last_name" like 'B%';



--6
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



--7
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



--8
SELECT
COUNT("public".employees."last_name") AS "Total Last Name",
"public".employees."last_name"
FROM
"public".employees
GROUP BY
"public".employees."last_name"
ORDER BY
"Total Last Name" DESC