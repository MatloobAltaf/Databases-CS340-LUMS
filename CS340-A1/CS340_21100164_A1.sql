--A
SELECT COUNT(ID) FROM CRIME;
--B
SELECT * FROM CRIME LIMIT 10;
--C
SELECT COUNT(ARREST) FROM CRIME WHERE ARREST='TRUE';
--D
SELECT AVG(SAFETY_SCORE) FROM SCHOOLS;
--E
SELECT COMMUNITY_AREA_NAME
FROM CENSUS_DATA
WHERE COMMUNITY_AREA_NAME LIKE 'B%';
--F
SELECT DISTINCT(PRIMARY_TYPE)
FROM CRIME
WHERE LOCATION_DESCRIPTION='GAS STATION';
--G
SELECT NAME_OF_SCHOOL, HEALTHY_SCHOOL_CERTIFIED
FROM SCHOOLS
WHERE COMMUNITY_AREA_NUMBER between 10 and 15 AND HEALTHY_SCHOOL_CERTIFIED = 'Yes';
--H
SELECT community_area_name, avg(college_enrollment) as average_enrollment
FROM SCHOOLS
GROUP BY community_area_name
ORDER BY average_enrollment DESC LIMIT 5;
--I
SELECT community_area_name, 	safety_score
FROM SCHOOLS
WHERE safety_score = (SELECT min(safety_score) FROM SCHOOLS);
--J
SELECT community_area_name, per_capita_income
FROM CENSUS_DATA
WHERE community_area_number  = (SELECT community_area_number FROM SCHOOLS WHERE safety_score = 1);
--K
SELECT name_of_school
FROM SCHOOLS
WHERE safety_score < (SELECT avg(safety_score) FROM SCHOOLS);
--L
SELECT CENSUS_DATA.community_area_name, per_capita_income, safety_score
FROM CENSUS_DATA JOIN SCHOOLS ON CENSUS_DATA.community_area_number = SCHOOLS.community_area_number
WHERE safety_score = 1;
