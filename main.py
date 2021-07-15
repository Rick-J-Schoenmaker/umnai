from flask import Flask, render_template
from flask_restful import Api, Resource, abort, reqparse
app = Flask(__name__)
api = Api(app)

vin_put_args = reqparse.RequestParser()
vin_put_args.add_argument("Type", type=str, help="Please provide vehicle type", required=True)
vin_put_args.add_argument("Make", type=str, help="Please provide the make of the vehicle... Example Audi", required=True)
vin_put_args.add_argument("Model", type=str, help="Please provide which model this vehicle is", required=True)
vin_put_args.add_argument("Year", type=int, help="Please provide vehicle manufacture year", required=True)
vin_put_args.add_argument("Seat capacity", type=int, help="Please provide the amount of seats present in the vehicle", required=True)
vin_put_args.add_argument("Roof rack availability", type=bool, help="Please provide if the car has roof rack availability")
vin_put_args.add_argument("Haul capacity", type=int, help="Please provide the trucks Haul capacity")
vin_put_args.add_argument("Sidecar availability", type=bool, help="Please provide if the motorcycle has sidecar availability")

vins = {}

def stop_if_vin_non_existing(vin_id):
    if vin_id not in vins:
        abort(404, message="vin is not valid")

def stop_if_vim_exists(vin_id):
    if vin_id in vins:
        abort(409, message="vin already exists")

class Vin (Resource):

    def get(self, vin_id):
        stop_if_vin_non_existing(vin_id)
        return vins[vin_id]

    def put(self, vin_id):
        stop_if_vim_exists(vin_id)
        args = vin_put_args.parse_args()
        vins[vin_id] = args
        return vins[vin_id], 201

    def delete(self, vin_id):
        stop_if_vin_non_existing(vin_id)
        del vins[vin_id]
        return '', 204

api.add_resource(Vin, "/vin/<int:vin_id>")

if __name__ == "__main__":
    app.run(debug=True)


