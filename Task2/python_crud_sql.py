import sqlite3

# Connect to SQLite database or If doesn't exist database, then create database
connect = sqlite3.connect('students_db.db')

# Create a cursor object for executing the SQL commands
cursor_obj = connect.cursor()

# Create the student table on student_db database
cursor_obj.execute('''
    CREATE TABLE IF NOT EXISTS student (
        student_id INTEGER PRIMARY KEY,
        student_name TEXT,
        dept TEXT,
        cgpa REAL,
        semester TEXT
    )
''')

# Create to CRUD operation all function on student_db database
# Add a student on database
def add_student(student_name, dept, cgpa, semester):
    cursor_obj.execute('''
        INSERT INTO student (student_name, dept, cgpa, semester)
        VALUES (?, ?, ?, ?)
    ''', (student_name, dept, cgpa, semester))
    connect.commit()
    print("("+student_name+') Student details added successfully.')

# Retrieve all students from database
def retrieve_students():
    cursor_obj.execute('SELECT * FROM student')
    students = cursor_obj.fetchall()
    return students

# Update a student's details on database
def update_student(student_id, student_name, dept, cgpa, semester):
    cursor_obj.execute('''
        UPDATE student
        SET student_name = ?, dept = ?, cgpa = ?, semester = ?
        WHERE student_id = ?
    ''', (student_name, dept, cgpa, semester, student_id))
    connect.commit()
    print(str(student_id)+' Student ID details updated successfully.')

# Delete a student from database
def delete_student(student_id):
    cursor_obj.execute('DELETE FROM student WHERE student_id = ?', (student_id,))
    connect.commit()
    print(str(student_id)+' Student ID deleted successfully.')



# Now use all of CRUD operation function
# Add 6 student on database
print("==================== Student Added ==========================")
add_student('Shamim Khaled', 'CSE', 3.03, 'Spring2023')
add_student('Rohan', 'BBA', 3.41, 'Fall2022')
add_student('Niloy', 'CSE', 3.87, 'Summer2022')
add_student('Sakif', 'CSE', 3.61, 'Spring2022')
add_student('Tanvir', 'BBA', 3.23, 'Spring2023')
add_student('Uzzal', 'IBA', 3.63, 'Fall2022')
print(" ")


# Retrieve all students from database
print("==================== Retrieve All Students ==========================")
students = retrieve_students()
for student in students:
    print(student)
print(" ")


# Update a student's details on database
print("==================== Updated Student Details ==========================")
update_student(1, 'Shamim Khaled', 'CSE', 3.9, 'Spring2023')
update_student(2, 'Abir Rohan', 'CSE', 3.41, 'Fall2022')
print(" ")


# Delete the student from database
print("==================== All Students After Deletion ==========================")
delete_student(3)
delete_student(4)
print(" ")
print('All users after deletion:')
students = retrieve_students()
for student in students:
    print(student)


# Close the database connection
connect.close()



