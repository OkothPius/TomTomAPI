import requests
import matplotlib.pyplot as plt

plt.style.use('seaborn')


API_KEY = 'a2cvZL5Hn6VUHWOBOJYMKnqD3122VWnY'
base_url = 'api.tomtom.com'
param_fields = '{incidents{type,geometry{type,coordinates},properties{id,iconCategory,magnitudeOfDelay,events{description,code,iconCategory},startTime,endTime,from,to,length,delay,roadNumbers,timeValidity,aci{probabilityOfOccurrence,numberOfReports,lastReportTime},tmc{countryCode,tableNumber,tableVersion,direction,points{location,offset}}}}}'

api_url = f'https://{base_url}/traffic/services/5/incidentDetails?key={API_KEY}&bbox=4.8854592519716675,52.36934334773164,4.897883244144765,52.37496348620152&fields={param_fields}&language=en-GB&t=1633435700&categoryFilter=0,1,2,3,4,5,6,7,8,9,10,11,14&timeValidityFilter=present'

data = requests.get(api_url).json()
# print(data)

traffic_data = data['incidents'][0]
traffic_property = traffic_data['properties']

startTime = traffic_property['startTime']
endTime = traffic_property['endTime']
delay = traffic_property['delay']

print(startTime)
print(endTime)
print(delay)

param_fields = '{incidents{type,geometry{type,coordinates},properties{id,iconCategory,magnitudeOfDelay,startTime,endTime,from,to,length,delay,timeValidity}}}'


# print(traffic_property)


# traffic_level, traffic_time = [],[]
# for item in traffic_data:
#     traffic_level.append(item[3])
#     traffic_time.append(item[2])
#
# traffic_level
# traffic_time

# plt.barh(traffic_level, traffic_time)

# plt.title('Traffic Levels from Hartenstraat to Raadhuisstraat')
# plt.xlabel('Time in the last 24hrs')

# plt.tight_layout()
# plt.show()
