from flask import Flask, request, json, escape
import pickle

model_file = 'model/decision_tree.pkl'

def main(request):
    """ Responds to an HTTP request using data from the request body parsed
    according to the "content-type" header.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    
    model = pickle.load(open(model_file,"rb"))
    content_type = request.headers['content-type']

    if content_type == 'application/json':
        request_json = request.get_json(silent=True)
        if request_json and 'data' in request_json:
            data = request_json['data']
            x = [data["data"]]
            prediction = model.predict(x)[0]
            result = {"result": prediction}
        else:
            raise ValueError("JSON is invalid, or missing a 'data' property")
    else:
        raise ValueError("Unknown content type: {}".format(content_type))

    return json.dumps(result)