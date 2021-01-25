import argparse
import requests


GITHUB_API = ()


def create_parser():
    parser = argparse.ArgumentParser(description='Get URL and requests Github repository')
    parser.add_argument('url', type=str, help='a github url')
    parser.add_argument('--begin', nargs='?', help='begin date')
    parser.add_argument('--end', nargs='?', help='ending date')
    parser.add_argument('--b', default='master', help='repository branch')

    # args = parser.parse_args()
    # print(args.accumulate())

    return parser


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    git_url = args.url
    date_begin = args.begin
    date_end = args.end
    branch = args.b

    print('url={}'.format(git_url))
    print('date_begin={}'.format(date_begin))
    print('date_end={}'.format(date_end))
    print('branch={}'.format(branch))

