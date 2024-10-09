from flask_jwt_extended import create_access_token, jwt_required
from flask_restx import Resource, Namespace
from web.api.resources.webtoons.model import Webtoon
from web.api.resources.webtoons.parser import webtoon_parser
from web.api.resources.webtoons.serializer import display_user_serializer
from web.api.resources.webtoons.utils import data_envelope, format_response

ns = Namespace("User API", description="API to interact with User app", path="/perform")


@ns.route('/create-token')
class Login(Resource):
    @staticmethod
    def post():
        """API To Create Access Token in Order To Access All APIs"""

        username = "shubh"
        password = "shubh@12"

        if username == "shubh" and password == "shubh@12":
            access_token = create_access_token(identity=username)
            return format_response(None, 200, "Login successful", custom_ob=access_token)

        return format_response(None, 401, "Invalid credentials")


@ns.route('/webtoons')
class WebToons(Resource):
    @staticmethod
    def get():
        """API To Fetch All Webtoons Details"""

        webtoons = Webtoon.objects()

        data = [webtoon.to_dict(webtoon) for webtoon in webtoons]
        return format_response(None, 200, "Webtoons fetched successfully", custom_ob=data)

    @ns.expect(webtoon_parser, validate=True)
    @jwt_required()
    def post(self):
        """API To Add A Webtoons Details"""

        args = webtoon_parser.parse_args()
        title = args['title']
        description = args['description']
        characters = args['characters']

        webtoons = Webtoon()
        webtoons.webtoons_id = webtoons.generate_id()
        webtoons.title = title
        webtoons.description = description
        webtoons.characters = characters
        webtoons.save()

        return format_response(None, 200, "New Webtoon Entry Added")


@ns.route("/webtoons/<string:webtoons_id>")
class GetProfileDetails(Resource):
    @ns.marshal_with(data_envelope(display_user_serializer))
    def get(self, webtoons_id):
        """API To Fetch A Specific Webtoons Detail"""

        data = Webtoon.objects(webtoons_id=webtoons_id).first()
        if not data:
            return format_response(None, 400, "No Webtoons Found from this ID")

        return format_response(data, 200, "Webtoons Fetched Successfully")


@ns.route("/webtoons/<string:webtoons_id>")
class GetProfileDetails(Resource):
    @jwt_required()
    @ns.marshal_with(data_envelope(display_user_serializer))
    def delete(self, webtoons_id):
        """API To Delete A Specific Webtoons Detail"""

        data = Webtoon.objects(webtoons_id=webtoons_id).first()
        if not data:
            return format_response(None, 400, "No Webtoons details found from this webtoon ID")
        data.delete()

        return format_response(None, 200, "Webtoons Deleted Successfully")
