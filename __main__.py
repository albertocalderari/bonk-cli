from argparse import Namespace

from cli import parser
from static import CONFIG_FILE


def main(args):
    namespace: Namespace = parser.parse_args(args)
    if hasattr(namespace, 'func'):
        namespace.func(namespace)
    else:
        args.append("-h")
        parser.parse_args(args, CONFIG_FILE)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
