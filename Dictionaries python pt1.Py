student_data = {
    "id1": 
    {"name" : ["Alice"],
     "Class" : ["V"],
     "subjects" : ["Math", "Science", "English"]  
    },

    "id2":
    {"name" : ["Bob"],
     "Class" : ["V"],
     "subjects" : ["Math", "History", "English"]
    },

    "id3":
    {"name" : ["Charlie"],
     "Class" : ["V"],
     "subjects" : ['Math, History', "English"]},
}

result = {}

for key, value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)