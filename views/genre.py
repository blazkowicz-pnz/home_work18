from flask_restx import Resource, Namespace
from dao.model.genre import GenreSchema
from container import genre_service

ns_genre = Namespace("genres")

@ns_genre.route("/")
class GenreView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return GenreSchema(many=True).dump(all_genres)


@ns_genre.route("/<int:gid>")
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get_one(gid)
        return GenreSchema().dump(genre)