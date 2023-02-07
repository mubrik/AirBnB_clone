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
    prompt = '(hbnb) '

    def preloop(self):
        """Set interpreter-wide attributes"""
        self.available = {'BaseModel': BaseModel}
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
        """create <class_name>: Create and saves a new instance of <class_name>"""
        # Verify class name
        if not class_name:
            print('** class name missing **')
            return
        elif class_name not in self.available:
            print("** class doesn't exist **")
            return

        obj = self.available[class_name]() # This looks ridiculous
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
        elif len(args) == 1:
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
        elif len(args) == 1:
            print("** instance id missing **")
            return
        obj_name = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if obj_name not in all_objs:
            print("** no instance found **")
            return

        # instance exist, destroy it!
        del all_objs[obj_name]

    def do_all(self, line):
        """all [class_name]: Prints all the current saved objects."""
        all_objs = storage.all()
        if line and line not in self.available:
            print("** class doesn't exist **")
            return
        list_objs = []
        for obj_name, obj in all_objs.items():
            if not line:
                list_objs.append(str(obj))
            else:
                list_objs.append(str(obj))

        print(list_objs)

    def do_update(self, line):
        """update class_name object_id attribute value: Updates the object with
        the id object_id by assigning the attribute <attribute> to <value>"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in self.available:
            print("** class doesn't exist")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        obj_name = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if obj_name not in all_objs:
            print("** no instance found **")
            return
        if len(args) == 2: # no attributes
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return

        # Figure out what the value is. Possible values are in integers,
        # float and strings.
        value = args[3]
        if value.count('.') == 1:  # possible float
            try:
                value = float(value)
            except ValueError:
                pass # Not a float
        elif value.isdigit():  # it is an int
            value = int(value)

# Have no access to the object here.
        # Creating a new object with the same attributes as the current object
        # and new attribute
        obj_dict = all_objs[obj_name]
        obj_dict[args[2]] = value
        obj = self.available[args[0]](**obj_dict)
        # Overwrite the previous entry
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
