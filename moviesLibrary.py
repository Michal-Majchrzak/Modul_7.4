class Movie:
    def __init__(self, title, release_year, genre, number_of_vies):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.number_of_vies = number_of_vies

    def play(self):
        self.number_of_vies = self.number_of_vies + 1

    def __str__(self):
        return f"{self.title} ({self.release_year})"

class TVSeries(Movie):
    def __init__(self, season_no, episode_no, *args, **kwargs)
        super().__init__(*args, **kwargs)
        self.season_no = season_no
        self.episode_no = episode_no

    def __str__(self):
        return f"{self.title} S{self.season_no}E{self.episode_no}"