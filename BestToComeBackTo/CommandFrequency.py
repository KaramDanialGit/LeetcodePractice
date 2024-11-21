"""
A user executes a series of three commands "cp", "ls", and "mv" with additional commands "!<index>" executing the command
at that index again. Return the number of times each command is called in an array of the following order [# cp, # ls, # mv]

Example:
command: [
    ls
    cp
    mv
    mv
    mv
    !1
    !3
    !6
]

output: [1, 2, 4]
"""

def frequency(commands):
    result = [0] * 3
    cmd_map = {"cp":0, "ls":1, "mv":2}

    def resolve(command):
        nonlocal result
        if command[0] == "!":
            index = int(command[1:]) - 1
            resolve(commands[index])
        else:
            result[cmd_map[command]] += 1

    for cmd in commands:
        if cmd[0] != "!":
            result[cmd_map[cmd]] += 1
        else:
            index = int(cmd[1:]) - 1
            print(commands[index])
            resolve(commands[index])

    print(result)
    return result


command = [
    "ls",
    "cp",
    "mv",
    "mv",
    "mv",
    "!1",
    "!3",
    "!6",
]
frequency(command)