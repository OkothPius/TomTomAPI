import requests
import matplotlib.pyplot as plt

Your_Api_Key = 'a2cvZL5Hn6VUHWOBOJYMKnqD3122VWnY'
site_url = 'https://api.tomtom.com/traffic/services/5/incidentDetails?key=a2cvZL5Hn6VUHWOBOJYMKnqD3122VWnY&bbox=4.8854592519716675,52.36934334773164,4.897883244144765,52.37496348620152'
response = requests.get(site_url)
response_json = response.json()


print(response_json['incidents'][0])


site_url = 'https://api.tomtom.com/traffic/services/5/incidentDetails?key=Your_Api_Key&bbox=4.8854592519716675,52.36934334773164,4.897883244144765,\
52.37496348620152&fields={incidents{type,geometry{type,coordinates},properties{id,iconCategory,magnitudeOfDelay,events{description,code,iconCategory},\
startTime,endTime,from,to,length,delay,roadNumbers,timeValidity,aci{probabilityOfOccurrence,numberOfReports,lastReportTime},tmc{countryCode,tableNumber,\
tableVersion,direction,points{location,offset}}}}}&language=en-GB&t=1111&categoryFilter=6&timeValidityFilter=present'

    {
      "incidents" : [
        {
          "type" : "Feature",
          "properties" : {
            "id":"4819f7d0a15db3d9b0c3cd9203be7ba5",
            "iconCategory" : 8,
            "magnitudeOfDelay" : 4,
            "startTime" : "2021-02-02T15:37:00Z",
            "endTime" : "2021-04-30T22:00:00Z",
            "from" : "Paleisstraat",
            "to" : "Rosmarijnsteeg",
            "length" : 238.553,
            "delay" : 0,
            "roadNumbers" : [],
            "timeValidity" : "present",
            "events" : [
              {
                "code" : 401,
                "description" : "Closed",
                "iconCategory" : 8
              }
            ],
            "aci" : null,
            "tmc" : null
          },
          "geometry" : {
            "type" : "LineString",
            "coordinates" : [[4.8905266414,52.3725919469],[4.8905306647,52.3725356560],[4.8905360291,52.3724806443],[4.8905387113,52.3724028603],[4.8905440757,52.3723505607],[4.8905467579,52.3722754886],[4.8905574868,52.3721722195],[4.8905762622,52.3719066767],[4.8905963788,52.3716639050],[4.8905936966,52.3715244540],[4.8905749211,52.3714278871],[4.8905440757,52.3713393544],[4.8905065248,52.3712669418],[4.8904555628,52.3711703743],[4.8904166708,52.3711100387],[4.8903268168,52.3709759593],[4.8901725898,52.3707653720],[4.8900062928,52.3705816510],[4.8899472842,52.3705320104]]
          }
        }
      ]
    }
