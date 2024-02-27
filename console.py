import os
import sys

import cmd2

base_parser = cmd2.Cmd2ArgumentParser(description="RentikuSearch CLI")
base_subparsers = base_parser.add_subparsers(
    title="subcommands", help="subcommands help"
)
create_parser = base_subparsers.add_parser("create", help="Create Object")
create_subparsers = create_parser.add_subparsers(
    title="subcommands", help="subcommands help"
)
create_user_parser = create_subparsers.add_parser("user", help="Create user")

create_user_parser.add_argument("-u", "--username", help="username")
create_user_parser.add_argument("-e", "--email", help="email")
create_user_parser.add_argument("-p", "--password", help="password")


class RentikuSearchCMD(cmd2.Cmd):
    prompt = "RentikuSearch:> "

    def __init__(self):
        super().__init__()

    def do_EOF(self, arg):
        """
        Exit
        """
        self.poutput("\n** Bye **")
        return True

    def do_exit(self, arg):
        """Exit"""
        self.poutput("\n** Bye **")
        return True

    def do_quit(self, arg):
        """Exit"""
        self.poutput("\n** Bye **")
        return True

    def emptyline(self):
        pass

    def do_clear(self, arg):
        """Clear screen"""
        os.system("clear")

    def create_user(self, arg):
        self.poutput("++ Created")

    create_user_parser.set_defaults(func=create_user)

    @cmd2.with_argparser(create_parser)
    def do_create(self, args):
        func = getattr(args, "func", None)
        if func is not None:
            func(self, args)
        else:
            self.do_help("base")


def main():
    console = RentikuSearchCMD()
    try:
        sys.exit(console.cmdloop())
    except (KeyboardInterrupt, EOFError):
        console.poutput("\n** Bye **")
        return True


if __name__ == "__main__":
    main()
