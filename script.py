import os
import sys  
import subprocess
import shutil


try:
    with shutil.rmtree("/Users/username/folder/project/node_modules", os.remove("package-lock.json")) as f:
        print("Hippity hoppity, hippty hee, node.js has commited alt+f4")
except FileNotFoundError:
    print('- "No files found here" said the code')


print()
print("- You should check out my Github! https://github.com/sebeeeeeee")

