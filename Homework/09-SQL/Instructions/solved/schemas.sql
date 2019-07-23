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
