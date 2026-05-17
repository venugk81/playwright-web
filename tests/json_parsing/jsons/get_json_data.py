import json

with open("./simple_students.json") as f:
    data = json.load(f)
    print(json.dumps(data, indent=4))
    print(type(data))
    print("Length is: ", len(data))

    for student in data:
        print(f"Student Name: {student.get('name')} and Age is: {student.get('age')}")
        if student.get("name")=="Bob":
            student["age"]=18
            print("----------------")
            print(json.dumps(data, indent=4))


    json.dump(data, open("./simple_student_new.json", "w"), indent=4)


