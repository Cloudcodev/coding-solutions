def count_substring(string, sub_string):
    count = 0
    sub_len = len(sub_string)
    
    # Iterate through the string, stopping early enough to avoid index out of bounds
    for i in range(len(string) - sub_len + 1):
        # Slice the main string and check if it matches the substring
        if string[i:i+sub_len] == sub_string:
            count += 1
    return count

