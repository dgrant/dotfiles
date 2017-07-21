#!/usr/bin/env python

import os
import shutil

IGNORES = ['bootstrap.sh', 'bootstrap.py', '.git', 'update.py']

def check_for_newer_dotfiles_in_home():
    files = os.listdir('.')
    files = [x for x in files if x not in IGNORES]
    for file in files:
        path_in_home_dir = os.path.join(os.path.expanduser('~'), file)
        if not os.path.exists(path_in_home_dir) or os.path.getmtime(path_in_home_dir) < os.path.getmtime(file):
            print('Copying', file, 'to', path_in_home_dir)
            shutil.copyfile(file, path_in_home_dir)

def main():
    check_for_newer_dotfiles_in_home()

if __name__ == '__main__':
    main()
