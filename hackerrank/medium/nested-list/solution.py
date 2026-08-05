if __name__ == '__main__':
    # Initialize a list to store student records and a set to store unique scores
    records = []
    unique_scores = set()
    
    # Read the input
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        unique_scores.add(score)
        
    # Sort the unique scores to find the second lowest
    # The second element (index 1) will be the second lowest grade
    second_lowest_score = sorted(list(unique_scores))[1]
    
    # Filter the names of the students who have the second lowest score
    target_students = [name for name, score in records if score == second_lowest_score]
    
    # Sort the names alphabetically and print them
    for student in sorted(target_students):
        print(student)
