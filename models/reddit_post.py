

class RedditPost:
    """
    This model contains basic information about a Reddit post.
    """

    def __init__(self, headline, section=None, date=None, time=None):
        self.headline = headline
        self.section = section
        self.date = date
        self.time = time

    def to_dict(self):
        return {
            "headline": self.headline,
            "section": self.section,
            "date": self.date,
            "time": self.time
        }