from flask import request
from flask_restx import Namespace, Resource
from dao.model.movie import MovieSchema
from container import movie_service

ns_movie = Namespace("movies")

# director_id = request.args.get("director_id", type=int)
# genre_id = request.args.get("genre_id", type=int)
# year = request.args.get("year", type=int)

@ns_movie.route("/")
class MovieView(Resource):
    def get(self):
        all_movies = movie_service.get_all()
        return MovieSchema(many=True).dump(all_movies)


    def post(self):
        req_json = request.json
        movie_service.create(req_json)

        return "", 201


@ns_movie.route("/<int:mid>")
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return MovieSchema().dump(movie), 200


    def put(self, mid):
        req_data = request.json
        req_data["id"] = mid
        movie_service.update(req_data)

        return "", 204


    def patch(self, mid):
        req_data = request.json
        req_data["id"] = mid

        movie_service.update_partial(req_data)

        return "", 204

    def delete(self, mid):
        movie_service.delete(mid)
        return "", 204


if __name__ == "__main__":
    application.run(debug=True)



