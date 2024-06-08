import os
import keyboard

current_working_directory = os.getcwd()


def ls_command(commandArr: list[str]) -> None:
    targetPath = commandArr[-1] if commandArr else os.getcwd()
    for file in os.listdir(targetPath):
        print(file)
    return


def mkdir_command(commandArr: list[list], currentDir) -> None:
    for folderName in commandArr:
        if "{" in folderName:
            index = 0
            tmpStr = ""

            while folderName[index] != "{":
                tmpStr += folderName[index]
                index += 1
            index += 1

            if not folderName[index].isdigit():
                break
            numberOfFiles = int(folderName[index])

            for i in range(numberOfFiles):
                os.mkdir(currentDir + "/" + tmpStr + str(i), 0o666)

        elif "," in folderName:
            folders = list(map(str, folderName.split(',')))
            for folder in folders:
                os.mkdir(currentDir + "/" + folder, 0o666)
        else:
            os.mkdir(currentDir + "/" + folderName, 0o666)
    return


while True:
    print(current_working_directory, end="> ")
    try:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):
            break
    except:
        continue

    command = list(map(str, input().split(" ")))
    if command[0] == "exit()":
        break
    if command[0] == "ls":
        ls_command(command[1:])
    if command[0] == "mkdir":
        mkdir_command(command[1:], os.getcwd())
