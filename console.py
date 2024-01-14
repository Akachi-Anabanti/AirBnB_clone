#!/usr/bin/python3
"""This is the console file"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB class inheriting the cmd.Cmd class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handles EOF and terminates the program"""
        return True

    def emptyline(self):
        pass

    def postloop(self):
        print


if __name__ == '__main__':
    HBNBCommand().cmdloop()
