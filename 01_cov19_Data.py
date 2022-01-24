import requests
import json
from datetime import datetime
from pprint import pprint

# Getting the current date and time
dt = datetime.now()

# getting the timestamp
ts = datetime.timestamp(dt)
print(ts)
url = 'https://www.mygov.in/sites/default/files/covid/covid_state_counts_ver1.json?timestamp='+str(round(ts,0))
# res = requests.get(url).text


# writing the file to json
state_data = json.loads(requests.get(url).text)
out_file = open("myfile.json", "w")
json.dump(state_data, out_file, indent=6)
out_file.close()

state_name = []
Total_Confirmed_cases =[]
activ_cases = []
discharged_cases =[]
death = []

# difference values
diff_confirmed_covid_cases =[]
diff_cured_discharged =[]
diff_death =[]
diff_active_covid_cases =[]

# for key, data in state_data.items():
#     print(key," >>>" ,data)
# Name of state
for value in state_data['Name of State / UT'].values():
    state_name.append(value)
# Total Confirmed Case
for value in state_data['Total Confirmed cases'].values():
    # print(value)
    Total_Confirmed_cases.append(value)
# activ_cases
for value in state_data['Active'].values():
    activ_cases.append(value)
# discharged_cases
for value in state_data['Cured/Discharged/Migrated'].values():
    discharged_cases.append(value)
# death
for value in state_data['Death'].values():
    death.append(value)

# Change cases
for value in state_data['diff_confirmed_covid_cases'].value():
    diff_confirmed_covid_cases.append(value)

for value in state_data['diff_cured_discharged'].value():
    diff_cured_discharged.append(value)

for value in state_data['diff_death'].value():
    diff_death.append(value)

for value in state_data['diff_active_covid_cases'].value():
    diff_active_covid_cases.append(value)




url_mh = 'https://www.covid19maharashtragov.in/mh-covid/dbd-cases-file?_by=District&_by=Date'