"""Experiment_23_Set6_Course_Registration_Prolog Launcher

Beginner-friendly version.
This file uses simple Python loops, lists, and dictionaries.
No heavy libraries or advanced tricks are used.
"""


import shutil


def main():
    if shutil.which('swipl') is None:
        print('SWI-Prolog is not installed.')
        print('Install SWI-Prolog and run this file again.')
        return

    print('SWI-Prolog is available.')
    print('This beginner-friendly example can be executed with the Prolog interpreter.')


if __name__ == "__main__":
    main()
