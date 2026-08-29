

# Complete the solve function below.
def solve(s):
    # Split the string by explicit spaces to preserve multiple spaces
    words = s.split(' ')
    
    # Capitalize each word and join them back with spaces
    capitalized_words = [word.capitalize() for word in words]
    
    return ' '.join(capitalized_words)
