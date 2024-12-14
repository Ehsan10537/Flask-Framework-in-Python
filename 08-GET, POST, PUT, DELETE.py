### HTTP verbs PUT and DELETE
### Working with API. we work with JSON files

# In this example we are going to create a to-do list.


from flask import  Flask, render_template, request, jsonify

# what is jsonify? 
"""
In Flask, jsonify is a function used to create a JSON (JavaScript Object Notation) response.
It converts Python data structures (like dictionaries, lists, etc.) into JSON format,
 which is a standard data-interchange format widely used in web applications.
"""

app = Flask(__name__)


#Initial Data in the To-Do list
items =[
    {"id":1, "name":"Item 1", "description":"This is item 1"},
    {"id":2, "name":"Item 2", "description":"This is item 2"}
]

@app.route('/')
def home():
    return "Welcome to the sample To-Do list app"

# GET: Retrieve all the items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET: Retrieve a specific item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"]==item_id), None)
    if item is None:
        return jsonify({"Error":"item not found"})
    else:
        return jsonify(item)
    

# POST: Create a new task --> in POST, we create a new item --> it's an API. it's waiting for something to be sent
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or not ('name' in request.json) or not ('description' in request.json):
        return jsonify({"Error":"item not found"})
    else:
        new_item = {
            "id" : items[-1]['id'] + 1 if items else 1,
            "name" : request.json['name'],
            "description" : request.json['description']
        }

    items.append(new_item)
    return jsonify(new_item)

# PUT : Update an existing item --> in PUT we update an item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"]==item_id), None)
    if item is None:
        return jsonify({"Error":"item not found"})
    else:
        item["name"] = request.json.get('name', item['name'])
        item["description"] = request.json.get('description', item['description'])
        
        return jsonify(item)


# DELETE : Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"result":"Item deleted"})



if __name__ == '__main__':
    app.run(debug=True)


# you can test the API using postman software sending GET, POST, PUT, and DELETE requests to the server.
# you can send along a JSON file usig postman.