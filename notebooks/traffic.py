import requests
import matplotlib.pyplot as plt

# Your_Api_Key = 'a2cvZL5Hn6VUHWOBOJYMKnqD3122VWnY'
# site_url = 'https://api.tomtom.com/traffic/services/5/incidentDetails?key=a2cvZL5Hn6VUHWOBOJYMKnqD3122VWnY&bbox=4.8854592519716675,52.36934334773164,4.897883244144765,52.37496348620152'
plt.style.use('seaborn')

site_url = 'https://api.tomtom.com/traffic/services/5/incidentDetails?key=a2cvZL5Hn6VUHWOBOJYMKnqD3122VWnY&bbox=4.8854592519716675,52.36934334773164,4.897883244144765,52.37496348620152&fields={incidents{type,geometry{type,coordinates},properties{id,iconCategory,magnitudeOfDelay,events{description,code,iconCategory},startTime,endTime,from,to,length,delay,roadNumbers,timeValidity,aci{probabilityOfOccurrence,numberOfReports,lastReportTime},tmc{countryCode,tableNumber,tableVersion,direction,points{location,offset}}}}}&language=en-GB&t=1633421340&categoryFilter=0,1,2,3,4,5,6,7,8,9,10,11,14&timeValidityFilter=present'

response = requests.get(site_url)
response_json = response.json()


print(response_json)
incident = response_json['incidents'][0]
# print(incident)

property = incident['properties']

traffic_level, traffic_time = [],[]
for item in property:
    traffic_level.append(item['delay'])
    traffic_time.append(item['startTime'])

plt.barh(traffic_level, traffic_time)

plt.title('Traffic Levels from Hartenstraat to Raadhuisstraat')
plt.xlabel('Time in the last 24hrs')

plt.tight_layout()
plt.show()

# print(incident['properties'])
response.status_code
