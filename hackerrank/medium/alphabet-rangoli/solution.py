import string

def print_rangoli(size):
    # Get lowercase alphabet letters needed for the given size
    alphabet = string.ascii_lowercase
    letters = [alphabet[i] for i in range(size)]
    
    # Generate the pattern lines for the top half (including middle line)
    lines = []
    for i in range(size):
        # Slice letters for current row and create symmetric sequence
        s = letters[size - 1 : i : -1] + letters[i:size]
        # Join characters with hyphens and center with hyphens
        lines.append("-".join(s).center(4 * size - 3, "-"))
    
    # Combine top half reversed (without middle) + middle + top half
    rangoli = lines[::-1] + lines[1:]
    
    # Print the full rangoli pattern
    print("\n".join(rangoli))


