import os as fileHandling
# Text File Handling

# Create a Text file
myTextFile = open("/Users/vijay/Documents/MyWorkPlace/Learning/Python/PyCharm_PY_WorkPlace/External_Files/TextFile.txt", 'w')
myTextFile.write("Python Text File.")
myTextFile.close()

# Append a Text file
myTextFile = open("/Users/vijay/Documents/MyWorkPlace/Learning/Python/PyCharm_PY_WorkPlace/External_Files/TextFile.txt", 'a')
myTextFile.write("This File Contains description of python methods. ")
myTextFile.close()

# Read a Text file
myTextFile = open("/Users/vijay/Documents/MyWorkPlace/Learning/Python/PyCharm_PY_WorkPlace/External_Files/TextFile.txt", 'r')
view_Content = myTextFile.read()
print(view_Content)
myTextFile.close()

# Rename File
oldFileName = "/Users/vijay/Documents/MyWorkPlace/Learning/Python/PyCharm_PY_WorkPlace/External_Files/NewTextFile.txt"
newFileName = "/Users/vijay/Documents/MyWorkPlace/Learning/Python/PyCharm_PY_WorkPlace/External_Files/TextFile.txt"
fileHandling.rename(oldFileName, newFileName)

# Delete File
fileHandling.remove(newFileName)





