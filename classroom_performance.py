def calculate_average_marks(students):
    average_marks = {}
    
    for student, marks in students.items():
        average_marks[student] = round(sum(marks) / len(marks),2)
    return average_marks

def identify_top_performer(average_marks):
    top_student = max(average_marks, key=average_marks.get)
    return top_student

students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}

average_marks = calculate_average_marks(students)
top_performer = identify_top_performer(average_marks)

print("Average Marks:", average_marks)
print("Top Performer:", top_performer)
