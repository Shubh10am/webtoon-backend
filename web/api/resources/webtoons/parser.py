from flask_restx import reqparse

webtoon_parser = reqparse.RequestParser()
webtoon_parser.add_argument('title', required=True, help='Title of the webtoon')
webtoon_parser.add_argument('description', required=True, help='Description of the webtoon')
webtoon_parser.add_argument('characters', action='append', required=True, help='List of characters in the webtoon')
