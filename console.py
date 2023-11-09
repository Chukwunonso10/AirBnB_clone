#!/usr/bin/python3

import cmd

class HBNBCommands(cmd.Cmd):
    """This defines the class that inherits from the cmd module"""
    intro = "Alx first introducton to AirBnB_clone project"

    prompt = "(hbnb) "

    def default(self, line):
        """invoked when the users Enters nothing"""
        return True

    def do_quit(self, line):
        """exit the shell"""
        return True
    def do_EOF(self, line):
        """handles when an EOF is encountered"""
        return true
    def do_help(self, line):
        """invokes the command for help"""
        print()

if __name__=="__main__":
    MyHbnb().cmdloop()

