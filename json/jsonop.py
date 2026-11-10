import json
jsonuser="""
{
    "name":"pawni",
    "phone":8595870667,
    "skills":["python","n8n","agents"],
    "address":{
        "city":"delhi",
        "pin":112
    }
}
"""
#print(jsonuser)
#print(type(jsonuser))
userdict=json.loads(jsonuser)
print(userdict)
print(type(userdict))
print(userdict["name"])
print("skills" in userdict)

todo={
    "title":"hi,everyone,yohoo",
    "iscompleted":False

}
jsontodo=json.dumps(todo)
print(jsontodo)
print(type(jsontodo))