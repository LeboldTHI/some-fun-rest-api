# REST API Concepts for Beginners 📚

## What is a REST API?

**REST** = **RE**presentational **S**tate **T**ransfer

A REST API is a way for programs to communicate with each other over the internet using HTTP requests and responses. Think of it like a waiter taking orders and bringing food back to your table.

### Real-World Analogy

Imagine a restaurant:
- **Client** (You) = Your browser or Postman
- **Server** (Restaurant) = Our Flask app
- **Request** (Order) = What you want to do
- **Response** (Food) = The answer you get back

---

## HTTP Methods (CRUD Operations)

REST APIs use HTTP methods to perform different actions:

### GET - Retrieve Data 📖
- **What it does**: Asks the server for information
- **Safe**: Yes (doesn't change anything)
- **Example**: "Give me all tasks" or "Give me task #1"
- **Response**: Returns the requested data

```
GET /tasks → Returns all tasks
GET /tasks/1 → Returns task with ID 1
```

### POST - Create Data ➕
- **What it does**: Sends new data to the server to create something
- **Safe**: No (changes the server)
- **Example**: "Create a new task for me"
- **Response**: Returns the created item with its new ID

```
POST /tasks with body {"title": "New task"}
→ Creates task and returns it with ID assigned
```

### PUT - Update Data ✏️
- **What it does**: Modifies existing data on the server
- **Safe**: No (changes the server)
- **Example**: "Update task #1 to mark it complete"
- **Response**: Returns the updated item

```
PUT /tasks/1 with body {"completed": true}
→ Updates task 1 and returns the updated version
```

### DELETE - Remove Data 🗑️
- **What it does**: Deletes data from the server
- **Safe**: No (changes the server)
- **Example**: "Remove task #1"
- **Response**: Confirms deletion

```
DELETE /tasks/1
→ Removes task 1 and confirms it's gone
```

---

## URL Structure

A REST API URL has meaningful parts:

```
http://localhost:5000/tasks/1
 ↓           ↓      ↓    ↓  ↓
Protocol    Host   Port  Route ID
```

- **Protocol**: `http://` or `https://`
- **Host**: Where the server is running (`localhost` = your computer)
- **Port**: The door through which you communicate (`5000` is Flask default)
- **Route**: The resource you're accessing (`/tasks`)
- **ID**: Specific item identifier (`/1` = task with ID 1)

---

## Request vs Response

### Request (What You Send)
A request has:
- **Method**: GET, POST, PUT, DELETE
- **URL**: Where to send it
- **Headers**: Extra information (like "I'm sending JSON")
- **Body**: Data to send (only for POST and PUT)

### Response (What You Get Back)
A response has:
- **Status Code**: Number indicating success/failure
- **Headers**: Extra information about the response
- **Body**: The actual data returned (usually JSON)

---

## HTTP Status Codes

Status codes tell you what happened:

### Success (✅)
- `200 OK` - Request succeeded (usually for GET, PUT, DELETE)
- `201 Created` - Resource created successfully (usually for POST)

### Client Error (❌)
- `400 Bad Request` - You sent invalid data
- `404 Not Found` - The resource doesn't exist
- `405 Method Not Allowed` - You used wrong HTTP method

### Server Error (💥)
- `500 Internal Server Error` - Something broke on the server

---

## JSON - Data Format

JSON is how we send and receive data in REST APIs. It's human-readable and easy to parse.

### JSON Basics

```json
{
    "id": 1,
    "title": "Learn REST APIs",
    "completed": false
}
```

- **Keys** are in quotes: `"id"`, `"title"`
- **Values** after the colon: `1`, `"Learn REST APIs"`, `false`
- **Objects**: Enclosed in `{}`
- **Arrays**: Enclosed in `[]`

### Common Data Types in JSON

```json
{
    "id": 42,              // Number
    "name": "John",        // String (text)
    "active": true,        // Boolean (true/false)
    "tags": ["a", "b"],    // Array (list)
    "address": {           // Object (nested)
        "city": "Berlin",
        "zip": "10115"
    },
    "phone": null          // Null (empty/no value)
}
```

---

## Our Example API - Tasks

Our simple API manages a task list:

```
Resource: /tasks
ID parameter: /tasks/<id>
```

### Available Operations

| Method | URL | Purpose | Example |
|--------|-----|---------|---------|
| GET | `/tasks` | Get all tasks | List your to-do list |
| GET | `/tasks/1` | Get specific task | View task #1 |
| POST | `/tasks` | Create new task | Add "Buy milk" |
| PUT | `/tasks/1` | Update task | Mark task #1 complete |
| DELETE | `/tasks/1` | Delete task | Remove task #1 |

---

## Response Examples

### Successful GET - All Tasks
```json
[
    {
        "id": 1,
        "title": "Learn Python",
        "completed": false
    },
    {
        "id": 2,
        "title": "Build API",
        "completed": true
    }
]
```

### Error - Task Not Found
```json
{
    "error": "Task not found"
}
```
Status Code: `404`

### Successful POST - Create Task
```json
{
    "id": 3,
    "title": "Test Postman",
    "completed": false
}
```
Status Code: `201`

---

## Authentication (Spoiler Alert)

In production APIs, you need **authentication** - proving you are who you say you are.

Common methods:
- **API Key**: A secret code you include in requests
- **Username/Password**: Standard login
- **OAuth**: Third-party login (Google, GitHub)
- **Tokens**: Get a token after login, use it for requests

Our example API has no authentication (for simplicity).

---

## Best Practices

### Naming
- Use **lowercase** for URLs: `/tasks` not `/Tasks`
- Use **plural** nouns: `/tasks` not `/task`
- Use **hyphens** for multi-word URLs: `/user-profiles` not `/userprofiles`

### HTTP Methods
- `GET` only for reading (never changes data)
- `POST` for creating
- `PUT` for updating (entire resource)
- `PATCH` for partial updates (if needed)
- `DELETE` for removing

### Status Codes
- Use correct codes: `201` for created, `200` for OK, `404` for not found
- Consistent errors: Always return `{error: "message"}` format

### Documentation
- Document all endpoints
- Show example requests and responses
- Explain required and optional fields

---

## Next Steps to Learn More

1. **Try the API**: Follow [POSTMAN_GUIDE.md](POSTMAN_GUIDE.md)
2. **Read the code**: Check comments in [app.py](app.py)
3. **Modify it**: Add new fields to tasks (e.g., priority, due date)
4. **Use a database**: Replace in-memory storage with a real database
5. **Add authentication**: Secure the API with API keys or tokens
