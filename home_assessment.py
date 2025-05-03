# Create a dictionary for a student with keys: "name", "age", "grade", and "subjects" (list of subjects).

# Add a new key "school" with a value.

# Update the "grade" to a new value.

# Delete the "age" key.

# Print all keys, values, and key-value pairs.


student = {"name":"Sabir","age":19,"grade":8.1,"Subject":"computer science"}

student.update({"University":"MAKAUT"})

del student["age"]

print(student.keys())
print(student.values())
print(student)