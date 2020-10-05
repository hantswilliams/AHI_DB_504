-- Before getting started, it is good to understand more about the data 
-- https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?BeginYear=2017


-- Demographic Variables and Sample Weights	DEMO_J Doc	DEMO_J Data [XPT - 3.3 MB]	February 2020
-- Blood Pressure	BPX_J Doc	BPX_J Data [XPT - 1.4 MB]	February 2020
-- Body Measures	BMX_J Doc	BMX_J Data [XPT - 1.4 MB]	February 2020
-- Cholesterol - High - Density Lipoprotein (HDL)	HDL_J Doc	HDL_J Data [XPT - 175.5 KB]	February 2020
-- Physical Activity	PAQ_J Doc	PAQ_J Data [XPT - 780.9 KB]	February 2020
-- Medical Conditions	MCQ_J Doc	MCQ_J Data [XPT - 5.2 MB]	February 2020
-- Prescription Medications	RXQ_RX_J Doc	RXQ_RX_J Data [XPT - 9.2 MB]	March 2020
-- Hospital Utilization & Access to Care	HUQ_J Doc	HUQ_J Data [XPT - 725.1 KB]	February 2020
-- Mental Health - Depression Screener	DPQ_J Doc	DPQ_J Data [XPT - 477.8 KB]	February 2020
-- Physical Functioning	PFQ_J Doc	PFQ_J Data [XPT - 2.3 MB]	February 2020


-- DEMOGRAPHICS  DEMO_J // https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Demographics&CycleBeginYear=2017
-- SEQN
-- RIAGENDR Gender of the participant.
-- RIDAGEMN Age in months of the participant at the time of screening. Reported for persons aged 24 months or younger at the time of exam (or screening if not examined).	
-- RIDAGEYR Age in years of the participant at the time of screening. Individuals 80 and over are topcoded at 80 years of age.	
-- INDFMIN2 Total family income (reported as a range value in dollars)	

-- BLOOD PRESSURE   BPX_J
-- BPXDI1 Diastolic: Blood pressure (first reading) mm Hg	 
-- BPXSY1 Systolic: Blood pressure (first reading) mm Hg	

-- BODY MEASURES     BMX_J 
-- BMXWT  Weight (kg)	 
-- BMXHT   Standing Height (cm)	 

-- CHOLESTEROL HDL_J 
-- LBDHDD Direct HDL-Cholesterol (mg/dL)	
-- LBDHDDSI Direct HDL-Cholesterol (mmol/L)	


-- PHysical Activity    PAQ_J 
-- PAQ610  In a typical week, on how many days {do you/does SP} do vigorous-intensity activities as part of {your/his/her} work?	
-- PAD675 How much time {do you/does SP} spend doing moderate-intensity sports, fitness or recreational activities on a typical day?	
-- PAD630 How much time {do you/does SP} spend doing moderate-intensity activities at work on a typical day?	


-- Medical Conditions   MCQ_J 
-- AGQ030 During the past 12 months, {have you/has SP} had an episode of hay fever?	
-- MCD180a How old {were you/was SP} when {you were/s/he was} first told {you/s/he} . . . had arthritis?	
-- MCD180b How old {were you/was SP} when {you were/s/he was} first told {you/s/he} . . .had congestive heart failure?	
-- MCD180c How old {were you/was SP} when {you were/s/he was} first told {you/s/he} . . .had coronary heart disease?	
-- MCD180e How old {were you/was SP} when {you were/s/he was} first told {you/s/he} . . .had a heart attack (also called myocardial infarction)?	

-- Prescribed Medications   RXQ_RX_J
-- RXDCOUNT The number of prescription medicines reported.	

-- Hospitalization Utilization Acccess to Care 
-- HUQ090 During the past 12 months, that is since {DISPLAY CURRENT MONTH} of {DISPLAY LAST YEAR}, {have you/has SP} seen or talked to a mental health professional such as a psychologist, psychiatrist, psychiatric nurse or clinical social worker about {your/his/her} health?	
-- HUQ071 {During the past 12 months, were you/{was} SP} a patient in a hospital overnight? Do not include an overnight stay in the emergency room.	
-- HUQ020 Compared with 12 months ago, would you say {your/SP's} health is now . . .	 



-- Lets start with some basic activites; 
-- How do we look at a table? // two primary commands: 
-- select 
-- from 

select * from us_population_2.demo_j; 
--
-- now do the same thing inside of the terminal 

select COUNT(*) from us_population_2.demo_j;

-- looks like there is alot - don't want to overload the system
-- so the 2nd most important variable for us is to use LIMIT 

select * from us_population_2.demo_j limit 5;

-- how do we then just look at the list of variable names? 
describe us_population_2.demo_j;


-- alright, now that we have a list of the variable names, 
-- how do we just return and query a subset? 

select SEQN from us_population_2.demo_j;

-- how about if we want three? 
select SEQN, RIDSTATR, RIDEXAGM  from us_population_2.demo_j;


-- what if we use quotes? 
select 'SEQN', 'RIDSTATR', 'RIDEXAGM'  from us_population_2.demo_j;


-- what if we want to rename fields to make them more human readible? 
select SEQN as 'key_id', RIDEXAGM as "var1", RIDRETH3 as 'var2' from us_population_2.demo_j limit 10;


-- what if we want to move certain things to new lines? 
select SEQN as 'key_id', RIDEXAGM as "var1", RIDRETH3 as 'var2' 
from us_population_2.demo_j 
limit 10;


-- what if we want to do some indentation? 
select 
    SEQN as 'key_id', 
    RIDEXAGM as "var1", 
    RIDRETH3 as 'var2' 
from 
    us_population_2.demo_j
limit 10;


-- DEMOGRAPHICS  DEMO_J // https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Demographics&CycleBeginYear=2017
-- SEQN
-- RIAGENDR Gender of the participant.
-- RIDAGEMN Age in months of the participant at the time of screening. Reported for persons aged 24 months or younger at the time of exam (or screening if not examined).	
-- RIDAGEYR Age in years of the participant at the time of screening. Individuals 80 and over are topcoded at 80 years of age.	
-- INDFMIN2 Total family income (reported as a range value in dollars)	

-- lets bring in those and re-code them to something more human readible 
select 
SEQN, 
RIAGENDR,
RIDAGEMN,
RIDAGEYR,
INDFMIN2 from us_population_2.demo_j limit 10; 


-- lets bring in those and re-code them to something more human readible 
select 
SEQN as 'patient_id',
RIAGENDR as 'gender',
RIDAGEMN as 'age_months',
RIDAGEYR as 'age_years',
INDFMIN2 as 'family_income' 
from us_population_2.demo_j
limit 10; 


-- how would we go about see the variety of responses for gender? 
select 
    RIAGENDR as 'gender',
    COUNT(*) 
from us_population_2.demo_j
group by gender;

-- how about if we were to transcode those values into something 
-- more meaningul? 

SELECT 
    SEQN as 'patient_id',
    IF(RIAGENDR='1','Female', 'Male') AS 'Gender' 
from us_population_2.demo_j
limit 10;


-- now how about if we were to group them together like we did previously? 
-- here is an example of how we slowly build up the complexity of our 
-- SQL queries by time 

SELECT 
    IF(RIAGENDR='1','Female', 'Male') AS 'gender' ,
    COUNT(*) 
from us_population_2.demo_j
group by gender;


--- now, how bout we explore age 
---
SELECT 
SEQN as 'patient_id',
RIDAGEYR as 'age_years'
from us_population_2.demo_j
limit 10; 

-- looks like there could be some numbers that are not rounded, 
-- how would we round them? 
SELECT 
SEQN as 'patient_id',
RIDAGEYR as 'age_years',
ROUND(RIDAGEYR) as 'age_years_round'
from us_population_2.demo_j
limit 10; 

-- this is just one of many MATHETICAL OPERATIONS 
-- see slide of presentation // Operators - mathetical functions 
-- https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html

-- now lets look at some operators that focus on COMPARISON 
-- https://dev.mysql.com/doc/refman/8.0/en/comparison-operators.html


-- BELOW WE ARE GOING TO NOW USE THE WHERE command for our COMPARISON 
-- operators: 
SELECT 
SEQN as 'patient_id',
RIDAGEYR as 'age_years',
ROUND(RIDAGEYR) as 'age_years_round'
from us_population_2.demo_j
WHERE RIDAGEYR <= 21
limit 10; 


-- now lets add some additional conditionality to that filter, 
-- so we will be looking at that age group between two values:
-- the values being between 20 and 21 

SELECT 
SEQN as 'patient_id',
RIDAGEYR as 'age_years',
ROUND(RIDAGEYR) as 'age_years_round'
from us_population_2.demo_j
WHERE RIDAGEYR <= 21 && RIDAGEYR >= 20
limit 10; 


-- now, how about we also add in gender? 
-- lets say that we want to use that same command, but 
-- only look at a sub-sample of females: 

SELECT 
SEQN as 'patient_id',
RIDAGEYR as 'age_years',
ROUND(RIDAGEYR) as 'age_years_round',
RIAGENDR as 'gender'
from us_population_2.demo_j
WHERE RIDAGEYR <= 21 && RIDAGEYR >= 20 && RIAGENDR = 1
limit 10; 


-- now lets modify and just look at males: 
SELECT 
SEQN as 'patient_id',
RIDAGEYR as 'age_years',
ROUND(RIDAGEYR) as 'age_years_round',
RIAGENDR as 'gender'
from us_population_2.demo_j
WHERE RIDAGEYR <= 21 && RIDAGEYR >= 20 && RIAGENDR = 2
limit 10; 



-- now lets modify and just look at males, we can do the same
-- thing but by using the != operator: 
SELECT 
SEQN as 'patient_id',
RIDAGEYR as 'age_years',
ROUND(RIDAGEYR) as 'age_years_round',
RIAGENDR as 'gender'
from us_population_2.demo_j
WHERE RIDAGEYR <= 21 && RIDAGEYR >= 20 && RIAGENDR != 1
limit 10; 


-- now, lets GROUP BY gender, with our filter of the age 
-- range between 13-21 and see how that looks 
SELECT 
RIAGENDR as 'gender',
COUNT(*)
from us_population_2.demo_j
WHERE RIDAGEYR <= 21 && RIDAGEYR >=13 
GROUP BY RIAGENDR
limit 10; 



-- now lets imagine we would want to save this table, 
-- so we can look back at it later - how would we do that? 
-- using the 'create view' functionality 
CREATE VIEW temptab1 AS  
SELECT 
RIAGENDR as 'gender',
COUNT(*)
from us_population_2.demo_j
WHERE RIDAGEYR <= 21 && RIDAGEYR >=13 
GROUP BY RIAGENDR
limit 10; 


-- now if we want to just recall that view later, we can perform: 
select * from temptab1 limit 10;



-- alright, now because we have different tables - how would we go 
-- about joing them ? 
-- well looking at the tables, and their data dictionaries, we know 
-- that the primary key that links them together is SEQN

-- so lets take a subsample of our demographics table, and select 
-- some stuff that matches with a specific SEQN number 93705 
-- 

select * 
from us_population_2.demo_j 
where SEQN = 93705;

select * 
from us_population_2.paq_j 
where SEQN = 93705;


-- one way we could do is is by using JOIN 
select * from us_population_2.demo_j, us_population_2.paq_j
limit 10;
-- not accureate potentially 

select 
    d.SEQN as d_id, 
    p.SEQN as p_id 
from demo_j d, paq_j p
limit 5; 


----- WE NEED TO DO A MERGE OF THESE TABLES TOGETHER 
-----
select 
    d.SEQN as d_id, 
    p.SEQN as p_id 
from demo_j d, paq_j p
where p.SEQN=d.SEQN
limit 5; 


-- same thing using the join statement: 
select 
    d.SEQN as d_id, 
    p.SEQN as p_id 
from demo_j d
join paq_j p
where p.SEQN=d.SEQN
limit 5;



----- lets now add in some more fields: 
select 
    d.SEQN as d_id, 
    d.RIDAGEYR as d_age,
    p.SEQN as p_id 
from demo_j d
join paq_j p
where p.SEQN=d.SEQN
limit 5; 


----- lets now add in some more fields: ADD IN ANOTHER FUNCTION 
select 
    d.SEQN as d_id, 
    d.RIDAGEYR as d_age,
    p.SEQN as p_id 
from demo_j d
join paq_j p
where p.SEQN=d.SEQN && d.RIDAGEYR < 60
limit 5; 