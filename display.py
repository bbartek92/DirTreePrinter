import base
from colored import fg

class TreePrinter():
    def __init__(self):
        self.mytree = base.Tree()
    def print_tree(self, path, level):
        tree = self.mytree.get_tree(path, level)
        colors = ['green', 'light_blue', 'magenta', 'cyan', 'yellow', 'red',
                  'light_gray', 'light_green', 'blue', 'light_magenta',
                  'light_cyan', 'light_yellow', 'light_red' ]
        for i in tree:
            try:
                color = fg(colors[i[0]-1])
            except IndexError:
                color = fg('cyan_1')
            print(color + '\t'*i[0], i[1], i[2])
        print(fg(15) + '')