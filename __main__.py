import sys
from argparse import ArgumentParser, Namespace

from actions import base, vatnik
from actions.base import init
from actions.timeline import search

parser = ArgumentParser(description='CLI to bonk vatniks at scale')
subparser = parser.add_subparsers()
init_parser: ArgumentParser = subparser.add_parser("init", help="Init the bonker")
init_parser.set_defaults(func=init)

timeline_parser: ArgumentParser = subparser.add_parser("timeline", help="Search for tweets to bonk in the timeline")
subparser = timeline_parser.add_subparsers()
search_parser: ArgumentParser = subparser.add_parser("search", help="Look for tweets to bonk")
search_parser.add_argument('keyword', type=str, nargs="+", help="the keyword to be used for your search")
search_parser.set_defaults(func=search)

def main(args):
    namespace: Namespace = parser.parse_args(args)
    if hasattr(namespace, 'func'):
        namespace.func(namespace)
    else:
        args.append("-h")
        parser.parse_args(args)

if __name__ == '__main__':
    main(['timeline', 'search', "ukronazi", "russia"])