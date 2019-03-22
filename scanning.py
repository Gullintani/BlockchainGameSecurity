import csv, os, json

inputCSV = open("./game_contract_address/name&address.csv", "r")
reader = csv.reader(inputCSV)

outputCSV = open("./game_result.csv", "w")
writer = csv.writer(outputCSV)
# 
count = 0
for item in reader:
    output = os.popen("sudo docker run mythril/myth -xo json -a " + item[1], "r")
    result_dic = json.loads(output.read())
    if result_dic["issues"] == []:
        writer.writerow([item[0],item[1]])
        print(reader.line_num)
        continue
    else:
        for issue in result_dic["issues"]:
            row = [item[0], item[1], issue["address"], issue["title"], issue["severity"], issue["function"], issue["sourceMap"], issue["swc-id"], issue["max_gas_used"], issue["min_gas_used"], issue["debug"], issue["description"]]
            writer.writerow(row)
    print(reader.line_num)
