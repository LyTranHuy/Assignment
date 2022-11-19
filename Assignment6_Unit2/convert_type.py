import os
import json
import csv


# Folder Path
path = "D:\\TestCode\\Assignment\\Assignment6_Unit2"
  
# Change the directory
os.chdir(path)
  
"""# iterate through all file
for file in os.listdir():
    # Check whether file is in json format or not
    if file.endswith(".json"):
        file_path = f"{path}\{file}"
        file_name_csv = file.replace('json', 'csv')
        print(file_name_csv)
    # Convert json to csv
        with open(file_path) as json_file:
            data = json.load(json_file)

        data_file = open(file_name_csv,'w')

        csv_writer = csv.writer(data_file)
        count = 0
        for item in data:
            if count == 0:
                header = data.keys()
                csv_writer.writerow(header)
                csv_writer.writerow(data.values())
                count += 1
        data_file.close()"""

for file in os.listdir():
    # Check whether file is in csv format or not
    if file.endswith(".csv"):
        file_path = f"{path}\{file}"
        file_name_json = file.replace('csv', 'json')

        # Convert csv to json 

        jsonArray=[]

        #read csv file
        with open(file_path) as csvfile:
            #load csv file using csv library's dictreader method
            csvRead = csv.DictReader(csvfile)

            #convert row csv row to python dictionary
            for row in csvRead:
                jsonArray.append(row)

        #convert python jsonarray to json string and write in into a file
        with open(file_name_json,'w') as jsonfile:
            jsonString = json.dumps(jsonArray, indent=4)
            jsonfile.write(jsonString)