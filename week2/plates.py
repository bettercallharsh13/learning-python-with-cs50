def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) >6:
        return False
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    found_number = False
    for c in s:
        if not c.isalnum():
            return False
        if c.isdigit():
            if not found_number:
                if c == "0":
                    return False
                found_number = True
        elif found_number:
            return False

    return True




main()
