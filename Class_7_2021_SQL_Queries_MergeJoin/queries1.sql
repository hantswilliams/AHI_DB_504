"""

SELECT <select_list>
FROM Table_A A
LEFT JOIN Table_B B
ON A.Key = B.Key

"""


"""
Simple expample - left join 

Create a table that show us encounter information combined with a patients ethnicity 

"""

SELECT A.PATIENT, A.DESCRIPTION, B.Id, B.ETHNICITY
FROM synthea.encounters A
LEFT JOIN  synthea.patients B
ON A.PATIENT = B.Id
LIMIT 10; 


"""
Question: Do males or females report pain levels greater then 5? 

Observation table: 
- Code = 72514-3
- Description = Pain severity - 0-10 verbal numeric rating [Score] - Reported
- VALUE > 5.0 
- PATIENT 

patients table: 
- Id
- Gender

"""


" Part 1 Response" 

SELECT patients.Id, patients.GENDER, observations.PATIENT, observations.CODE, observations.DESCRIPTION, observations.VALUE
FROM synthea.patients
LEFT JOIN synthea.observations
ON patients.Id = observations.PATIENT
WHERE observations.VALUE > 5.0 AND observations.Code = "72514-3"
LIMIT 10;


" Part 2 Modification "

SELECT patients.GENDER, count(*)
FROM synthea.patients
LEFT JOIN synthea.observations
ON patients.Id = observations.PATIENT
WHERE observations.VALUE > 5.0 AND observations.Code = "72514-3"
GROUP BY patients.GENDER
LIMIT 10;



" Part 3 Modification "
SELECT patients.GENDER, count(*) as 'count',  observations.VALUE
FROM synthea.patients
LEFT JOIN synthea.observations
ON patients.Id = observations.PATIENT
WHERE observations.VALUE > 5.0 AND observations.Code = "72514-3"
GROUP BY patients.GENDER, observations.VALUE;




" PATIENTS THAT ARE M, WHAT ARE THE TOTAL NUMBER OF ENCOUNTERS, 
AND OBSERVATIONAL DATA PER ENCOUNTER DO THEY HAVE....

- For males: 
    - Total number of encounters per person 
    - Total number of observerations per encounter per person 

"


"Just getting a basic query working for this...."
SELECT patients.Id, patients.GENDER, encounters.PATIENT, encounters.Id, encounters.ENCOUNTERCLASS
	FROM synthea.patients
	LEFT JOIN synthea.encounters
	ON patients.Id = encounters.PATIENT
	WHERE patients.GENDER = "M" 
	LIMIT 10;

   

"Now lets dial things back...Total count of Encounters per Person"
SELECT encounters.PATIENT, count(*)
	FROM synthea.patients
	LEFT JOIN synthea.encounters
	ON patients.Id = encounters.PATIENT
	WHERE patients.GENDER = "M" 
    GROUP BY encounters.PATIENT
	LIMIT 100;



"Encounters Table by ID count"
SELECT patients.Id, count(encounters.Id) as encounterCount 
	FROM synthea.patients
	LEFT JOIN synthea.encounters
	ON patients.Id = encounters.PATIENT
	WHERE patients.GENDER = "M" 
    GROUP BY patients.Id


"Observations by ID count"
SELECT patients.Id, count(observations.CODE) as observationCodeCount 
	FROM synthea.patients
	LEFT JOIN synthea.observations
	ON patients.Id = observations.PATIENT
	WHERE patients.GENDER = "M" 
    GROUP BY patients.Id


"Then we would want to join these two above tables together? E.g., "


CREATE VIEW encounterView2 AS
SELECT encounters.PATIENT, count(*)
	FROM synthea.patients
	LEFT JOIN synthea.encounters
	ON patients.Id = encounters.PATIENT
	WHERE patients.GENDER = "M" 
    GROUP BY encounters.PATIENT


CREATE VIEW observationView1 AS
SELECT patients.Id, count(observations.CODE) as observationCodeCount 
	FROM synthea.patients
	LEFT JOIN synthea.observations
	ON patients.Id = observations.PATIENT
	WHERE patients.GENDER = "M" 
    GROUP BY patients.Id



"then can do a join of these two new views...."

select observationView1.Id, observationView1.observationCodeCount, encounterView1.encounterCount
from observationView1
left join encounterView1 
ON observationView1.Id = encounterView1.Id





#### doing some stuff with sqlalchemy: 

MYSQL_HOSTNAME = 'inserthere'
MYSQL_USER = 'inserthere'
MYSQL_PASSWORD = 'inserthere'
MYSQL_DATABASE = 'ahi'
connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}:3305/{MYSQL_DATABASE}'
engine = create_engine(connection_string)


-- What we want: 
--  still want a pain score > 5 in addition 
-- total count of observations per person (do not want to exclude any, we want to get a total count of all observations)  
-- total count of encounters per person  
-- operationalize: 
	-- single table
		-- each row = distinct person 
        -- 1 column == total count of observations across all encounters - DONE 
        -- 1 column == total count of encounters for that individual 
        
        -- id	observationtotalCount	encounterTotalCount 
        -- 1		300						5
        -- 2 		150						2 
        
	-- ASK: create two separate queries; two separate select statements; 
    
-- Query 1 

-- CREATE VIEW encounterspain AS
-- SELECT count(*) as encountersCount, encounters.PATIENT
-- FROM synthea.encounters
-- LEFT JOIN synthea.observations
-- ON observations.PATIENT = encounters.PATIENT
-- WHERE observations.code = '72514-3' and observations.value > 5.0 
-- GROUP BY observations.PATIENT;


-- obversationspain -> count -> observationsCOUNT 
-- encounterspain - encountersCount
-- key we can merge them together on: PATIENT 

select *
from obversationspain
inner join encounterspain
on obversationspain.PATIENT = encounterspain.PATIENT

-- ORDERING FOR COMMANDS: 
SELECT ....
FROM...
JOIN ... ON  -- optional 
WHERE... -- optional 
GROUP BY.... -- optional 
ORDER BY....-- optional  