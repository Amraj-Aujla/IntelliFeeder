from flask import Flask, jsonify, request, Response
from flask_cors import CORS, cross_origin
import requests
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.before_request
def basic_authentication():
    if request.method.lower() == 'options':
        return Response()


@app.route("/api/feed", methods=['GET', 'POST'])
@cross_origin(allow_headers=['Content-Type'])
def handle_request():
    # Define the URL and JSON payload
    #url = "http://10.43.12.121:5000/"
    #payload = {"request": "Left"}
    # response = jsonify({'request': input['request']})
    input = request.get_json()
    print(input['request'])
    if (input['request'] == "Left"):
        return jsonify({'request': "cat-success"})

    
    elif (input['request'] == "Right"):
        return jsonify({'request': "dog-success"})

    elif (input['request'] == "feed-data"):
        return jsonify({'request': "data-success"})
    
    else:
        response = jsonify({'request': "error"})
        response.status_code = 400
        return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)



# # Define the URL and JSON payload
# url = "http://10.43.12.121:5000/"
# payload = {"request": "Left"}

# # Convert the payload to JSON
# json_payload = json.dumps(payload)

# # Set the content type header to JSON
# headers = {"Content-Type": "application/json"}

# # Send the POST request with the JSON payload
# response = requests.post(url, data=json_payload, headers=headers)

# # Print the response
# print(response.text)