num_people = {}
num_avg1 = {}
num_avg2 = {}
num_fail1 = {}
num_fail2 = {}
head = 0

with open('score.txt', 'r',encoding='utf-8') as f:
    for line in f:
        line = line.replace("\n","")
        if (line != ""):
            lis = line.split(" ")
        if head == 0:
            head = 1
        else:
            if lis[3] not in num_avg1.keys():
                num_people[lis[3]] = 1
                num_avg1[lis[3]] = int(lis[1])
                num_avg2[lis[3]] = int(lis[2])
                num_fail1[lis[3]] = 0
                num_fail2[lis[3]] = 0
            else:
                num_people[lis[3]] += 1
                num_avg1[lis[3]] += int(lis[1])
                num_avg2[lis[3]] += int(lis[2])
            if int(lis[1]) < 60:
                num_fail1[lis[3]] += 1
            if int(lis[2]) < 60:
                num_fail1[lis[3]] += 1
for i in num_people.keys():
    print("{0}年级一共{1}人，专业课1平均成绩为{2}，专业课2平均成绩为{3}，专业课1不及格人数为{4}，专业课2不及格人数为{5}".format(i,num_people[i],
                                                                        num_avg1[i]/num_people[i],num_avg2[i]/num_people[i],num_fail1[i],num_fail2[i]))

