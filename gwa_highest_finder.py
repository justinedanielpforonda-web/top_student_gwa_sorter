#reads the file and then print it 
with open("student_gwa.txt") as gwaStudents:
    for line in gwaStudents:
        name, gwa = line.split()
        best_name = name

#conditions for gwa
for line in gwaStudents:
    name,gwa = line.split()
    gwa = float(gwa)

    if gwa <  bestGwa:
        bestGwa = gwa
        best_name = name


