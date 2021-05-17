import json

data = '''
{
  "name" : "Satvik",
  "phone" : {
    "type" : "intl",
    "number" : "7893116684"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
