# Testing the REST API with Postman

This guide explains how to test each endpoint of the REST API using Postman.

## Setup

1. **Download Postman**: https://www.postman.com/downloads/
2. **Start the API**: Run `python app.py` in your terminal
3. **Open Postman**: Launch the Postman application

## Testing Each Endpoint

### 1. Health Check - Verify API is Running ✅

**Method**: GET  
**URL**: `http://localhost:5000/`

**Steps**:
1. Create a new request (Ctrl+N or Cmd+N)
2. Select "GET" from the dropdown
3. Paste the URL above
4. Click "Send"

**Expected Response**:
```json
{
    "message": "Welcome to the REST API! Visit /tasks to get started."
}
```

---

### 2. Get All Tasks 📋

**Method**: GET  
**URL**: `http://localhost:5000/tasks`

**Steps**:
1. Create a new request
2. Select "GET"
3. Paste the URL
4. Click "Send"

**Expected Response**:
```json
[
    {
        "id": 1,
        "title": "Learn Python",
        "completed": false
    },
    {
        "id": 2,
        "title": "Build a REST API",
        "completed": false
    },
    {
        "id": 3,
        "title": "Test with Postman",
        "completed": false
    }
]
```

---

### 3. Get a Single Task 🔍

**Method**: GET  
**URL**: `http://localhost:5000/tasks/1`

**Steps**:
1. Create a new request
2. Select "GET"
3. Replace `1` with the task ID you want (try 1, 2, or 3)
4. Click "Send"

**Expected Response**:
```json
{
    "id": 1,
    "title": "Learn Python",
    "completed": false
}
```

**Try with non-existent ID** (e.g., `/tasks/999`):
- You'll get a 404 error: `{"error": "Task not found"}`

---

### 4. Create a New Task ➕

**Method**: POST  
**URL**: `http://localhost:5000/tasks`

**Steps**:
1. Create a new request
2. Select "POST"
3. Paste the URL
4. Click on the "Body" tab
5. Select "raw" radio button
6. Choose "JSON" from the dropdown (right side)
7. Paste this in the text area:
   ```json
   {
       "title": "Buy groceries"
   }
   ```
8. Click "Send"

**Expected Response** (Status: 201 Created):
```json
{
    "id": 4,
    "title": "Buy groceries",
    "completed": false
}
```

**Try different titles**:
- `{"title": "Call mom"}`
- `{"title": "Read a book"}`

**Test error handling** - Send without "title" field:
- You'll get a 400 error: `{"error": "Missing 'title' field"}`

---

### 5. Update a Task ✏️

**Method**: PUT  
**URL**: `http://localhost:5000/tasks/1`

**Steps**:
1. Create a new request
2. Select "PUT"
3. Paste the URL and replace `1` with a task ID
4. Click on the "Body" tab
5. Select "raw" and "JSON"
6. Paste this (update only what you want to change):
   ```json
   {
       "title": "Completed: Learn Python",
       "completed": true
   }
   ```
7. Click "Send"

**Expected Response** (Status: 200 OK):
```json
{
    "id": 1,
    "title": "Completed: Learn Python",
    "completed": true
}
```

**Partial updates** - You can update just the title:
```json
{
    "title": "Updated title only"
}
```

Or just the completed status:
```json
{
    "completed": true
}
```

---

### 6. Delete a Task 🗑️

**Method**: DELETE  
**URL**: `http://localhost:5000/tasks/1`

**Steps**:
1. Create a new request
2. Select "DELETE"
3. Paste the URL and replace `1` with a task ID
4. Do NOT put anything in the Body tab
5. Click "Send"

**Expected Response** (Status: 200 OK):
```json
{
    "message": "Task deleted",
    "task": {
        "id": 1,
        "title": "Learn Python",
        "completed": false
    }
}
```

**Verify deletion** - Get all tasks again with GET `/tasks`. The task should be gone!

---

## Understanding HTTP Status Codes

| Code | Meaning | Example |
|------|---------|---------|
| 200 | OK - Request succeeded | GET, PUT, DELETE successful |
| 201 | Created - Resource created | POST successful |
| 400 | Bad Request - Invalid data | Missing required fields |
| 404 | Not Found - Resource doesn't exist | Task with ID 999 doesn't exist |
| 405 | Method Not Allowed | Using GET on a POST endpoint |

---

## Practice Exercise

Try this workflow to master the REST API:

1. ✅ Get all tasks (GET `/tasks`)
2. ✅ Create a new task (POST `/tasks`)
3. ✅ Get that new task (GET `/tasks/{new_id}`)
4. ✅ Update the task (PUT `/tasks/{new_id}`)
5. ✅ Get all tasks again to see the update
6. ✅ Delete the task (DELETE `/tasks/{new_id}`)
7. ✅ Try to get the deleted task (GET `/tasks/{new_id}`) - should return 404

---

## Tips

- **Save Requests**: After creating a request, click "Save" to save it in your workspace
- **Collections**: Group related requests in Collections for better organization
- **Environment Variables**: Use `{{variable}}` to create reusable URLs and data
- **Response Preview**: The response appears at the bottom of Postman after you click Send
- **Status Code**: Look at the colored status code indicator:
  - Green = 2xx (Success)
  - Orange = 4xx (Client Error)
  - Red = 5xx (Server Error)
