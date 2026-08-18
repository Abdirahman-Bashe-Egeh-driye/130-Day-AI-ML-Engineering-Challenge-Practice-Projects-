student = {
    "name" : "ABDI",
    "AGE" :"20",
    "CITY" : "BURAO",
    "MARKS" :"70"
}
print(student["name"])
student.update({"marks": "80"})
print(student.keys())
print(student.values())
print(student.items())
print(student.get("marks"))
print(student.pop("name"))