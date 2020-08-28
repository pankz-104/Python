# changing name of folders on order 1  .. 2 .. 3 .. 

import os

def dir_checker(Dir):
    return os.path.isdir(Dir)

def file_checker(File):
    return os.path.isfile(File)

if __name__ == '__main__':
    print("Welcome to folder preetify !!")

    a = 0
    while True:
        print("Enter a directory")
        direc = input("Directory: ")

        if dir_checker(direc):
            print("Checked if it is a directory ..!! \n yes ti is ")
            break
        elif not dir_checker(direc):
            print("Checked if it is a directory ..!! \n No its not a directory")
            continue

    os.chdir(direc)

    while True:
        print("Enter file name: ")
        file_name = input("File name: ")
        if file_checker(file_name):
            print("Checked if file exists \n yes file exists")
            break
        elif not file_checker(file_name):
            print("Checked if file exists \n No file dont exists")
            continue

    while True:
        print("Enter file format")
        file_format = input("File format: ")
        if file_format.endswith(".jpg"):
            break
        elif file_format.endswith(".txt"):
            break
        elif file_format.endswith(".py"):
            break
        elif file_format.endswith(".exe"):
            break
        elif file_format.endswith(".apk"):
            break
        else:
            print("Extension is not supported.. try another one ")
            continue

    for fileName in os.listdir(direc):
        if fileName == file_name:
            continue

        elif file_checker(file_name):
            if fileName.endswith(file_format):
                a += 1
                os.rename(fileName, f"{a} {file_format}")
            else:
                os.rename(fileName,fileName.capitalize())
        elif not file_checker(fileName):
            continue
