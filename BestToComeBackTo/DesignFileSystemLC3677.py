"""
Description

In this problem, you need to design a file system that can create a new path and bind a value.
Each of these paths begins with a separator /, and there must be several lowercase letters after each separator.
For example, /lint and /lint/code are valid paths, while an empty string and / are not.

You need to implement the following method:
    bool createPath(string path, int value): Determine whether path can be created, if yes, create and bind the corresponding value, and return true at the same time, otherwise return false.
    int get(string path): If the path path exists, return the value associated with path, otherwise return -1.
"""

class file_system:
    def __init__(self):
        self.fs_tree = {}

    def createPath(self, path, value):
        if not path:
            return False

        if path in self.fs_tree:
            return False

        currParent = path[:path.rfind("/")]

        if len(currParent) > 1 and currParent not in self.fs_tree:
            return False

        self.fs_tree[path] = value
        return True

    def get(self, path):
        if path in self.fs_tree:
            return self.fs_tree[path]
        return -1


fs = file_system()
fs.createPath("/root", 1)
fs.createPath("/root/dev", 2)
print(fs.fs_tree)
print(fs.get("/root/dev"))