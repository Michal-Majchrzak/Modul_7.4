from random import randint
from datetime import datetime


class Movie:
    def __init__(self, title, release_year, genre, number_of_views):
        self._title = title
        self._release_year = release_year
        self._genre = genre
        self._number_of_views = number_of_views

    def __str__(self):
        return f"{self._title} ({self._release_year})"

    @property
    def title(self):
        return self._title

    @property
    def release_year(self):
        return self._release_year

    @property
    def genre(self):
        return self._genre

    @property
    def number_of_views(self):
        return self._number_of_views

    @number_of_views.setter
    def number_of_views(self, views):
        if type(views) is int:
            self._number_of_views = views

    def play(self):
        self._number_of_views = self._number_of_views + 1


class TVSeries(Movie):
    def __init__(self, season_no, episode_no, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._season_no = season_no
        self._episode_no = episode_no

    def __str__(self):
        return f"{self._title} S{self.season_no}E{self.episode_no}"

    @property
    def season_no(self):
        if self._season_no < 10:
            return f"0{self._season_no}"
        else:
            return str(self._season_no)

    @property
    def episode_no(self):
        if self._episode_no < 10:
            return f"0{self._episode_no}"
        else:
            return str(self._episode_no)


class MoviesLibrary:
    def __init__(self):
        self._movies_library = list()

    def get_movies(self):
        movies_list = [movie for movie in self._movies_library if not isinstance(movie, TVSeries)]
        sorted_list = sorted(movies_list, key=lambda movie: movie.title)
        return sorted_list

    def get_series(self):
        tv_series_list = [series for series in self._movies_library if isinstance(series, TVSeries)]
        sorted_list = sorted(tv_series_list, key=lambda series: series.title)
        return sorted_list

    def search(self, title=""):
        for value in self._movies_library:
            if title.lower() == value.title.lower():
                return value
        return None

    def generate_views(self):
        if len(self._movies_library) > 0:
            random_entry_no = randint(0, len(self._movies_library)-1)
            self._movies_library[random_entry_no].number_of_views = randint(1, 100)
        else:
            print("Brak pozycji w bibliotece")

    def generate_views_x10(self):
        for count in range(10):
            self.generate_views()

    def top_titles(self, count, content_type):
        _entries = list()
        if content_type == 'movie':
            _entries = self.get_movies()
        elif content_type == 'series':
            _entries = self.get_series()
        else:
            return _entries
        _entries = sorted(_entries, key=lambda entry: entry.number_of_views, reverse=True)

        return _entries[:count]

    def add_entries(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                entry = line[:-1].split(',')
                if entry[0] == 'tv':
                    _season = randint(1, 8)
                    _episode = randint(1, 24)
                    self._movies_library.append(TVSeries(_season, _episode, entry[1], entry[2], entry[3], 0))
                else:
                    self._movies_library.append(Movie(entry[1], entry[2], entry[3], 0))


if __name__ == "__main__":
    print("Bibiloteka filmow")
    movies_lib = MoviesLibrary()

    movies_lib.add_entries('tv&movie_list.txt')
    movies_lib.generate_views_x10()

    print(f"Najpopularniejsze filmy i seriale dnia {datetime.today().strftime('%d.%m.%Y')}")

    print("\nFilmy :")
    for movie in movies_lib.top_titles(3, 'movie'):
        print(movie)

    print("\nSeriale :")
    for series in movies_lib.top_titles(3, 'series'):
        print(series)
