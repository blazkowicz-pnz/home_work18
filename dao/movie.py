from dao.model.movie import Movie
# from views.movie import director_id, genre_id, year

class MovieDAO:
    def __init__(self, session):
        self.session = session


    def get_one(self, mid):
        return self.session.query(Movie).get(mid)


    def get_all(self):
        # movies =
        # if director_id:
        #     movies = self.session.query(Movie).filter(Movie.director_id == director_id)
        return self.session.query(Movie).all()





    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

        return movie


    def update(self, movie):

        self.session.add(movie)
        self.session.commit()

        return movie


    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()
