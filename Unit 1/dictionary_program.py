# dictionary program

d = {"name": "mahi", "age": 18}

print(d)

print("name is:", d["name"])

d["age"] = 19
d["city"] = "nagpur"

print("after update:", d)

d.pop("age")

print("after remove:", d)

d2 = {"course": "ai"}

d.update(d2)

print("final:", d)