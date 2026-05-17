import json

with open("./moderate.json") as f:
    data = json.load(f)
    print(json.dumps(data, indent=4))
    print(type(data))

    print(json.dumps(data["data"], indent=4))
    data_obj = data["data"]
    print("data_obj type: ", type(data_obj))
    print("size of data lists: ", len(data_obj))

    for dt in data_obj:
        print(json.dumps(dt, indent=4))
        print("ID: ", dt["id"])
        dt['data']['Price']= float(dt['data']["Price"])+10.0



    # for student in data:
    #     print(f"Student Name: {student.get('name')} and Age is: {student.get('age')}")
    #     if student.get("name")=="Bob":
    #         student["age"]=18
    #         print("----------------")
    #         print(json.dumps(data, indent=4))
    #
    #
    json.dump(data, open("./moderate_updated.json", "w"), indent=4)
    #
    #
