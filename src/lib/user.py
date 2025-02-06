    # if request.method == "GET":
    #     with open("users.json", "r") as f:
    #         data = json.load(f)
    #         data.append({
    #             "username": "user4",
    #             "pets": ["hamster"]
    #         })
    #         return flask.jsonify(data)
    # if request.method == "POST":
    #     received_data = request.get_json()
    #     print(f"received data: {received_data}")
    #     message = received_data['data']
    #     return_data = {
    #         "status": "success",
    #         "message": f"received: {message}"
    #     }
    #     return flask.Response(response=json.dumps(return_data), status=201)

def save_user():
    print('Saving user data')