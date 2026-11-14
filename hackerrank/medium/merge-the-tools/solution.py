def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i + k]
        print("".join(dict.fromkeys(substring)))

