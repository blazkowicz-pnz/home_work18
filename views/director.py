from flask_restx import Resource, Namespace
from dao.model.director import DirectorSchema
from container import director_service

ns_director = Namespace("directors")

@ns_director.route("/")
class DirectorView(Resource):
    def get(self):
        all_directors = director_service.get_all()
        return DirectorSchema(many=True).dump(all_directors)


@ns_director.route("/<int:did>")
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_one(did)
        return DirectorSchema().dump(director)