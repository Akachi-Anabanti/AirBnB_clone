#!/usr/bin/python3
"""This is the console file"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import file_path
import json
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    __class_names = {"BaseModel": BaseModel}

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """Handles EOF and terminates the program"""
        print("")
        return True

    def emptyline(self):
        """handles empty line in response to the prompt;
        does nothing
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it
        (to JSON file) and prints the is

        Usage:
            $ create BaseModel
        """

        if not line:
            print("** class name missing **")
            return False
        if len(line.split(" ")) > 1 or line not in self.__class_names.keys():
            print("** class doesn't exist **")
            return False
        my_model_inst = self.__class_names[line]()
        my_model_inst.save()
        print(my_model_inst.id)

    def do_show(self, line):
        """
        Prints the string representation of
        an instance based on the class name and id

        Usage:
            $ show BaseModel 9uhsu8-8fjhnis89-0vnslwu
        """

        if not line:
            print("** class name missing **")
            return False
        cmd_args = line.split(" ")
        class_name = cmd_args[0]

        if class_name not in self.__class_names.keys():
            print("** class doesn't exist **")
            return False

        if len(cmd_args) != 2:
            print("** instance id missing **")
            return False

        class_instance_id = cmd_args[1]

        instance_key = ".".join([class_name, class_instance_id])

        with open(file_path, "r") as f:
            objects = json.load(f)
            if instance_key not in objects.keys():
                print("** no instance found **")
                return False
        obj_dict = objects[instance_key]
        my_obj_instance = self.__class_names[class_name](**obj_dict)
        print(my_obj_instance)

    def do_destroy(self, line):
        """
        Deletes an instance base on the class name and id (
        save changes in the JSON file)

        Usage:
            $ destroy BaseModel 1234-1234-1234
        """

        if not line:
            print("** class name missing **")
            return False

        cmd_args = line.split(" ")
        class_name = cmd_args[0]

        if class_name not in self.__class_names.keys():

            print("** class doesn't exist **")
            return False

        if len(cmd_args) != 2:

            print("** instance id missing **")
            return False

        class_instance_id = cmd_args[1]

        instance_key = ".".join([class_name, class_instance_id])

        with open(file_path, "r") as f:
            objects = json.load(f)
            if instance_key not in objects.keys():
                print("** no instance found **")
                return False

        del objects[instance_key]
        storage.delete(instance_key)

        with open(file_path, "w") as f:
            json.dump(objects, f)

    def do_all(self, line):
        """
        Prints all string representation of all instances based
        or not on the class name

        Usage:
            $ all BaseModel
            $ all
        """
        obj_list = []
        with open(file_path, "r") as f:
            objects = json.load(f)
        if not line:
            for obj_key, obj_dict in objects.items():
                class_name = obj_key.split(".")[0]
                my_obj_instance = self.__class_names[class_name](**obj_dict)
                obj_list.append(str(my_obj_instance))
            print(obj_list)

        elif len(line.split(" ")) > 1 or\
                line not in self.__class_names.keys():
            print("** class doesn't exist **")
            return False

        else:
            for obj_key, obj_dict in objects.items():
                if obj_key.startswith(line):
                    class_name = obj_key.split(".")[0]
                    my_obj_instance =\
                        self.__class_names[class_name](**obj_dict)
                    obj_list.append(str(my_obj_instance))
            print(obj_list)

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by updating the change into the JSON file
        usage:
            $ update <class name> <id> <attribute name> <attribute value>"
        only one attribute can be updated at a time
        """
        with open(file_path) as f:
            objects = json.load(f)
        if not line:
            print("** class name missing **")
            return False
        cmd_args = line.split(" ")

        if cmd_args[0] not in self.__class_names.keys():
            print("** class doesn't exist **")
            return False
        if len(cmd_args) < 2:
            print("** instance id missing **")
            return False
        class_name = cmd_args[0]
        obj_instance_id = cmd_args[1]
        instance_key = class_name + "." + obj_instance_id
        if instance_key not in objects.keys():
            print("** no instance found **")
            return False
        if len(cmd_args) < 3:
            print("** attribute name missing **")
            return False
        if len(cmd_args) < 4:
            print("** value missing **")
            return False
        attr_name = cmd_args[2]
        attr_val = cmd_args[3]

        obj_dict = objects[instance_key]
        obj_dict[attr_name] = attr_val

        my_obj_instance = self.__class_names[class_name](**obj_dict)
        storage.new(my_obj_instance)
        my_obj_instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
