#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Test case for the Console.
"""

import unittest
from unittest.mock import patch
import io
from console import HBNBCommand
from contextlib import redirect_stdout


class TestConsole(unittest.TestCase):
    """Test case for TestConsole attributes"""

    def setUp(self):
        """setup"""
        self.id_regex = r"[\d\w]{8}-[\d\w]{4}-[\d\w]{4}-[\d\w]{4}-[\d\w]{12}"

    def test_help_all(self):
        """Tesing `help all` command"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(
                HBNBCommand.do_all.__doc__ + "\n", f.getvalue())
            f.close()

    def test_help_show(self):
        """Tesing `help show` command"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(
                HBNBCommand.do_show.__doc__ + "\n", f.getvalue())
            f.close()

    def test_help_update(self):
        """Tesing `help update` command"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertEqual(
                HBNBCommand.do_update.__doc__ + "\n", f.getvalue())
            f.close()

    def test_help_destroy(self):
        """Tesing `help destroy` command"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(
                HBNBCommand.do_destroy.__doc__ + "\n", f.getvalue())
            f.close()

    def test_help_create(self):
        """Tesing `help create` command"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(
                HBNBCommand.do_create.__doc__ + "\n", f.getvalue())
            f.close()

    def test_create_invalid(self):
        """testing invalid create command"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())
            f.close()

    def test_create_invalid_arg(self):
        """testing invalid create command"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create invalid")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
            f.close()

    def test_create_valid_basemodel(self):
        """testing valid create BaseModel command"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertRegex(
                f.getvalue(),
                self.id_regex)
            f.close()

    def test_create_valid_user(self):
        """testing valid create user command"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User")
            self.assertRegex(
                f.getvalue(),
                self.id_regex)
            f.close()

    def test_create_valid_amenity(self):
        """testing valid create Amenity command"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            self.assertRegex(
                f.getvalue(),
                self.id_regex)
            f.close()

    def test_create_valid_city(self):
        """testing valid create City command"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create City")
            self.assertRegex(
                f.getvalue(),
                self.id_regex)
            f.close()

    def test_create_valid_place(self):
        """testing valid create Place command"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            self.assertRegex(
                f.getvalue(),
                self.id_regex)
            f.close()

    def test_create_valid_state(self):
        """testing valid create State command"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create State")
            self.assertRegex(
                f.getvalue(),
                self.id_regex)
            f.close()

    def test_create_valid_review(self):
        """testing valid create Review command"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            self.assertRegex(
                f.getvalue(),
                self.id_regex)
            f.close()
