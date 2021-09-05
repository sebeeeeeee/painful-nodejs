import os
import sys  
import subprocess
import shutil

# You will have to change the node_modules path. Found a better solution? Make a PR on the repository!
try:
    with shutil.rmtree("/Users/username/folder/project/node_modules", os.remove("package-lock.json")), os.remove("yarn.lock")) as f:
        print("Hippity hoppity, hippty hee, ur code has commited eeeeeeee")
except FileNotFoundError:
    print('- "No files found here" said the code')


print()
print('- https://github.com/sebeeeeeee/painful-nodejs')

