from flask import Flask
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app)

KV_STORE = {}


post_args = reqparse.RequestParser()
post_args.add_argument("key", type=str, help="Key is required", required=True)
post_args.add_argument("value", type=str, help="Value is required", required=True)

put_args = reqparse.RequestParser()
put_args.add_argument("key", type=str)
put_args.add_argument("value", type=str)

def abort_record_does_not_exit():
    abort(404, message="Record ID does not exit ...")


class KVStoreList(Resource):
    def get(self):
        return KV_STORE


class KVStore(Resource):
    def get(self, myname):
        if myname not in KV_STORE:
            abort_record_does_not_exit()
            return KV_STORE
        return KV_STORE[myname]

    def post(self, myname):
        args = post_args.parse_args()
        if myname in KV_STORE:
            abort(409, message="The object already exist")
        KV_STORE[myname] = {"key": args["key"], "value": args["value"]}
        print(KV_STORE[myname])
        return KV_STORE[myname], 201

    def put(self, myname):
        args = put_args.parse_args()
        if myname not in KV_STORE:
            abort(404, message="Key does not exist, Can not update")
        if args["key"]:
            KV_STORE[myname]["key"] = args["key"]
        if args["value"]:
            KV_STORE[myname]["value"] = args["value"]
        return KV_STORE[myname]

    def delete(self, myname):
        if myname not in KV_STORE:
            abort(404, message="Record does not exist, Can not update")
        del KV_STORE[myname]
        return 200





api.add_resource(KVStoreList, '/kvstore')

api.add_resource(KVStore, '/kvstore/<string:myname>')


if __name__ == "__main__":
    app.run(debug=True)
