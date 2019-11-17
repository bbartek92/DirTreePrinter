import argparse
import sys
import os
import display

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write(f'error: {message}\n')
        self.print_help()
        sys.exit(2)

class Config():
    def __init__(self):
        self.current_path = os.getcwd()
        self.display_lvl = 3

    def set_path(self, path=''):
        if path != '':
            self.current_path = path

    def set_level(self, level=''):
        if level != '':
            self.display_lvl = int(level)

my_parser = MyParser(prog='DirTreePrinter',
                     description='This app prints directory trees.')

my_parser.add_argument('-path', action='store',
                       help='Your directory full path, if skipped, '
                            'will use currect directory')

my_parser.add_argument('-level', action='store',
                       help='Provide a level of tree depth, defaults to 3')

args = my_parser.parse_args()

cnfg = Config()
if args.path:
    cnfg.set_path(args.path)

if args.level:
    cnfg.set_level(args.level)

tree = display.TreePrinter()

tree.print_tree(cnfg.current_path, cnfg.display_lvl)