
# int -> str -> list -> reverse list -> join list as str -> int
def reverse_integer(input:int) -> int:
    return int("".join(list(str(input))[::-1]))

# take 1234 
# first loop 
# output = (1234 % 10) * 10 ^ (len(1234) - 1) == (4) * 10 ^ 3 == 4000
# input = 123.4 == 123 as int
# second loop 
# output = 4000 += (123 % 10) * 10 ^ (len(123) - 1) == (3) * 10 ^ 2 == 300
# etc.. to 4321
def reverse_integer2(input:int) -> int:
    output = 0
    while input >= 1:
        # modulo 10 then multiply by 10 to the length of int - 1 (essentially an order of magnitude smaller)
        output += (input % 10) * 10 ** (len(str(input)) -1)
        # decrease input by an order of magnitude
        input = int(input / 10)
    return output
        
def reverse_integer3(input:int) -> int:
    remainder = 0
    reversed = 0
    while input > 0:
        remainder = input % 10 
        input = int(input/10)
        reversed = reversed * 10 + remainder
    return reversed



if __name__ == "__main__":

    integer = 1234
    print(reverse_integer(integer))
    print(reverse_integer2(integer))
    print(reverse_integer3(integer))
