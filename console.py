#!/usr/bin/python3
"""This is the console file"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """Handles EOF and terminates the program"""
        print("")
        return True

    def emptyline(self):
        """handles empty line in response to the prompt;
        does nothing
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
