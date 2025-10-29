def calculate_average_marks(students_data):
    averages = {}
    for name, marks in students_data.items():
        avg = sum(marks) / len(marks)

        
        if avg % 1 == 0:
            averages[name] = int(avg)
        else:
            averages[name] = round(avg, 2)

    return averages

def find_top_performer(averages):
    return max(averages, key=averages.get)

students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}

average_marks = calculate_average_marks(students)
top_student = find_top_performer(average_marks)

print("Average Marks:", average_marks)
print("Top Performer:", top_student)