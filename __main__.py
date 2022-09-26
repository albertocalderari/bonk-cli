from argparse import ArgumentParser

from actions import init, search

parser = ArgumentParser(description='CLI to bonk vatniks at scale')
subparser = parser.add_subparsers()
init_parser: ArgumentParser = subparser.add_parser("init", help="Init the bonker")
init_parser.set_defaults(func=init)
init_parser: ArgumentParser = subparser.add_parser("search", help="Init the bonker")
init_parser.set_defaults(func=search)

args = parser.parse_args(['search'])
args.func()
