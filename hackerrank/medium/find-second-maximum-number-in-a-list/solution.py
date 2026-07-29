if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # Convert to a set to remove duplicates, then to a list to sort it
    unique_scores = list(set(arr))
    
    # Sort the unique scores in ascending order
    unique_scores.sort()
    
    # The runner-up is the second to last element
    print(unique_scores[-2])
