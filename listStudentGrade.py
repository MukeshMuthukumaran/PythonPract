def evaluate_grade(marks):
   
    grade = ''
    for mark in marks:
        assert 0 <= mark <= 100, "Invalid mark entry"
    
    average = sum(marks) / len(marks)
    
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B+"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C+"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"
    
    return grade


print("Marks: [90, 95, 100]", "=>", "Grade:", evaluate_grade([90, 95, 100]))
print("Marks: [30, 40, 50]", "=>", "Grade:", evaluate_grade([30, 40, 50]))

try:
    evaluate_grade([110, 80, 90])
except AssertionError as e:
    print("Marks: [110, 80, 90]", "=>", e)
