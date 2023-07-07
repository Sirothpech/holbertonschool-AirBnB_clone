#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter
"""
import sys
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """
    This class contains the entry point of the command interpreter.
    """

    prompt = '(hbnb) '

    class_mapping = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)
        """
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print('** class name missing **')
            return

        try:
            cls = getattr(sys.modules[__name__], arg)
            instance = cls()
            instance.save()
            print(instance.id)
        except AttributeError:
            print('** class doesn\'t exist **')

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()

        if not args:
            print('** class name missing **')
            return

        class_name = args[0]
        if class_name not in __class__.class_mapping:
            print('** class doesn\'t exist **')
            return

        if len(args) < 2:
            print('** instance id missing **')
            return

        instance_id = args[1]
        key = '{}.{}'.format(class_name, instance_id)
        if key not in models.storage.all():
            print('** no instance found **')
            return
        instance = models.storage.all()[key]
        print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()

        if not args:
            print('** class name missing **')
            return

        class_name = args[0]
        if class_name not in __class__.class_mapping:
            print('** class doesn\'t exist **')
            return

        if len(args) < 2:
            print('** instance id missing **')
            return

        instance_id = args[1]
        key = '{}.{}'.format(class_name, instance_id)
        if key not in models.storage.all():
            print('** no instance found **')
            return

        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, arg):
        """Prints string representation of all instances"""
        args = arg.split()
        if not args:
            instances = models.storage.all().values()
        else:
            class_name = args[0]
            if class_name not in __class__.class_mapping:
                print('** class doesn\'t exist **')
                return
            instances = []
            for instance in models.storage.all().values():
                if type(instance).__name__ == class_name:
                    instances.append(instance)

        print([str(instance) for instance in instances])

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in __class__.class_mapping:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = models.storage.all()
        if key not in objects:
            print("** no instance found **")
            return

        # instance found

        if len(args) == 2:
            print("** attribute name missing **")
            return

        attr_name = args[2]

        if len(args) == 3:
            print("** value missing **")
            return

        # Update the instance attribute
        attr_value = args[3]
        obj = objects[key]
        setattr(obj, attr_name, attr_value)
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
