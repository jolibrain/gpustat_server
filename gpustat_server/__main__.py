import json

from flask import Flask, Response
from gpustat import GPUStatCollection

app = Flask('gpustat_server')


def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError(type(obj))


@app.route("/")
def gpustat_server():
    stats = GPUStatCollection.new_query()
    rep = Response(json.dumps(stats.jsonify(), default=date_handler),
                   mimetype='application/json')
    rep.headers = {**rep.headers,
                   **{'Access-Control-Allow-Origin': '*',
                      'Access-Control-Allow-Methods': 'GET'}}
    return rep


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Serve gpustat on given host:port")

    parser.add_argument("--host", default="localhost")
    parser.add_argument("--port", type=int, default=12345)

    app.run(**vars(parser.parse_args()))
