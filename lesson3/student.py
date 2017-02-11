def averageGrade(students):
    sum=0.0
    for key in students:
        sum=sum+students[key]['grade']
    average=sum/len(students)
    return average
def printRecords(students):
    print('There are %d students' % (len(students)))
    i=1
    for key in students:
        print('Student %d:' % (i))
        print('Name: ' + students[key]['name'])
        print('Grade: ' + str(students[key]['grade']))
        i=i+1
