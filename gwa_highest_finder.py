#reads the file and then print it 
with open("student_gwa.txt") as gwaStudents:
    for line in gwaStudents:
        name, gwa = line.strip()
#conditions for gwa

for line in gwaStudents:
    if gwa <  bestGwa:
        bestGwa = gwa


