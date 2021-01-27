-- A task is to count the number of empolyeess with salaries less than 2000$

-- table EMPLOYEES
    -- EMP_ID INT
    -- EMP_NAME STRING
    -- SALARY INT
    
SELECT COUNT(EMP_ID)
FROM EMPLOYEES
WHERE SALARY <= 2000;