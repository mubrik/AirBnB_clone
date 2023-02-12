#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Test case for the Console.
"""

import unittest
import sys
import io
from unittest.mock import create_autospec
from console import HBNBCommand
from models.base_model import BaseModel
from contextlib import redirect_stdout


class TestConsole(unittest.TestCase):
    """Test case for TestConsole attributes"""

    def setUp(self) -> None:
        self.id_regex = r"[\d\w]{8}-[\d\w]{4}-[\d\w]{4}-[\d\w]{4}-[\d\w]{12}"
        return super().setUp()

    def test_help_all(self):
        """Tesing `help all` command"""
        f = io.StringIO()
        with redirect_stdout(f):
            HBNBCommand().onecmd("help all")
            self.assertEqual(
                HBNBCommand.do_all.__doc__ + "\n", f.getvalue())
            f.close()

    def test_help_show(self):
        """Tesing `help show` command"""
        f = io.StringIO()
        with redirect_stdout(f):
            HBNBCommand().onecmd("help show")
            self.assertEqual(
                HBNBCommand.do_show.__doc__ + "\n", f.getvalue())
            f.close()

    def test_help_update(self):
        """Tesing `help update` command"""
        f = io.StringIO()
        with redirect_stdout(f):
            HBNBCommand().onecmd("help update")
            self.assertEqual(
                HBNBCommand.do_update.__doc__ + "\n", f.getvalue())
            f.close()

    def test_help_destroy(self):
        """Tesing `help destroy` command"""
        f = io.StringIO()
        with redirect_stdout(f):
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(
                HBNBCommand.do_destroy.__doc__ + "\n", f.getvalue())
            f.close()

    def test_help_create(self):
        """Tesing `help create` command"""
        f = io.StringIO()
        with redirect_stdout(f):
            HBNBCommand().onecmd("help create")
            self.assertEqual(
                HBNBCommand.do_create.__doc__ + "\n", f.getvalue())
            f.close()

    def test_create_invalid(self):
        """testing invalid create command"""
        f = io.StringIO()
        with redirect_stdout(f):
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())
            f.close()

    def test_create_invalid_arg(self):
        """testing invalid create command"""
        f = io.StringIO()
        with redirect_stdout(f):
            HBNBCommand().onecmd("create invalid")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
            f.close()

    def test_create_valid_user(self):
        """testing valid create user command"""
        f = io.StringIO()
        with redirect_stdout(f):
            HBNBCommand().onecmd("create User")
            self.assertRegex(
                f.getvalue(),
                self.id_regex)
            f.close()

    def test_create_valid_amenity(self):
        """testing valid create Amenity command"""
        f = io.StringIO()
        with redirect_stdout(f):
            HBNBCommand().onecmd("create Amenity")
            self.assertRegex(
                f.getvalue(),
                self.id_regex)
            f.close()
