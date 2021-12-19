def anagram_check(input_string:str, target_string:str) -> bool:
    if len(input_string) != len(target_string):
        return False
    for char in list(input_string):
        if list(target_string).count(char) != list(input_string).count(char):
            return False
    return True


if __name__ == "__main__":
    string1 = "restful"
    string2 = "fluster"
    print(anagram_check("restful","fluster"))
    
