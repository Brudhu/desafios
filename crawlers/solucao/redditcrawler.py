#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from reddithelpers import Thread, thread_regex
from argparse import ArgumentParser
import re


def get_hot_threads(subreddits: list, hot_up_votes: int = 5000):
    """ Gets a list of Threads from subreddit with more up
        votes than hot_up_votes.

    Keyword arguments:
    subreddits -- list of subreddits name to search threads from
    hot_up_votes -- the minimum number (int) of up votes to consider
                    a thread "hot" (default 5000)

    Returns:
    List of Hot Threads
    """

    # Open Firefox browser
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    # Get hot threads list
    hot_threads = []
    for subreddit in subreddits:
        # Read Reddit source code
        driver.get(f'https://old.reddit.com/r/{subreddit}/')
        output = driver.page_source

        threads = re.findall(thread_regex, output)
        hot_threads += [Thread(subreddit, up_votes, link, title, comments_link)
                        for up_votes, link, title, comments_link in threads
                        if Thread.fix_up_votes(up_votes) >= hot_up_votes]

    # Sort threads by number of upvotes (desc)
    hot_threads.sort(key=lambda topic: topic.up_votes, reverse=True)

    # Close browser and return
    driver.quit()
    return hot_threads


def main():
    # define arguments for parser
    parser = ArgumentParser(
        description='Find "hot threads" in a groups of subreddits')

    subreddits_help = 'a list of subreddits to check separated by '\
                      '";". Eg.: "dogs;cats;brazil"'
    parser.add_argument('subreddits', type=str, help=subreddits_help)

    num_of_votes_help = 'minimum number of votes for a thread to be "hot"'
    parser.add_argument('-n', '--number-of-votes', type=int,
                        default=5000, help=num_of_votes_help)

    # get arguments
    args = parser.parse_args()
    subreddits = args.subreddits.split(';')
    hot_up_votes = args.number_of_votes

    # get hot threads
    hot_threads = get_hot_threads(subreddits, hot_up_votes)

    # Print output
    for thread in hot_threads:
        print('_' * 40)
        print(f'{thread.subreddit} | {thread.title}\nUp votes: '
              f'{thread.up_votes}\nLink: {thread.link}\nComments: '
              f'{thread.comments_link}\n')


if __name__ == '__main__':
    main()
