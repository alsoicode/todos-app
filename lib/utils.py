import json


def jsonify(value):
    return json.dumps(value, ensure_ascii=False)
