if __name__ == '__main__':
    n = int(input("How many student want to calculate average:"))
    student_marks = {}
    for _ in range(n):
        #This line Take name and marks of the student
        name, *line = input("Enter Name:").split()
        #This lline convert string into float number
        scores = list(map(float, line))
        #Append the name and scores in dictionary
        student_marks[name] = scores
    query_name = input("Target Name:")
    marks=student_marks[query_name]
    #Here format function is used for convert the averge into two decimal:
    print("Average is :",format(sum(marks)/3,'.2f'))
