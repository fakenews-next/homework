students = {}
f = open ('C:/Users/12579/Desktop/sb.txt','r')
lines = f.readlines()
print(lines)
for line in lines:
    tmp1 = line.split(',')
    print(tmp1)
    xuehao = tmp1[0]
    xinming = tmp[1]
    students[xuehao] = xinming
print(students)
f.close()