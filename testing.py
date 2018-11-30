import os
path = "C:\\Users\\jonathaaan\\Desktop\\testing"
for root, dirs, files in os.walk(path):
    for filename in files:
        print(os.path.join(root,filename))