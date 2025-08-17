country = {
    "India" : 1,
    "Australia" : 2,
    "Saudi Arabia" : 3,
}

# Searxh dictionary number for India
print("The country code for India-")
print(country.get("India", "Not Found"))

# Search the number for Saudi Aravbia
print("The country code for Saudi Arabia-")

print(country.get("Saudi Arabia", "Not Found"))