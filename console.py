#!/usr/bin/python3
"""
This module is the starting point for the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):

    """
    command interpreter class
    """

    prompt = "(hbnb) "

    def default(self, line):
        """
        handles cmd inputs that are not recognized by the program
        """

        self._precmd(line)

    def _precmd(self, line):
        """
        monitor and modify the command before it is executed
        """
        # print("PRECMD:::", line)
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
         if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def update_dict(self, classname, uid, s_dict):
        """
        updates the values in a given dictionary
        """
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name empty **")
        elif classname not in storage.classes():
            print("** class does not exist **")
        elif uid is None:
            print("** instance id empty **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** instance not found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_EOF(self, line):
        """
        handles EOF (end-of-file) input from the user
        """
        print()
        return True

    def do_quit(self, line):
        """
        print goodbye message and exits the program
        """
        return True

    def emptyline(self):
        """
        Empty function acts as place-holder
        """
        pass

    def do_create(self, line):
        """
        function is used to create a new record or object
        """
        if line == "" or line is None:
            print("** class name empty **")
        elif line not in storage.classes():
            print("** class does not exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)

    def do_show(self, line):
        """
        allows the user to view the provided line of code
        """
        if line == "" or line is None:
            print("** class name empty **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class does not exist **")
            elif len(words) < 2:
                print("** instance id empty **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** instance not found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """
        Deletes an instance of a certain class
        """
        if line == "" or line is None:
            print("** class name empty **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class does not exist **")
            elif len(words) < 2:
                print("** instance id empty **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** instance not found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """
        Prints all instances or instances of a certain class
        """
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class does not exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_count(self, line):
        """
        Method counts instances of a particular class
        """
        words = line.split(' ')
        if not words[0]:
            print("** class name empty **")
        elif words[0] not in storage.classes():
            print("** class does not exist **")
        else:
            matches = [
                xy for xy in storage.all() if xy.startswith(
                    words[0] + '.')]
            print(len(matches))

    def do_update(self, line):
        """
        Updates an instance based on class & ID, adding/updating an attribute
        """
        if line == "" or line is None:
            print("** class name empty **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:

            print("** class name empty **")
        elif classname not in storage.classes():
            print("** class does not exist **")
        elif uid is None:
            print("** instance id empty **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** instance not found **")
            elif not attribute:
                print("** attribute name empty **")
            elif not value:
                print("** value empty **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
