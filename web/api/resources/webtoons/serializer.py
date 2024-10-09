from flask_restx import Api, fields

api = Api(version="1.0",
          title="Webtoons API",
          description="API to manage your Webtoons", ui=False)


display_user_serializer = api.model("User details", {
    "id": fields.String(description="Unique identifier for the webtoon"),
    "title": fields.String(description="Title of the webtoon"),
    "description": fields.String(description="Description of the webtoon"),
    "characters": fields.List(fields.String(), description="List of characters in the webtoon"),
    "created_at": fields.DateTime(description="Creation timestamp of the webtoon"),
    "updated_at": fields.DateTime(description="Last updated timestamp of the webtoon")
})
