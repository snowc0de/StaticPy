# Modules
import os
import fileinput
import linecache
import shutil

# Will define what directory to use for the os module
# Make the dir.txt file empty
file = open("dir.txt", "w")
file.write('')
file.close()
file = open("dir.txt", "r")
# Adding the path into it
file.close()
file = open("dir.txt", "a")
file.write(os.getcwd())
# Save the original path as oripath
file.close()
file = open("dir.txt", "r")
oripath = file.read()
file.close()

# Adding template folders into it
file = open("dir.txt", "a")
file.write("/template/")

# Template finder
template = 'cmd'

# Adding template to file
file.write(template)
file.close()
# Set path as file
file = open("dir.txt", "r")
path = file.read()
file.close()
# Set file as path
os.chdir(path)
file = open("dir.txt", "w")
file.write(path)
file.close()

# template selector, to-do
template = 'cmd'
# MILESTONE ALGO
# File finder
i = 1
while i != 0:
    os.chdir(path)
    open("templates.txt", "r")
    l = linecache.getline('templates.txt', i)
    if l == '':
        i = 0
    else:
        print(l)
        i = i + 1
# File selector
filename = input("What file do you want to use? ")
file = open("dir.txt", "a")
file.write("/")
file.write(filename)
file.close()
file = open("dir.txt", "r")
path = file.read()
# Copy the content files to the main output dir
os.chdir(path)
print(path)
os.system("ls")

# Delete content of the ancient file
file.close()
file = open("cp.txt", "w")
file.write("")
file.close()

# Writting the beggining of the comment cp -r path1
file = open("cp.txt", "a")
file.write("cp -r ")
file.write(path)

# Exception for index file
if filename == "index":
    file.write("/*")

# Adding the end of the command cp -r path1 path2
file.write(" ")
file.write(oripath)
file.write("/output")

# Excepetion for index file
if filename == "index":
    file.write("")
else:
    file.write("/")

file.close()
file = open("cp.txt", "r")
run = file.read()
print("run is ", run)
os.system(run)

# Replace variables from var to selected file.
i = 1
while i != 0:
    os.chdir(path)
    open("var.txt", "r")
    v = linecache.getline('var.txt', i)
    if v == '': # Nothing as end of vars, not works for the moment
        i = 0
    else:
        print("What is the variable ",v)
        a = input("[Type e for getting your editor]")
        with fileinput.FileInput("var.txt", inplace=True, backup='.bak') as file:
            for line in file:
                os.chdir(path)
                open(filename)
                print(line.replace(v, a), end='')
        i = i + 1
name = input("What is the name of your", filename, "? ")


# Publish script
print("0 : I don't what to pulish, I just need the files")
print("1 : Using IPFS")
print("2 : Using FTP")
print("3 : Locally")

publish = input("How do you want to publish your website? ")

if publish == 0:
    print("Your files are in the output directory")
else:
    print("Cannot continue, please wait the next release")
