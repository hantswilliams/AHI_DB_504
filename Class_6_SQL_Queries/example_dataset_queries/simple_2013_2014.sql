-- Before getting started, it is good to understand more about the data 
-- Other information can be founder here: https://www.kaggle.com/cdc/national-health-and-nutrition-examination-survey?select=questionnaire.csv

-- Demographic data dictionary can be found here: https://wwwn.cdc.gov/Nchs/Nhanes/Search/variablelist.aspx?Component=Demographics&CycleBeginYear=2013
-- Examination data dictionary can be found here: https://wwwn.cdc.gov/Nchs/Nhanes/Search/variablelist.aspx?Component=Examination&CycleBeginYear=2013
-- Dietary data dictionary can be found here: https://wwwn.cdc.gov/Nchs/Nhanes/Search/variablelist.aspx?Component=Dietary&CycleBeginYear=2013
-- Lab data dictionary can be found here: https://wwwn.cdc.gov/Nchs/Nhanes/Search/variablelist.aspx?Component=Laboratory&CycleBeginYear=2013
-- Questionnaire data dictionary can be found here: https://wwwn.cdc.gov/Nchs/Nhanes/Search/variablelist.aspx?Component=Questionnaire&CycleBeginYear=2013


-- Variables that appear to be of interest from demographics:
-- SEQN // Respondent sequence number.	
-- AIALANGA // Language of the MEC ACASI Interview Instrument	
-- DMDFMSIZ // Total number of people in the Family
-- RIAGENDR // Gender of the participant.	
-- RIDAGEYR // Age in years of the participant at the time of screening. Individuals 80 and over are topcoded at 80 years of age.	
-- INDHHIN2 // Total household income (reported as a range value in dollars)	
-- STATE2K // Census 2000 FIPS State Code	
-- STATE2K // Census 2000 FIPS State Code (2-digit numeric with leading zeros significant)	
-- STATE2KX // Census 2010 FIPS State Code (2-digit numeric with leading zeros significant)	
-- STATE2KX // Census 2010 FIPS State Code (2-digit numeric with leading zeros significant)	
-- UR // Urban/Rural Indicator	



-- Variables that appear to be of interest from examination: 
-- SEQN // Respondent sequence number.	
-- BPXDI1 // Diastolic: Blood pressure (first reading) mm Hg	
-- BPXSY1 // Systolic: Blood pressure (first reading) mm Hg	
-- BMXWT // Weight (kg)	 
-- OHXIMP // Tooth Count: Ever had a tooth replaced with a surgical implant?	 

-- Variables that appear to be of interest from diet: 
-- SEQN // Respondent sequence number.	
-- DR1STY // Did {you/SP} add any salt to {your/her/his} food at the table yesterday? Salt includes ordinary or seasoned salt, lite salt, or a salt substitute.	
-- DR1TNUMF // Total number of foods/beverages reported in the individual foods file	
-- DRD350D // Lobsters eaten during past 30 days	
-- DRQSDIET // Are you currently on any kind of diet, either to lose weight or for some other health-related reason?	 
-- DRQSDT1 // What kind of diet are you on? (Is it a weight loss or low calorie diet: low fat or cholesterol diet; low salt or sodium diet; sugar free or low sugar diet; low fiber diet; high fiber diet; diabetic diet; or another type of diet?)	

-- Variables that appear to be of interest from lab data: 
-- SEQN // Respondent sequence number.	
-- LBXSNASI // Sodium (mmol/L)	
-- LBDHI // HIV antibody test result	 
-- LBXHE1 // Herpes Simplex Virus Type 1	
-- LBXHE2 // Herpes Simplex Virus Type 2	
-- LBDLDL // LDL-cholesterol (mg/dL)	
-- LBDLDLSI // LDL-cholesterol (mmol/L)	

-- Variables that appear to be of interest from questionnaire data: 
-- SXD101 // In your lifetime, with how many men have you had any kind of sex?	 
-- SXD171 // In your lifetime, with how many women have you had any kind of sex?	 
-- SXQ292 // Do you think of yourself as...	
-- SXQ294 // Do you think of yourself as...	
-- CDQ001 // {Have you/Has SP} ever had any pain or discomfort in {your/her/his} chest?	
-- BPD035 // How old {were you/was SP} when {you were/he/she was} first told that {you/he/she} had hypertension or high blood pressure?	
-- BPD058 // How often {did you check your/did SP check his/her} blood pressure at home during the last 12 months?	
-- BPQ020 // HYPERTENSION --> {Have you/Has SP} ever been told by a doctor or other health professional that {you/s/he} had hypertension, also called high blood pressure?	
-- MCQ086 // {Are you/is SP} on a gluten-free diet?	
-- MCQ180a // ARTHRITIS --> How old {were you/was SP} when {you were/s/he was} first told {you/s/he} . . . had arthritis?	
-- MCQ180c // CAD --> How old {were you/was SP} when {you were/s/he was} first told {you/s/he} . . .had coronary heart disease?	
-- MCQ180b // CHF --> How old {were you/was SP} when {you were/s/he was} first told {you/s/he} . . .had congestive heart failure?	
-- MCQ180f // STROKE --> How old {were you/was SP} when {you were/s/he was} first told {you/s/he} . . .had a stroke?	
-- HIQ031A // {Are you/Is SP} covered by private insurance?	 
-- HIQ031AA // No coverage of any type.	
-- HIQ210 // In the past 12 months, was there any time when {you/SP} did not have any health insurance coverage?	
-- HUD080 // How many different times did {you/SP} stay in any hospital overnight or longer {during the past 12 months}? (Do not count total number of nights, just total number of hospital admissions for stays which lasted 1 or more nights.)	
-- HUQ020 // Compared with 12 months ago, would you say {your/SP's} health is now . . .	
-- PAD615 // How much time {do you/does SP} spend doing vigorous-intensity activities at work on a typical day?	
-- DUQ210 // How old were you the first time you used marijuana or hashish?	
-- DUQ240 // Have you ever used cocaine, crack cocaine, heroin, or methamphetamine?	 
-- ALQ130 // In the past 12 months, on those days that {you/SP} drank alcoholic beverages, on the average, how many drinks did {you/he/she} have?	
-- DPQ090 // Over the last 2 weeks, how often have you been bothered by the following problems: Thoughts that you would be better off dead or of hurting yourself in some way?	
-- RXDCOUNT // The number of prescription medicines reported.	
