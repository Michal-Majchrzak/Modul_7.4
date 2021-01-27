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
    def __init__(self, season_no, episode_no, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season_no = season_no
        self.episode_no = episode_no

    def __str__(self):
        return f"{self.title} S{self.season_no}E{self.episode_no}"


def get_movies(library):
    movies_list = [movie for movie in library if not isinstance(movie, TVSeries)]
    sorted_list = sorted(movies_list, key=lambda movie: movie.title)
    return sorted_list


def get_series(library):
    tv_series_list = [series for series in library if isinstance(series, TVSeries)]
    sorted_list = sorted(tv_series_list, key=lambda series: series.title)
    return sorted_list
