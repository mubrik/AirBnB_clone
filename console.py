#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
A command line interpreter for the AirBnB objects.
Type help to get all commands
"""

import cmd
from models import storage
from exports import valid_classes, BaseModel


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

    def do_create(self, class_name: str):
        """create <class_name>:
        Create and saves a new instance of <class_name>"""
        # Verify class name
        if not self.is_line_valid(class_name, "create"):
            return
        # This looks ridiculous, mb: looks fine lol
        obj = valid_classes[class_name]()
        storage.save()
        print(obj.id)

    def do_show(self, line: str):
        """show class_name object_id: prints the string representation of
        object with id object_id"""
        # Verify argument
        if not self.is_line_valid(line, "show"):
            return
        args = line.split()
        obj_name = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if obj_name not in all_objs:
            print("** no instance found **")
            return

        # instance exist, print it!
        print(all_objs[obj_name])

    def do_destroy(self, line: str):
        """destroy class_name object_id: destroy the object with the id
        object_id"""
        # Verify argument
        if not self.is_line_valid(line, "destroy"):
            return
        args = line.split()
        obj_name = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if obj_name not in all_objs:
            print("** no instance found **")
            return

        # instance exist, destroy it!
        del all_objs[obj_name]
        storage.save()

    def do_all(self, line: str):
        """all [class_name]: Prints all the current saved objects."""
        if not self.is_line_valid(line, "all"):
            return
        all_objs = storage.all()
        filter = True if line and line in valid_classes else False
        list_objs = []
        if filter:
            list_objs = [str(v) for k, v in all_objs.items() if line in k]
        else:
            list_objs = [str(v) for _, v in all_objs.items()]
        # do we print an empty list?
        print(list_objs)

    def do_update(self, line: str):
        """update class_name object_id attribute value: Updates the object with
        the id object_id by assigning the attribute <attribute> to <value>"""
        # not limiting it splits the space in value eg:hello world
        if not self.is_line_valid(line, "update"):
            return
        args = line.split(" ", 3)
        arg_l = len(args)
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
        key, val = args[2], args[3]
        # do we strip here? if val = "33" ~= "'33'" the conversion to ..
        # int below wont work?
        value = None
        try:
            value = float(val) if "." in val else int(val)
        except ValueError as e:
            # just pass value?
            value = self.get_update_str(val)
        instance = all_objs[obj_name]
        setattr(instance, key, value)
        instance.save()

    def get_update_str(self, line: str):
        """Return the right string to use as value for the update command"""
        # strip the first 3 arguments
        """ for i in range(3):
            idx = line.index(' ')
            line = line[idx + 1:] """
        # lets make a wild assumption
        if line[0] == '"' and line[-1] == '"':
            return line[1:-1]
        if line[0] == "'" and line[-1] == "'":
            return line[1:-1]
        return line
        # find the other quote
        line = line[1:]
        idx = line.index('"')
        return line[:idx]

    def is_line_valid(self, line: str, func: str):
        """validator for all handlers """
        if not line:
            if func == "all":
                return True
            print("** class name missing **")
            return False
        args = line.split(" ", 3)
        # classname
        if args[0] not in valid_classes:
            print("** class doesn't exist **")
            return False
        if func in ["all", "create"]:
            return True
        # instance
        if len(args) == 1:
            print("** instance id missing **")
            return False
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
