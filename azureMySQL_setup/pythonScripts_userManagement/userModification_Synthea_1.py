import pandas as pd


loadUsers = pd.read_csv('/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_DB_504/azureMySQL_setup/pythonScripts_userManagement/ahi_cohort_2022.csv')

loadUsers['un'] = loadUsers['userEmail'].str.split('@').str[0]
loadUsers['un'] = loadUsers['un'].str.lower()
loadUsers['un'] = loadUsers['un'].str.replace(r'\.', '')
loadUsers['un'] = loadUsers['un'].str.replace(r'\-', '')
loadUsers['pwd'] = loadUsers['un'] + '2021'


userlist = list(loadUsers['un'])


rule = """
GRANT select, show view ON synthea.* TO 'USERNAME'@'%';
FLUSH PRIVILEGES;"""


modedAdd = [] 

for i in range(len(loadUsers)) :
    
  #Create the variables  
  username =  loadUsers.loc[i, "un"] 
 
  #Make a copy of the rule template 
  ruleCopy = rule
    
  #Replace the variables of the rule template with each of the row/from the transformed dataframe
  ruleCopy = ruleCopy.replace("USERNAME", username)
 
  modedAdd.append(ruleCopy)
  
  print('finishedWith: ', username)
  
  del(ruleCopy)
  
    
modedAddString = "\n".join(modedAdd)





#open and delete existing file
open("/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_DB_504/azureMySQL_setup/pythonScripts_userManagement/userModification_synthea_1.sql", 'w').close()
#write the new rules to it
f= open("/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_DB_504/azureMySQL_setup/pythonScripts_userManagement/userModification_synthea_1.sql","w+")
f.write(modedAddString)
f.close() 

