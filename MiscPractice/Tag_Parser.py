'''
Create a function capable of validating a string of commands wrapped in tags
Example "{{ #foo }} this is an example tag {{ /foo }}"          <- Valid
Example "{{ #child }} this is an invalid tag config {{ #child"  <- Invalid
'''


def validate(tag_string):
    stack = []
    index = 0
    open_brackets = ""

    while index < len(tag_string):
        if tag_string[index] == "{":
            while index < len(tag_string) and tag_string[index] != "}":
                if tag_string[index] == "{":
                    open_brackets += "{"
                elif tag_string[index] == "#":
                    prev = index
                    while tag_string[index] != " ":
                        index += 1
                    stack.append(["#", tag_string[prev + 1:index]])
                elif tag_string[index] == "/":
                    stack.pop()
                else:
                    if index > len(tag_string):
                        return False
                index += 1
            close_brackets = tag_string[index:index + 2]

            if len(open_brackets) != len(close_brackets):
                return False
            open_brackets = ""

        index += 1
    return not stack


test_1 = "{{ #foo }} this is an example tag {{ /foo }}"
test_2 = "{{ #child }} this is an invalid tag config {{ /child"
test_3 = "{ #dog }} this is a incomplete {{ /dog }}"

print(validate(test_1))
print(validate(test_2))
print(validate(test_3))
