import os
import sys  
import subprocess
import shutil

# You will have to change the node_modules path. Found a better solution? Make a PR on the repository!
try:
    with shutil.rmtree("/Users/username/folder/project/node_modules", os.remove("package-lock.json")) as f:
        print("Hippity hoppity, hippty hee, node.js has commited alt+f4")
except FileNotFoundError:
    print('- "No files found here" said the code')


print()
print('- https://github.com/sebeeeeeee/painful-nodejs')

