if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    marks = []
    for nm, marks in student_marks.items():
        if nm == query_name:
            average = sum(marks) / len(marks)
            print(format(average, ".2f"))


        
