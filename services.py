from flask import Blueprint
from flask_restplus import fields, Api, Resource
from werkzeug.exceptions import BadRequest

from app import application


api = Api(application,
          title='Flask MLR POC',
          description='Proof of Concept for Flask Microservices',
          default='mlr_poc',
          default_label='MLR POC',
          doc='/api')

message_model = api.model('MessageModel', {
    'message' : fields.String,
})

hello_model = api.inherit('HelloModel', message_model, {
    'message' : fields.String('Hello'),
    'name': fields.String
})

@api.route('/hello')
@api.route('/hello/<name>')
class HelloWorld(Resource):
    @api.marshal_with(hello_model)
    @api.doc(params={'name': 'Name to say hello to. Defaults to World'})
    def get(self, name='World'):
        return {
            'message': 'hello',
            'name': name
        }
    @api.marshal_with(hello_model)
    @api.doc(params={'name': 'Name to say hello to'},
             responses={201: "Created"})
    def post(self, name):
        if name:
            return {
                'message': 'hello',
                'name' : name
            }, 201
        else:
            raise BadRequest('No name')

@api.route('/message/<msg>')

class Message(Resource):
    @api.marshal_with(message_model)
    def get(self, msg):
        return {
            'message': msg
        }
    @api.marshal_with(message_model)
    @api.doc(responses={201: "Created"})
    def post(self, msg):
        return {
            'message': msg,
        }, 201


