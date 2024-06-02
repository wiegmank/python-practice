contacts = {
    'number':4,
    'students':
        [
            {'name' : "Charlie Dog", 'email' : "charlie@dog.com"},
            {'name' : "Maya Dog", 'email' : "maya@dog.com"},
            {'name' : "Auggie Dog", 'email' : "auggie@dog.com"},
            {'name' : "Kevin Human", 'email' : "kevin@human.com"},
        ]
}

print("Student emails:")
for student in contacts['students']:
    print(student['email'])