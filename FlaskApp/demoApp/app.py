from flask import Flask, request, jsonify

app = Flask("__main__")

# In-memory store (non-persistent storage)
store = [
    {
        "name": "Fresh Fruits Store",
        "item": [
            {
                "name": "Apple",
                "price": 3.5  # Price per unit
            },
            {
                "name": "Banana",
                "price": 0.5  # Price per unit
            }
        ]
    },
    {
        "name": "Organic Fruits Corner",
        "item": [
            {
                "name": "Mango",
                "price": 2.0  # Price per unit
            },
            {
                "name": "Strawberry",
                "price": 4.0  # Price per unit
            }
        ]
    }
]


# Route handling both GET and POST methods
@app.route("/store", methods=["GET", "POST"])
def handle_store():
    # Handle GET request: Return the store data
    if request.method == "GET":
        return jsonify({"store": store}), 200  # Return JSON with a success status code

    # Handle POST request: Add a new store
    elif request.method == "POST":
        # Get the JSON payload from the request
        data = request.get_json()

        # Validate input (Best Practice)
        if not data or "name" not in data or "item" not in data:
            return jsonify({"error": "Invalid input, 'name' and 'item' are required."}), 400  # Bad Request

        # Add the new store to the in-memory store
        new_store = {
            "name": data["name"],
            "item": data["item"]
        }
        store.append(new_store)

        return jsonify(new_store), 201  # Return the created store with a success status code

# In-memory storage for unimplemented route requests
unimplemented_routes = {}

@app.route("/store/<string:name>/item", methods=["GET", "POST"])
def create_item(name):
    data = request.get_json()
    if request.method == "POST":
        for store_name in store:
            if store_name["name"] == name:
                new_item = { "name": data["name"], "price": data["price"] }
                store_name["item"].append(new_item)
                return new_item, 201
        return {"message": "store notfound"}, 404
    if request.method == "GET":
        return {"message": "Under Development"}, 404






@app.route("/unimplemented-routes", methods=["GET"])
def fetch_unimplemented_routes():
    """
    Endpoint to fetch all unimplemented routes and their request counts.
    """
    return jsonify({"unimplemented_routes": unimplemented_routes}), 200

# <string:route>: Matches /test, but not /test/endpoint.
# <path:route>: Matches both /test and /test/endpoint.
# The <path> type allows capturing the full path of the URL after /, including any slashes (/).
# The value of route will be passed as a string to the associated function.
@app.route("/<path:route>", methods=["GET", "POST", "PUT", "DELETE"])
def wildcard_route(route):
    """
    Wildcard route to handle unimplemented endpoints.
    """
    # Track the requested route in the dictionary
    if route in unimplemented_routes:
        unimplemented_routes[route] += 1
    else:
        unimplemented_routes[route] = 1

    # Return a friendly message to the user
    return jsonify({
        "message": "Currently, this route is not available. We will try to implement it based on user demand.",
        "route_requested": route,
        "request_count": unimplemented_routes[route]
    }), 404  # Use 404 status code to indicate "Not Found"

# @app.get("/store")
# def get_store():
#     return {
#         "store": store
#     }
# @app.post("/store")
# def create_store():
#     new_store = request.get_json()
#     store.append(
#         {
#             "name": new_store.get("name"),
#             "item": []
#         }
#     )
#     return store, 201


#
if __name__ == "__main__":
    app.run(debug=True, reload=True)