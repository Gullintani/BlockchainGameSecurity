import csv, os, json, gc
gc.disable()
inputCSV = open("./input/name&address2.csv", "r")
reader = csv.reader(inputCSV)

outputCSV = open("./output/game_result2.csv", "w")
writer = csv.writer(outputCSV)
# 

for item in reader:
    output = ""
    output = os.popen("docker run mythril/myth -xo json -a " + item[1], "r")
    if output == None:
        del output
        gc.collect()
        continue
    result_dic = json.loads(output.read())
    if result_dic["issues"] == []:
        writer.writerow([item[0],item[1]])
        print(reader.line_num)
        del output
        del result_dic
        gc.collect()
        continue
    else:
        for issue in result_dic["issues"]:
            row = [item[0], item[1], issue["address"], issue["title"], issue["severity"], issue["function"], issue["sourceMap"], issue["swc-id"], issue["max_gas_used"], issue["min_gas_used"]]
            writer.writerow(row)
        del output
        del result_dic
        del row
        gc.collect()
        print(reader.line_num)
