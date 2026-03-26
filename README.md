# some-fun-rest-api 🚀

A beginner-friendly REST API application built with Python and Flask to demonstrate how REST APIs work.

## What is This?

This project teaches beginner programmers how to:
- Create a REST API using Python
- Use HTTP methods (GET, POST, PUT, DELETE)
- Test APIs with Postman
- Send and receive JSON data
- Understand how web services communicate

## Quick Start

### Prerequisites
- Python 3.7 or higher
- Postman (https://www.postman.com/downloads/)

### Installation

#### Step 1: Navigate to the Project Folder
```bash
cd some-fun-rest-api
```

#### Step 2: Create a Virtual Environment

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows (Command Prompt):**
```bash
python -m venv venv
venv\Scripts\activate
```

**On Windows (PowerShell):**
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

> ℹ️ **What is a virtual environment?**
> It's an isolated Python environment for your project. It prevents conflicts with other Python projects. After activation, you'll see `(venv)` in your terminal prompt.

#### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

> ℹ️ **Why `pip` works now:** Inside the virtual environment, `pip` works on macOS/Linux. You don't need `pip3` anymore.

#### Step 4: Run the API

```bash
python app.py
```

You should see:
```
 * Running on http://localhost:5001
 * Debug mode: on
```

#### Step 5: Test in Postman or Browser

1. Open Postman or your browser
2. Go to `http://localhost:5001/`
3. You should see: `{"message": "Welcome to the REST API! Visit /tasks to get started."}`

#### Step 6: Stop the Server

Press `Ctrl+C` in your terminal.

#### Step 7: Deactivate the Virtual Environment (Optional)

When you're done developing:
```bash
deactivate
```

---

## Platform Differences Guide

### macOS/Linux vs Windows

| Task | macOS/Linux | Windows (CMD) | Windows (PowerShell) |
|------|-----------|---------------|---------------------|
| **Create venv** | `python3 -m venv venv` | `python -m venv venv` | `python -m venv venv` |
| **Activate venv** | `source venv/bin/activate` | `venv\Scripts\activate` | `venv\Scripts\Activate.ps1` |
| **Run API** | `python app.py` | `python app.py` | `python app.py` |
| **Deactivate venv** | `deactivate` | `deactivate` | `deactivate` |

### Key Differences Explained

**1. Virtual Environment Activation:**
- **macOS/Linux**: Uses forward slashes `/` and `source` command
- **Windows**: Uses backslashes `\` and different activation scripts

**2. Python Command:**
- **macOS/Linux**: Often need `python3` (since `python` might refer to Python 2)
- **Windows**: Usually just `python` works for Python 3

**3. Path Separators:**
- **macOS/Linux**: `venv/bin/activate`
- **Windows**: `venv\Scripts\activate`

### Windows PowerShell Special Notes

If you get an error like: `cannot be loaded because running scripts is disabled`

Run this first (one time):
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then proceed with activating the virtual environment.

---

## 📚 Documentation

### For Learning the Concepts
Read **[REST_API_CONCEPTS.md](REST_API_CONCEPTS.md)** to understand:
- What REST APIs are
- HTTP methods (GET, POST, PUT, DELETE)
- How to work with JSON
- Status codes and responses

### For Testing the API
Follow **[POSTMAN_GUIDE.md](POSTMAN_GUIDE.md)** to:
- Test each endpoint step-by-step
- Learn how to use Postman
- Try different request types
- Understand response codes

### Learning the Code
Read **[app.py](app.py)** - It's heavily commented with:
- Explanations for each route
- What each HTTP method does
- How to test each endpoint
- Python best practices

---

## Quick API Reference

| Method | Endpoint | Purpose | Example |
|--------|----------|---------|---------|
| GET | `/tasks` | Get all tasks | Fetch your entire to-do list |
| GET | `/tasks/1` | Get one task | Fetch task #1 |
| POST | `/tasks` | Create new task | Add a new task |
| PUT | `/tasks/1` | Update task | Edit task #1 |
| DELETE | `/tasks/1` | Delete task | Remove task #1 |

---

## Example: Create a New Task

### Using Postman:
1. **Method**: POST
2. **URL**: `http://localhost:5000/tasks`
3. **Body** (JSON):
   ```json
   {
       "title": "Learn REST APIs"
   }
   ```
4. Click "Send"

### Response (201 Created):
```json
{
    "id": 4,
    "title": "Learn REST APIs",
    "completed": false
}
```

---

## File Structure

```
├── README.md                    # This file
├── app.py                       # Main REST API application
├── requirements.txt             # Python dependencies
├── REST_API_CONCEPTS.md         # Theory and concepts
└── POSTMAN_GUIDE.md            # Step-by-step Postman testing guide
```

---

## Features

✅ **Easy to Understand**
- Simple task management API
- Clear comments explaining everything
- Perfect for beginners

✅ **All CRUD Operations**
- Create (POST)
- Read (GET)
- Update (PUT)
- Delete (DELETE)

✅ **Complete Documentation**
- Concept explanations
- Step-by-step Postman guide
- In-code comments

✅ **Error Handling**
- 404 for missing resources
- 400 for invalid requests
- Clear error messages

✅ **Ready to Run**
- No database setup needed
- In-memory storage
- Single command to start

---

## What You'll Learn

By working through this project, you'll understand:

1. **HTTP Fundamentals**
   - Different HTTP methods and when to use them
   - Status codes and what they mean
   - Request/response structure

2. **REST Principles**
   - URLs as resources
   - Standard CRUD operations
   - Stateless communication

3. **Python Web Development**
   - Flask framework basics
   - Routing and request handling
   - JSON serialization

4. **API Testing**
   - Using Postman to test APIs
   - Reading API responses
   - Debugging requests

5. **Data Handling**
   - JSON format
   - Request bodies
   - Response formatting

---

## Next Steps

**Once you understand this API, try:**

1. **Add more fields** to tasks (priority, due date, description)
2. **Add a database** (SQLite, PostgreSQL)
3. **Add authentication** (API keys, tokens)
4. **Deploy to the internet** (Heroku, AWS, Railway)
5. **Build a frontend** (React, Vue, plain HTML+JavaScript)
6. **Use a different framework** (Django, FastAPI)

---

## Troubleshooting

### Getting 403 Forbidden on macOS?
**Common issue:** macOS uses port 5000 for AirTunes. Change the port:

1. Open [app.py](app.py)
2. Change the last line from:
   ```python
   app.run(debug=True, host="localhost", port=5000)
   ```
   to:
   ```python
   app.run(debug=True, host="localhost", port=5001)
   ```
3. Save and restart the API
4. In Postman, use: `http://localhost:5001/`

### Port 5000 already in use (or any other port)?
If you get a "Address already in use" error, try a different port:
```python
app.run(debug=True, host="localhost", port=5002)
```
(Or any number between 3000-8000)

### Module not found error?
Make sure you installed dependencies:
```bash
pip install -r requirements.txt
```
And that your virtual environment is activated (you should see `(venv)` in your prompt)

### Can't connect in Postman?
1. ✅ Make sure the API is running (`python app.py`)
2. ✅ Use `http://` not `https://`
3. ✅ Double-check your port number matches what you set in `app.py`
4. ✅ Try in your browser first: `http://localhost:5000/` (or whatever port you set)
5. ✅ Check the terminal - look for error messages

### Getting "Module not found: flask"?
Your virtual environment isn't activated. Do this:
```bash
source venv/bin/activate
python app.py
```
You should see `(venv)` in your terminal prompt.

---

## Resources for Further Learning

- **Flask Documentation**: https://flask.palletsprojects.com/
- **HTTP Methods**: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
- **REST API Design**: https://restfulapi.net/
- **JSON Format**: https://www.json.org/
- **Postman Learning Center**: https://learning.postman.com/

---

## License

This project is provided as educational material for students.

---

**Happy Learning! 🎓** Start with [REST_API_CONCEPTS.md](REST_API_CONCEPTS.md) to understand the theory, then follow [POSTMAN_GUIDE.md](POSTMAN_GUIDE.md) to practice!
