from datafilereaders.movie_file_csv_reader import MovieFileCSVReader

def test_read():
    test = MovieFileCSVReader('datafiles\\Data1000Movies.csv')
    test.read_csv_file()

    assert len(test.dataset_of_movies) == 1000
    assert len(test.dataset_of_actors) == 1985
    assert len(test.dataset_of_directors) == 644
    assert len(test.dataset_of_genres) == 20
