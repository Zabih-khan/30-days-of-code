n = int(input("How many student want to calculate average."))
dic = {}
for i in range(n):
    name, *line = input("Enter Name and All Marks of the student with space.").strip().split()
    score = list(map(float,line))
    dic[name] = score
T_name = input("Target name:")
marks = dic[T_name]
x = sum(marks)/len(marks)
print(x)