import os as dirHandling

# Create Directory
oldDirName = "/Users/vijay/Documents/MyWorkPlace/Learning/Python/PyCharm_PY_WorkPlace/Old_Directory"
dirHandling.mkdir(oldDirName)

# Rename Directory
newDirName = "/Users/vijay/Documents/MyWorkPlace/Learning/Python/PyCharm_PY_WorkPlace/New_Directory"
dirHandling.rename(oldDirName, newDirName)

# Delete Directory
dirHandling.rmdir(newDirName)

# Get Current working directory path
print("Current Working Directory Path:", dirHandling.getcwd())

# Change working directory path
dirHandling.chdir("/Users/vijay/Documents/MyWorkPlace/Learning/Python/PyCharm_PY_WorkPlace")
print("Updated Working Directory Path:", dirHandling.getcwd())
print("Updated Working Directory Path:", dirHandling.listdir())
print("Updated Working Directory Path:", dirHandling.listdir("/users"))
