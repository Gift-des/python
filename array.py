
courses = ["MIT", "CyberSecurity", "Datascience"]

print(courses)

# Accessing an element in an array
print(courses[0])

# Adding a new element in an array
courses.append("Android Development")
print(courses)

# Deleting an element in an array
courses.remove("CyberSecurity")
print(courses)

# Looping through an array
for course in courses:
    print(course)
