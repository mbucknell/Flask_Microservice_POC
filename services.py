from flask import request
from flask_restplus import fields, Api, Resource

from app import application

api = Api(application)

message_model = api.model('HelloModel', {
    'message' : fields.String,
    'name' : fields.String
})

@api.route('/hello')
@api.route('/hello/<name>')
class HelloWorld(Resource):
    @api.marshal_with(message_model)
    def get(self, name='World'):
        return {
            'message': 'hello',
            'name': name
        }

    def put(self):
        return {'message' : 'Not yet implemented'}, 400