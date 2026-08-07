if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # Extract the marks for the queried student
    query_scores = student_marks[query_name]
    
    # Calculate the average
    average_score = sum(query_scores) / len(query_scores)
    
    # Print the result formatted to 2 decimal places
    print(f"{average_score:.2f}")
    
