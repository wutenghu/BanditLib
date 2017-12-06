"""
    Author: wutenghu <wutenghu@chuangxin.com>
    Date:   2017/12/6
"""
import argparse


def main():
    parser = argparse.ArgumentParser(description='this is the description')
    parser.add_argument('--alg', dest='alg',
                        help='Select a specific algorithm')
    parser.add_argument('--context_dim', type=int,
                        help='Set dimension of context features.')
    parser.add_argument('--hidden_dim', type=int,
                        help='Set dimension of hidden features.')

    args = parser.parse_args()

    print('arg --alg {}'.format(type(args.alg)))

if __name__ == '__main__':
    main()
