def student_data(data):
    
    for i in data:
        total=sum(i["marks"])
        percent=round(total/len(i["marks"]),2)
        i["total"]=total
        i["percentage"]=percent
        return data
s=student_data([
    {"name":"Alice","marks":[98,56,78,49,86]},
    {"name":"Bob","marks":[93,58,73,46,88]},
    {"name":"Charly","marks":[90,57,74,47,65]},
    {"name":"David","marks":[96,66,88,49,95]},
    {"name":"Ethan","marks":[97,76,68,44,55]}
    ])
print(s)