"""
"""

def checkAttackTheOpponent(cord_x1, cord_y1, cord_x2, cord_y2):
    if cord_x1 == cord_x2:
        return "Yes"
    elif cord_y1 == cord_y2:
        return "Yes"
    else:
        if abs(cord_x2 - cord_x1) == abs(cord_y2 - cord_y1):
            return "Yes"

    return "No"

def main():
    # input for cord_x1
    cord_x1 = int(input())

    # input for cord_y1
    cord_y1 = int(input())

    # input for cord_x2
    cord_x2 = int(input())

    # input for cord_y2
    cord_y2 = int(input())


    result = checkAttackTheOpponent(cord_x1, cord_y1, cord_x2, cord_y2)
    print(result)

"""
(ab){3}(cd){3} -> abababcdcdcd
(ab(c){3}d){2} -> abcccdabcccd
"""

def expandedString(inputStr):
    # Write your code here

    string_arr = [""] * len(inputStr)
    index = 0

    for char in inputStr:
        if char == "(":
            index += 1
            continue
        if char == ")":
            index -= 1
            continue
        if char.isdigit():
            N = int(char)
            for i in range(N):
                string_arr[index] += string_arr[index + 1]
            string_arr[index + 1] = ""
            continue

        if char != "{" and char != "}":
            string_arr[index] += char

    return string_arr[0]

def main():
    # input for inputStr
    inputStr = str(input())

    result = expandedString(inputStr)
    print(result)

"""

"""

def checkIPValidity(addressIP):
    # Write your code here
    current_chars = ""

    for character in addressIP:
        if character == ".":
            current_int = int(current_chars)
            if current_int < 0 or current_int > 255:
                return "INVALID"
            current_chars = ""
            continue

        current_chars += character

    return "VALID"

def main():
    # input for addressIP
    addressIP = str(input())

    result = checkIPValidity(addressIP)
    print(result)