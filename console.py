#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
A command line interpreter for the AirBnB objects.
Type help to get all commands
"""

import cmd
from models import storage
from exports import valid_classes, BaseModel
from ast import literal_eval


class HBNBCommand(cmd.Cmd):
    """A representation of the command line interpreter
    Attributes:
    - prompt: A string to print as prompt
    """

    prompt = "(hbnb) "

    def preloop(self):
        """Set interpreter-wide attributes"""
        self.available = {"BaseModel": BaseModel}
        self.valid_commands = {
                "all": self.do_all,
                }

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
        if not class_name:
            print("** class name missing **")
            return

        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return
        # This looks ridiculous, mb: looks fine lol
        obj = valid_classes[class_name]()
        storage.save()
        print(obj.id)

    def do_show(self, line: str):
        """show class_name object_id: prints the string representation of
        object with id object_id"""
        # Verify argument
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in valid_classes:
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

    def do_destroy(self, line: str):
        """destroy class_name object_id: destroy the object with the id
        object_id"""
        # Verify argument
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in valid_classes:
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

    def do_all(self, line: str, **kwargs):
        """all [class_name]: Prints all the current saved objects."""
        all_objs = storage.all()
        if not kwargs:
            if line and line not in valid_classes:
                print("** class doesn't exist **")
                return
        if kwargs:
            line = kwargs['class_name']
        filter = True if line and line in valid_classes else False
        list_objs = []
        if filter:
            list_objs = [str(v) for k, v in all_objs.items() if line in k]
        else:
            list_objs = [str(v) for _, v in all_objs.items()]
        print(list_objs)

    def do_update(self, line: str):
        """update class_name object_id attribute value: Updates the object with
        the id object_id by assigning the attribute <attribute> to <value>"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        arg_l = len(args)
        if args[0] not in valid_classes:
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
        # mubrik: handle string in string?
        key, val = args[2], args[3]
        value = None
        try:
            # if "." in key:  # float
            if "." in val:  # arfs6: check value not key
                value = float(val)
            else:
                value = int(val)
        except ValueError as e:
            # value error means conversion failed, so str, can pass
            value = self.get_update_str(line)
        instance = all_objs[obj_name]
        setattr(instance, key, value)
        instance.save()

    def get_update_str(self, line):
        """Return the right string to use as value for the update command"""
        # strip the first 3 arguments
        for i in range(3):
            idx = line.index(' ')
            line = line[idx + 1:]

        if line[0] != '"':
            # return the first argument
            return line.split()[0]

        # find the other quote
        line = line[1:]
        idx = line.index('"')
        return line[:idx]

    def call_command(self, class_name, line):
        """Calls the right command to perform the task
        Parameters:
        - class_name: name of class to use
        - line: line of text to process.
            text is in the form `.command(options)`
        """
        if not line or line[0] != ".":
            # return or print error?
            return
        elif '(' not in line or ')' not in line:
            return

        line = line[1:]  # removing the first . sign
        parts = line.partition('(')
        command = parts[0]
        options = parts[1] + parts[2]
        del parts  # just felt like
        if command not in self.valid_commands:
            return
        try:
            # catch invalid options
            options = literal_eval(options)
        except SyntaxError:
            return
        self.valid_commands[command](None, class_name=class_name, options=options)

    def do_User(self, line):
        """User.command(options): Performs command on User with options"""
        self.call_command('User', line)

    def do_BaseModel(self, line):
        """BaseModel.command(options): Performs command on BaseModel with options"""
        self.call_command('BaseModel', line)

    def do_Place(self, line):
        """Place.command(options): Performs command on Place with options"""
        self.call_command('Place', line)

    def do_City(self, line):
        """City.command(options): Performs command on City with options"""
        self.call_command('City', line)

    def do_Review(self, line):
        """Review.command(options): Performs command on Review with options"""
        self.call_command('Review', line)

    def do_Amenity(self, line):
        """Amenity.command(options): Performs command on Amenity with options"""
        self.call_command('Amenity', line)

    def do_State(self, line):
        """State.command(options): Performs command on State with options"""
        self.call_command('State', line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
