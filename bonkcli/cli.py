import sys
from argparse import ArgumentParser, Namespace

from bonkcli.actions import timeline, vatnik
from bonkcli.actions.base import init, update_current_config
from bonkcli.models import By
from bonkcli.static import CONFIG_FILE, BANNER, DOG

values = [v.value for v in By]

parser = ArgumentParser(description="CLI to bonk vatniks at scale. Let's go bonking!")
main_subparser = parser.add_subparsers()

# init
init_parser: ArgumentParser = main_subparser.add_parser("init", help="Init the bonker")
init_parser.set_defaults(func=init)

# timeline
timeline_parser: ArgumentParser = main_subparser.add_parser(
    "timeline",
    help="Search for tweets to bonk in the timeline"
)
timeline_subparser = timeline_parser.add_subparsers()
search_parser: ArgumentParser = timeline_subparser.add_parser(
    "search",
    help="Look for tweets to bonk"
)
search_parser.add_argument(
    'keyword',
    type=str,
    nargs="+",
    help="the keyword to be used for your search"
)
search_parser.add_argument(
    "--by",
    type=By,
    default=By.recent,
    help=f"What method should be used to sort the tweets: {[v for v in By]}, default 'recent'"
)
search_parser.set_defaults(func=timeline.search)

# vatnik
vatnik_parser: ArgumentParser = main_subparser.add_parser(
    "vatnik",
    help="Search for tweets to bonk in the timeline"
)
subparser = vatnik_parser.add_subparsers()
search_parser: ArgumentParser = subparser.add_parser(
    "search",
    help="Look for possible vatniks"
)
search_parser.add_argument(
    'keyword',
    type=str,
    nargs="+",
    help="The keyword to be used for your search"
)
search_parser.add_argument(
    "--by",
    type=By,
    default=By.popular,
    help=f"What method should be used to sort the tweets: {', '.join(values)}"
)
search_parser.set_defaults(func=vatnik.search)

bonk_parser: ArgumentParser = subparser.add_parser("bonk", help="Bonk a vatnik")
bonk_parser.add_argument('user', type=str, help="The user to bonk")
bonk_parser.add_argument(
    '-n',
    type=int,
    default=100,
    help="The nuber of tweets to bonk, default 100"
)
bonk_parser.add_argument(
    '--retweets',
    default=False,
    action='store_true',
    help="Include Retweets"
)
bonk_parser.add_argument(
    '--replies',
    default=False,
    action='store_true',
    help="Include Replies"
)
bonk_parser.set_defaults(func=vatnik.bonk_vatnik)


def run(args):
    namespace: Namespace = parser.parse_args(args)
    if hasattr(namespace, 'func'):
        config = namespace.func(namespace, CONFIG_FILE)
        update_current_config(CONFIG_FILE, config)
    else:
        args.append("-h")
        parser.parse_args(args)


def main():
    print(DOG)
    print(BANNER)
    run(sys.argv[1:])
