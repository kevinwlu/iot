def averageGrade(students):
    """
    Calculate the mean of all values.

    Args:
        students: (todo): write your description
    """
    sum=0.0
    for key in students:
        sum=sum+students[key]['grade']
    average=sum/len(students)
    return average
def printRecords(students):
    """
    Prints a list of the values

    Args:
        students: (todo): write your description
    """
    print('There are %d students' % (len(students)))
    i=1
    for key in students:
        print('Student %d:' % (i))
        print('Name: ' + students[key]['name'])
        print('Grade: ' + str(students[key]['grade']))
        i=i+1
