CREATE DATABASE employee_resignation_db;
USE employee_resignation_db;
CREATE TABLE EmployeeResignations (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(100),
    Gender VARCHAR(10),
    Age INT,
    Department VARCHAR(50),
    JobRole VARCHAR(50),
    DateOfJoining DATE,
    DateOfExit DATE,
    PerformanceRating INT,
    ResignationReason VARCHAR(100),
    LastWorkingLocation VARCHAR(50)
);
ALTER TABLE EmployeeResignations
ADD COLUMN `Tenure (Years)` DECIMAL(5,2),
ADD COLUMN YearOfExit INT;
SELECT COUNT(*) AS TotalEmployees
FROM employee_resignation_db.EmployeeResignations;
SELECT *
FROM EmployeeResignations
LIMIT 10;
DESCRIBE EmployeeResignations;

SELECT
    COUNT(*) AS Total_Resignations,
    ROUND(AVG(Age), 2) AS Average_Age,
    ROUND(AVG(`Tenure (Years)`), 2) AS Average_Tenure
FROM EmployeeResignations;

SELECT
    Department,
    COUNT(EmployeeID) AS Total_Resignations
FROM EmployeeResignations
GROUP BY Department
ORDER BY Total_Resignations DESC;

SELECT
    Gender,
    COUNT(EmployeeID) AS Total_Resignations
FROM EmployeeResignations
GROUP BY Gender
ORDER BY Total_Resignations DESC;
SELECT
    ResignationReason,
    COUNT(EmployeeID) AS Total_Resignations
FROM EmployeeResignations
GROUP BY ResignationReason
ORDER BY Total_Resignations DESC;
SELECT
    YearOfExit,
    COUNT(EmployeeID) AS Total_Resignations
FROM EmployeeResignations
GROUP BY YearOfExit
ORDER BY YearOfExit;
SELECT
    PerformanceRating,
    COUNT(EmployeeID) AS Total_Resignations
FROM EmployeeResignations
GROUP BY PerformanceRating
ORDER BY PerformanceRating;
SELECT
    COUNT(EmployeeID) AS High_Performer_Resignations
FROM EmployeeResignations
WHERE PerformanceRating >= 4;
SELECT
    Department,
    Gender,
    COUNT(EmployeeID) AS Total_Resignations
FROM EmployeeResignations
GROUP BY Department, Gender
ORDER BY Department, Gender;

SELECT
    Department,
    ROUND(AVG(`Tenure (Years)`), 2) AS Average_Tenure
FROM EmployeeResignations
GROUP BY Department
ORDER BY Average_Tenure DESC;
SELECT
    Department,
    COUNT(EmployeeID) AS High_Performer_Resignations
FROM EmployeeResignations
WHERE PerformanceRating >= 4
GROUP BY Department
ORDER BY High_Performer_Resignations DESC;
SELECT
    CASE
        WHEN Age < 25 THEN 'Below 25'
        WHEN Age BETWEEN 25 AND 34 THEN '25-34'
        WHEN Age BETWEEN 35 AND 44 THEN '35-44'
        WHEN Age BETWEEN 45 AND 54 THEN '45-54'
        ELSE '55 and Above'
    END AS Age_Group,
    COUNT(EmployeeID) AS Total_Resignations
FROM EmployeeResignations
GROUP BY Age_Group
ORDER BY Total_Resignations DESC;

SELECT
    LastWorkingLocation,
    COUNT(EmployeeID) AS Total_Resignations
FROM EmployeeResignations
GROUP BY LastWorkingLocation
ORDER BY Total_Resignations DESC;

SELECT
    YearOfExit,
    Gender,
    COUNT(EmployeeID) AS Total_Resignations
FROM EmployeeResignations
GROUP BY YearOfExit, Gender
ORDER BY YearOfExit, Gender;
SELECT
    Department,
    ROUND(AVG(Age), 2) AS Average_Age
FROM EmployeeResignations
GROUP BY Department
ORDER BY Average_Age DESC;

SELECT
    JobRole,
    COUNT(EmployeeID) AS Total_Resignations
FROM EmployeeResignations
GROUP BY JobRole
ORDER BY Total_Resignations DESC;

SELECT
    Department,
    ROUND(AVG(PerformanceRating), 2) AS Average_Performance
FROM EmployeeResignations
GROUP BY Department
ORDER BY Average_Performance DESC;

SELECT
    Department,
    ResignationReason,
    COUNT(EmployeeID) AS Total_Resignations
FROM EmployeeResignations
GROUP BY Department, ResignationReason
ORDER BY Department, Total_Resignations DESC;

SELECT
    Gender,
    ResignationReason,
    COUNT(EmployeeID) AS Total_Resignations
FROM EmployeeResignations
GROUP BY Gender, ResignationReason
ORDER BY Gender, Total_Resignations DESC;

SELECT
    CASE
        WHEN `Tenure (Years)` < 2 THEN 'Less than 2 years'
        WHEN `Tenure (Years)` BETWEEN 2 AND 5 THEN '2-5 years'
        WHEN `Tenure (Years)` BETWEEN 5.01 AND 10 THEN '5-10 years'
        ELSE 'More than 10 years'
    END AS Tenure_Group,
    COUNT(EmployeeID) AS Total_Resignations
FROM EmployeeResignations
GROUP BY Tenure_Group
ORDER BY Total_Resignations DESC;

SELECT
    ResignationReason,
    COUNT(EmployeeID) AS High_Performer_Resignations
FROM EmployeeResignations
WHERE PerformanceRating >= 4
GROUP BY ResignationReason
ORDER BY High_Performer_Resignations DESC;

