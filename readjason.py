import json

with open("3412.9_296.4.json", "r") as f:
	json_str = f.read()
print(json_str)
your_dict = json.loads(json_str)
shapes = your_dict["shapes"]
length = len(shapes)

for label in range(length):
	shapes[label]["label"] = "building" + str(label+1)
print(shapes)
#your_dict_json = json.dumps(your_dict,indent=1)
#print(your_dict_json)
#print(type(your_dict_json))
with open("3412.9_296.4.json", "w", encoding="UTF-8") as f1:
	json.dump(your_dict,f1, ensure_ascii=False,indent = 1)
