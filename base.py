import os
import re

class Tree:
    def __init__(self):
        self.counter = 0
        self.dir_list = []
    def get_tree(self, path, level):
        self.level = level
        self.path = path
        self.path_to_level()
        self.recur(self.path, '', self.counter)
        return(self.dir_list)

    def path_to_level(self):
        for _ in range(0, self.level):
            self.path = os.path.dirname(os.path.normpath(self.path))

    def recur(self, path, i, count):
        if self.level*2 > count:
            count += 1
            path = os.path.join(path, i)
            dir = os.listdir(path)
            for pos, i in enumerate(dir):
                if not os.path.isdir(os.path.join(path, i)):
                    # print('not a path', i)
                # if re.match('.*\..*', i):
                    self.dir_list.append([count, pos, i])
                else:
                    self.dir_list.append([count, pos, i])
                    self.recur(path, i, count)