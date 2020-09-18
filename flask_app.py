from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'Status': 'active'}

class Function1(Resource):
    def post(self):

        #post input
        input_json = request.get_json(force=True)

        #return dict
        return jsonify({'result':'result')})



#add api
api.add_resource(HelloWorld, '/')
api.add_resource(Function1,'/classify/')

if __name__ == '__main__':

    app.run(debug=True)
