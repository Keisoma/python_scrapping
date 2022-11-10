from scrapping import leagueScrapping
import argparse
import sqlite3
import pandas

parser = argparse.ArgumentParser(description='Get information about League of Legends champions')


group = parser.add_mutually_exclusive_group()
group.add_argument('-t', '--top', action='store_true', help='Get top laners')
group.add_argument('-j', '--jungle', action='store_true', help='Get junglers')
group.add_argument('-m', '--mid', action='store_true', help='Get mid laners')
group.add_argument('-a', '--adc', action='store_true', help='Get ADCs')
group.add_argument('-s', '--support', action='store_true', help='Get supports')

args = parser.parse_args()

if __name__ == '__main__':
    conn = sqlite3.connect('champions.db')
    cursor = conn.cursor()

    if args.top:
        leagueScrapping("top")
    elif args.jungle:
        leagueScrapping("jungle")
    elif args.mid:
        leagueScrapping("mid")
    elif args.adc:
        leagueScrapping("adc")
    elif args.support:
        leagueScrapping("support")