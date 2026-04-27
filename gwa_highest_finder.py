try:
    #reads the file and then print it 
    with open("student_gwa.txt") as gwaStudents:
        line = gwaStudents.readline()
        name, gwa = line.split()
        best_name = name
        best_gwa = float(gwa)
    #loops the each line to check if first line is lower than current line
        for line in gwaStudents:
            name,gwa = line.split()
            gwa = float(gwa)
    #conditions for gwa
            if gwa <  best_gwa:
                best_gwa = gwa
                best_name = name
    #prints result
    print("Top student:", best_name)
    print("Highest GWA:", best_gwa)
except FileExistsError:
    print("File does not exists",
          "make sure your file is named Student_gwa.txt")
    
