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
    'message' : fields.String(description='Message to deliver'),
})


@api.route('/hello/<name>')
class HelloWorld(Resource):
    @api.marshal_with(message_model)
    def get(self, name):
        return {
            'message': 'Hello {0}'.format(name),
        }

    @api.doc(responses={201: "Created"})
    @api.marshal_with(message_model)
    def post(self, name):
        if name == 'This':
            raise BadRequest('No name')
        else:
            return {
                'message': 'Hello {0}'.format(name)
            }, 201

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


