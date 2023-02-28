#!/usr/bin/env python3
'''
                   מבוא למדעי הנתונים: כלים ושיטות
https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/c879b1b9aeb5499cbe13bcd14bc0a5a7/78bc3f2a945a417daff110e2819e2e34/2?activate_block_id=block-v1%3AHIT%2BACD_RFP4_DataScienceIntro_HE%2B2022_1%2Btype%40html%2Bblock%402cb1771459934eb48c669fcca7f63330
https://labs.vocareum.com/main/main.php?m=editor&asnid=537330&stepid=537331&hideNavBar=1
'''
import time
import requests
import json
import pandas as pd


url = "http://api.open-notify.org/iss-now.json" 
def flatten(response_d):
    #Show one row per timestamp and longitude and latitude as columns.
    response_d["latitude"] = response_d["iss_position"]["latitude"]
    response_d["longitude"] = response_d["iss_position"]["longitude"]
    del(response_d["iss_position"])
    return response_d


# Make a get request to get the latest position of the international space station from the
# opennotify api.

response = requests.get(url)

print("requests.get(url) = ",response )
#The content of our previous, successful response:
print("response.content = ",response.content)
content_type = response.headers['content-type']
print("response.headers['content-type'] = ", content_type)#  this is JSON  stored a bytes object
print("response.headers = ",response.headers)




response_j = response.content.decode("utf-8")#decode this byte object, so JSON will be readable.

print(" response.content.decode(utf-8) = ", response_j)
response_d = json.loads(response_j)
print("type(response_d) = ",type(response_d)) #<class 'dict'>
print(" dict ==>   json.loads(response_j) = ",response_d)
print("response_d[ iss_position ] = ", response_d["iss_position"])

df = pd.read_json(response_j)
print('\n\n',df)

# Show one row per timestamp and longitude and latitude as columns.
# we use  'flatten' function
print('\n\none row per timestamp and longitude and latitude as columns\n',flatten(response_d))

'''
Get a couple of positions of the ISS over time and save it as an array:
'''


def pull_position():
    """Retreives the position of the ISS and returns it as a flat dictionary"""
    
    response = requests.get(url)
    response_j = response.content.decode("utf-8")
    response_d = json.loads(response_j)
    flat_response = flatten(response_d)
    return flat_response  

iss_position = []
    
# calls pull_position 10 times with 3 seconds break
for i in range(10):
    flat_response = pull_position()
    iss_position.append(flat_response)
    print("[",i,"]  = ",flat_response)
    time.sleep(1)
    
print("len(iss_position) = ",len(iss_position))

#Now we can convert this into a nice dataframe:
iss_position_df = pd.DataFrame(iss_position)
iss_position_df['timestamp']  = pd.to_datetime(iss_position_df['timestamp'], unit="s")

iss_position_df = iss_position_df.set_index(pd.DatetimeIndex(iss_position_df['timestamp']))
iss_position_df["latitude"] = iss_position_df["latitude"].map(float)
iss_position_df["longitude"] = iss_position_df["longitude"].map(float)
print(iss_position_df )   
    
    
    
    

    