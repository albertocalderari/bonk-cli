from argparse import ArgumentParser, Namespace

from actions import timeline, vatnik
from actions.base import init

parser = ArgumentParser(description='CLI to bonk vatniks at scale')
main_subparser = parser.add_subparsers()
init_parser: ArgumentParser = main_subparser.add_parser("init", help="Init the bonker")
init_parser.set_defaults(func=init)

timeline_parser: ArgumentParser = main_subparser.add_parser("timeline",
                                                            help="Search for tweets to bonk in the timeline")
timeline_subparser = timeline_parser.add_subparsers()
search_parser: ArgumentParser = timeline_subparser.add_parser("search", help="Look for tweets to bonk")
search_parser.add_argument('keyword', type=str, nargs="+", help="the keyword to be used for your search")
search_parser.set_defaults(func=timeline.search)

vatnik_parser: ArgumentParser = main_subparser.add_parser("vatnik", help="Search for tweets to bonk in the timeline")
subparser = vatnik_parser.add_subparsers()
search_parser: ArgumentParser = subparser.add_parser("search", help="Look for possible vatniks")
search_parser.add_argument('keyword', type=str, nargs="+", help="The keyword to be used for your search")
search_parser.set_defaults(func=vatnik.search)
bonk_parser: ArgumentParser = subparser.add_parser("bonk", help="Look for possible vatniks")
bonk_parser.add_argument('user', type=str, help="the user to bonk")
bonk_parser.add_argument('-n', type=int, default=100, help="The nuber of tweets to bonk")
bonk_parser.set_defaults(func=vatnik.bonk_vatnik)


def main(args):
    namespace: Namespace = parser.parse_args(args)
    if hasattr(namespace, 'func'):
        namespace.func(namespace)
    else:
        args.append("-h")
        parser.parse_args(args)


if __name__ == '__main__':
    main(['vatnik', 'bonk', 'jameschristan11'])
