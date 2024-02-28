import os
import sys

import cmd2

from RentikuSearch.models import storage
from RentikuSearch.models.models import Property, User

storage.reload()

base_parser = cmd2.Cmd2ArgumentParser(description="RentikuSearch CLI")
base_subparsers = base_parser.add_subparsers(
    title="subcommands", help="subcommands help"
)
create_parser = base_subparsers.add_parser("create", help="Create Object")
create_subparsers = create_parser.add_subparsers(
    title="subcommands", help="subcommands help"
)
create_user_parser = create_subparsers.add_parser("user", help="Create user")

create_user_parser.add_argument(
    "-u", "--username", required=True, help="username"
)
create_user_parser.add_argument("-e", "--email", required=True, help="email")
create_user_parser.add_argument("-p", "--password", help="password")

create_property_parser = create_subparsers.add_parser(
    "property", help="Create property"
)

create_property_parser.add_argument("-T", "--title", help="Property title")
create_property_parser.add_argument("-t", "--type", help="Property type")
create_property_parser.add_argument(
    "-d", "--description", help="Property Description"
)
create_property_parser.add_argument(
    "-l", "--location", help="Property location"
)
create_property_parser.add_argument(
    "-p", "--price", type=float, help="Property price"
)
create_property_parser.add_argument(
    "-u", "--owner-id", type=int, help="Property owner"
)


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
        user = User(
            username=arg.username,
            email=arg.email,
            password_hash=arg.password,
        )
        user.save()

    create_user_parser.set_defaults(func=create_user)

    def create_property(self, arg):
        property = Property(
            title=arg.title,
            type=arg.type,
            description=arg.description,
            location=arg.location,
            price=arg.price,
            owner_id=arg.owner_id,
        )
        property.save()

    create_property_parser.set_defaults(func=create_property)

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
