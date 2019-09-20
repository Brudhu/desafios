class Thread:
    """ Class to handle information from Reddit Threads.

    The property-methods are:
    - title (of the thread)
    - link (to the thread)
    - comments_link (to the thread's comments)
    - up_votes (of the thread)
    - subreddit (where the thread is located)

    There is also a static method that fix the upvotes:
    fix_up_votes(up_votes: str)
    """

    _title = ''
    _link = ''
    _comments_link = ''
    _up_votes = 0
    _subreddit = ''

    def __init__(self, subreddit: str, up_votes: str,
                 link: str, title: str, comments_link: str):
        """ Constructor for the Thread class.

        Keyword arguments:
        subreddit -- subreddit name (str)
        up_votes -- number of up votes (str)
        link -- link to the thread (str)
        title -- of the thread (str)
        comments_link -- link to the comments (str)
        """

        self._subreddit = subreddit
        self._title = title
        self._comments_link = comments_link
        self._up_votes = Thread.fix_up_votes(up_votes)
        if link[:3] == '/r/':
            link = 'https://old.reddit.com' + link
        self._link = link

    @property
    def subreddit(self):
        return self._subreddit

    @property
    def title(self):
        return self._title

    @property
    def link(self):
        return self._link

    @property
    def comments_link(self):
        return self._comments_link

    @property
    def up_votes(self):
        return self._up_votes

    @staticmethod
    def fix_up_votes(up_votes: str):
        """ Static method that 'fixes' the up votes returned from Reddit.

        Keyword arguments:
        up_votes -- string representation of the number of up votes (str)
                    Eg.: '582' '10.2k' '10.2K' '•'
        """

        if 'k' in up_votes or 'K' in up_votes:
            up_votes = up_votes.replace('k', '').replace('K', '')
            return int(float(up_votes) * 1000)

        if up_votes == '&bull;' or up_votes == '•':
            return 0

        return int(up_votes)

    def __repr__(self):
        return f'(SubReddit: {self._subreddit}, Upvotes: {self._up_votes}, '\
               f'Title: {self._title[:30]}, Link: {self._link[:40]})'


# Regex that captures four groups:
# 1: Number of votes
# 2: Link
# 3: Title
# 4: Link to comments
thread_regex = '<div class="score unvoted".*?>([^<]+)<.*?<a class="title.*?'\
               'href="(.*?)"[^>]*>([^<]*)</a>.*?<li class="first"><a href='\
               '"(.*?)" data-event-action="comments"'
