


def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        # Format each integer i into decimal, octal, hex (uppercase), and binary
        dec_val = str(i)
        oct_val = oct(i)[2:]
        hex_val = hex(i)[2:].upper()
        bin_val = bin(i)[2:]
        
        # Print each value space-padded to match the binary width
        print(f"{dec_val:>{width}} {oct_val:>{width}} {hex_val:>{width}} {bin_val:>{width}}")

