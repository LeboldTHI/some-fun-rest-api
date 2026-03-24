"""
Simple REST API for Beginners
This is a basic example of how to create a REST API using Python and Flask.
It demonstrates the four main HTTP methods: GET, POST, PUT, and DELETE.
"""

from flask import Flask, request, jsonify

# Create a Flask application
# This is the core of our REST API
app = Flask(__name__)

# In-memory data storage (simple database alternative)
# In production, you would use a real database like PostgreSQL or MongoDB
tasks = [
    {"id": 1, "title": "Learn Python", "completed": False},
    {"id": 2, "title": "Build a REST API", "completed": False},
    {"id": 3, "title": "Test with Postman", "completed": False},
    {"id": 4, "title": "Deploy the API", "completed": False},
    {"id": 5, "title": "Write documentation", "completed": False},
]

# Counter for generating unique task IDs
next_task_id = 6


# ============================================================================
# ROUTE 1: GET - Retrieve all tasks
# URL: http://localhost:5000/tasks
# Method: GET
# Response: List of all tasks
# ============================================================================
@app.route("/tasks", methods=["GET"])
def get_all_tasks():
    """
    Get all tasks.
    Returns a JSON list of all tasks stored in memory.
    """
    return jsonify(tasks), 200


# ============================================================================
# ROUTE 2: GET - Retrieve a single task by ID
# URL: http://localhost:5000/tasks/<id>
# Method: GET
# Response: Single task if found, error message if not found
# ============================================================================
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    """
    Get a single task by ID.
    
    The <int:task_id> syntax tells Flask to:
    1. Extract the task_id from the URL
    2. Convert it to an integer
    """
    # Search for the task with the matching ID
    task = next((t for t in tasks if t["id"] == task_id), None)

    if task is None:
        # Return 404 error if task not found
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task), 200


# ============================================================================
# ROUTE 3: POST - Create a new task
# URL: http://localhost:5000/tasks
# Method: POST
# Body (JSON): {"title": "Your task here"}
# Response: Newly created task
# ============================================================================
@app.route("/tasks", methods=["POST"])
def create_task():
    """
    Create a new task.
    
    To test this in Postman:
    1. Set method to POST
    2. Go to Body tab
    3. Select "raw" and choose "JSON"
    4. Enter: {"title": "Buy groceries"}
    """
    global next_task_id

    # Get JSON data from the request body
    data = request.get_json()

    # Validate that the request contains a "title" field
    if not data or "title" not in data:
        return jsonify({"error": "Missing 'title' field"}), 400

    # Create a new task object
    new_task = {
        "id": next_task_id,
        "title": data["title"],
        "completed": False,
    }

    # Add the task to our list
    tasks.append(new_task)
    next_task_id += 1

    # Return 201 (Created) status code along with the new task
    return jsonify(new_task), 201


# ============================================================================
# ROUTE 4: PUT - Update an existing task
# URL: http://localhost:5000/tasks/<id>
# Method: PUT
# Body (JSON): {"title": "Updated title", "completed": true}
# Response: Updated task
# ============================================================================
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    """
    Update an existing task.
    
    To test this in Postman:
    1. Set method to PUT
    2. URL: http://localhost:5000/tasks/1
    3. Go to Body tab, select "raw" and "JSON"
    4. Enter: {"title": "Updated task", "completed": true}
    """
    # Find the task to update
    task = next((t for t in tasks if t["id"] == task_id), None)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    # Get the JSON data from the request body
    data = request.get_json()

    # Update the task fields if they are provided in the request
    if "title" in data:
        task["title"] = data["title"]
    if "completed" in data:
        task["completed"] = data["completed"]

    return jsonify(task), 200


# ============================================================================
# ROUTE 5: DELETE - Remove a task
# URL: http://localhost:5000/tasks/<id>
# Method: DELETE
# Response: Success message or error
# ============================================================================
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """
    Delete a task by ID.
    
    To test this in Postman:
    1. Set method to DELETE
    2. URL: http://localhost:5000/tasks/1
    3. Send the request
    """
    global tasks

    # Find the index of the task
    task_index = next((i for i, t in enumerate(tasks) if t["id"] == task_id), None)

    if task_index is None:
        return jsonify({"error": "Task not found"}), 200

    # Remove the task from the list
    removed_task = tasks.pop(task_index)

    return jsonify({"message": "Task deleted", "task": removed_task}), 200


# ============================================================================
# ROUTE 6: Health Check - Verify the API is running
# URL: http://localhost:5000/
# Method: GET
# Response: Simple greeting message
# ============================================================================
@app.route("/", methods=["GET"])
def home():
    """
    Welcome endpoint to verify the API is running.
    """
    return jsonify({"message": "Welcome to the REST API! Visit /tasks to get started."}), 200


# ============================================================================
# Error handler for 404 (Not Found)
# ============================================================================
@app.errorhandler(404)
def not_found(error):
    """
    Handle requests to endpoints that don't exist.
    """
    return jsonify({"error": "Endpoint not found"}), 404


# ============================================================================
# Error handler for 405 (Method Not Allowed)
# ============================================================================
@app.errorhandler(405)
def method_not_allowed(error):
    """
    Handle requests using wrong HTTP methods.
    """
    return jsonify({"error": "Method not allowed"}), 405


# Run the application
if __name__ == "__main__":
    # debug=True enables auto-reload when you save changes
    # host='0.0.0.0' makes the API accessible from any machine on your network
    # port=5000 is the default Flask port
    app.run(debug=True, host="localhost", port=5001)
