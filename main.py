from flask import Flask,Blueprint
from Include.Api_calls import *

app = Flask(__name__)
api = Api(app)

app.register_blueprint(api_calls_create)
app.register_blueprint(api_calls_delete)
app.register_blueprint(api_calls_put)
app.register_blueprint(api_calls_get)

api.add_resource(Api_calls_create, "/<string:filetype>")
api.add_resource(Api_calls_delete, "/<string:filetype>/<int:id>")
api.add_resource(Api_calls_get, "/<string:filetype>", "/<string:filetype>/<int:id>")
api.add_resource(Api_calls_put, "/<string:filetype>/<int:id>")

if __name__ == "__main__":
	app.run(debug=False)
