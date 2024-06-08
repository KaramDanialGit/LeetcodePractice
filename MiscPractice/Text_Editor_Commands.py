def solution(operations):
    cursor_position = 0
    selected_text = ""
    clipboard = []
    plain_text = ""

    for task in operations:
        operation = task.split()[0]

        if operation == "TYPE":
            content = task.split()[1:]

            if selected_text != "":
                plain_text = plain_text.replace(selected_text, "")
            else:
                for word in content:
                    plain_text = plain_text[cursor_position:] + word + " " + plain_text[:cursor_position]
                print(plain_text)

        if operation == "SELECT":
            start_index = int(task.split()[1])
            end_index = int(task.split()[2])

            selected_text = plain_text[start_index:end_index]

        if operation == "MOVE_CURSOR":
            cursor_position += int(task.split()[1])
            cursor_position = max(cursor_position, 0)
            cursor_position = min(cursor_position, len(plain_text))
            selected_text = ""

        if operation == "COPY":
            clipboard.append(selected_text)

        if operation == "PASTE":
            if len(task.split()) == 1:
                if selected_text != "":
                    plain_text = plain_text.replace(selected_text, clipboard[past_index - 1])
                else:
                    plain_text[:cursor_position] + clipboard[0] + " " + plain_text[cursor_position:]
                continue

            past_index = int(task.split()[1])

            if selected_text != "":
                plain_text = plain_text.replace(selected_text, clipboard[past_index - 1])
            else:
                plain_text[:cursor_position] + clipboard[past_index - 1] + " " + plain_text[cursor_position:]

    print(plain_text)


operations = ["TYPE Great Britain is the capital of London",
             "SELECT 0 12",
             "COPY",
             "SELECT 32 37",
             "COPY",
             "PASTE 2",
             "SELECT 0 12",
             "PASTE",
             "MOVE_CURSOR 32",
             "TYPE !"]

solution(operations)

"""
Expected: "London is the capital of Great Britain!"
"""