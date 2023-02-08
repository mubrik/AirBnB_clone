#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
A command line interpreter for the AirBnB objects.
Type help to get all commands
"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """A representation of the command line interpreter
    Attributes:
    - prompt: A string to print as prompt
    """

    prompt = "(hbnb) "

    def preloop(self):
        """Set interpreter-wide attributes"""
        self.available = {"BaseModel": BaseModel}

    def emptyline(self):
        """Does nothing when the user enters an empty line"""
        return

    def do_EOF(self, line):
        """Exits the interpreter"""
        return self.close()

    def do_quit(self, line):
        """quit: Exits the interpreter"""
        return self.close()

    def close(self):
        """Does clean up tasks an exits the interpreter"""
        return True

    def do_create(self, class_name):
        """create <class_name>:
        Create and saves a new instance of <class_name>"""
        # Verify class name
        if not class_name:
            print("** class name missing **")
            return

        if class_name not in self.available:
            print("** class doesn't exist **")
            return

        obj = self.available[class_name]()  # This looks ridiculous
        storage.save()
        print(obj.id)

    def do_show(self, line):
        """show class_name object_id: prints the string representation of
        object with id object_id"""
        # Verify argument
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in self.available:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_name = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if obj_name not in all_objs:
            print("** no instance found **")
            return

        # instance exist, print it!
        print(all_objs[obj_name])

    def do_destroy(self, line):
        """destroy class_name object_id: destroy the object with the id
        object_id"""
        # Verify argument
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in self.available:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_name = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if obj_name not in all_objs:
            print("** no instance found **")
            return

        # instance exist, destroy it!
        del all_objs[obj_name]
        storage.save()

    def do_all(self, line):
        """all [class_name]: Prints all the current saved objects."""
        all_objs = storage.all()
        if line and line not in self.available:
            print("** class doesn't exist **")
            return
        filter = True if line and line in self.available else False
        list_objs = []
        if filter:
            list_objs = [v for k, v in all_objs.items() if line in k]
        else:
            list_objs = [v for _, v in all_objs.items()]
        # for obj_name, obj in all_objs.items():
        #     if not line:
        #         list_objs.append(str(obj))
        #     else:
        #         list_objs.append(str(obj))

        print(list_objs)

    def do_update(self, line):
        """update class_name object_id attribute value: Updates the object with
        the id object_id by assigning the attribute <attribute> to <value>"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        arg_l = len(args)
        if args[0] not in self.available:
            print("** class doesn't exist")
            return
        if arg_l == 1:
            print("** instance id missing **")
            return
        obj_name = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if obj_name not in all_objs:
            print("** no instance found **")
            return
        if arg_l == 2:  # no attributes
            print("** attribute name missing **")
            return
        if arg_l == 3:
            print("** value missing **")
            return
        print(args)
        # Figure out what the value is. Possible values are in integers,
        # float and strings.
        key, val = args[2], args[3]
        """ if val.count(".") == 1:  # possible float
            try:
                value = float(val)
            except ValueError:
                pass  # Not a float
        elif val.isdigit():  # it is an int
            value = int(val) """
        value = None
        try:
            if "." in key:  # float
                value = float(val)
            else:
                value = int(val)
        except ValueError as e:
            # value error means conversion failed, so str, can pass
            value = str(val)
        # Have no access to the object here. mubrik: we do now
        instance = all_objs[obj_name]
        instance[key] = value
        instance.save()
        # obj = self.available[args[0]](**obj_dict)
        # Overwrite the previous entry


if __name__ == "__main__":
    HBNBCommand().cmdloop()