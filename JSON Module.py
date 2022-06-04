"""
                                            JSON Module
"""
import json
data = '{"Puja": "Eng", "Dora": "Doc"}'
# json.loads() helps to parse object
parsed = json.loads(data)
print(parsed["Puja"])

# json.dumps() helps. sort_keys parameter in json.dumps() helps us to set whether the data will be sorted or not
data2 = {"2": "English", "1": "Physics", "3": False}
data2 = json.dumps(data2, sort_keys=True)
print(data2)

# json.load(): Helps in reading json file and return in form of dictionary
# Opening JSON file
f = open('JSON_File.json', )

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['student_details']:
    print(i)

# Closing file
f.close()