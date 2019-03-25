import csv, os, json, gc
gc.disable()
inputCSV = open("./input/gamble_name&address.csv", "r")
reader = csv.reader(inputCSV)

outputCSV = open("./output/gamble_result.csv", "w")
writer = csv.writer(outputCSV)
# 
def get_result():
    for item in reader:
        try:
            output = ""
            output = os.popen("docker run mythril/myth -xo json -a " + item[1] + " --execution-timeout 100", "r")
            if output == None:
                del output
                continue
            result_dic = json.loads(output.read())
            if result_dic["issues"] == []:
                writer.writerow([item[0],item[1]])
                print(reader.line_num)
                del output
                del result_dic
                continue
            else:
                for issue in result_dic["issues"]:
                    row = [item[0], item[1], issue["address"], issue["title"], issue["severity"], issue["function"], issue["sourceMap"], issue["swc-id"], issue["max_gas_used"], issue["min_gas_used"]]
                    writer.writerow(row)
                del output
                del result_dic
                del row
                print(reader.line_num)
        except:
            continue

get_result()
