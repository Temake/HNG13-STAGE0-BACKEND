# FastAPI Profile Service

A simple FastAPI service that provides profile information with real-time data fetching capabilities.

## Features

- **Health Check Endpoint**: Simple status verification
- **Profile Endpoint**: Returns user profile with timestamp and external data
- **External API Integration**: Fetches cat facts from catfact.ninja
- **Error Handling**: Graceful fallbacks for external API failures

## Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) package manager

## Installation

1. **Clone or navigate to the project directory**
   ```powershell
   cd https://github.com/Temake/HNG13-STAGE0-BACKEND
   ```

2. **Install dependencies using uv**
   ```powershell
   # Create virtual environment and install dependencies
   uv sync
   
   # Or if you need to install from requirements.txt
   uv pip install -r requirements.txt
   ```

## Running the Application

Start the FastAPI development server:

```powershell
# Using uv to run uvicorn
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Or activate the virtual environment first
uv run python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at: `http://127.0.0.1:8000`

## API Endpoints

### GET `/`
**Health Check**
- Returns a simple greeting message
- Used to verify the service is running

**Response:**
```json
{
  "Hello": "World"
}
```

### GET `/me`
**Profile Information**
- Returns user profile with timestamp and a cat fact
- Fetches real-time data from external API
- Includes error handling for external service failures

**Response:**
```json
{
  "status": "success",
  "user": {
    "name": "Teminioluwa Adekoya",
    "email": "teminioluwaopemipo@gmail.com",
    "stack": "Python/FastAPI",
    "linkedIn": "https://www.linkedin.com/in/teminioluwa-adekoya-6537a2294/",
    "github": "https://github.com/temake"
  },
  "timestamp": "2024-10-17T12:00:00.000000+00:00",
  "fact": "Cats have five toes on their front paws, but only four toes on their back paws."
}
```

## Usage Examples

### Using curl
```powershell
# Health check
curl http://127.0.0.1:8000/

# Get profile
curl http://127.0.0.1:8000/me
```

### Using PowerShell
```powershell
# Health check
Invoke-RestMethod -Uri "http://127.0.0.1:8000/" -Method Get

# Get profile
Invoke-RestMethod -Uri "http://127.0.0.1:8000/me" -Method Get
```

## Project Structure

```
backend/
├── main.py              # FastAPI application and route handlers
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── __pycache__/        # Python bytecode cache
```

## Dependencies

The project uses the following main dependencies:
- **FastAPI**: Modern web framework for building APIs
- **httpx**: Async HTTP client for external API calls
- **uvicorn**: ASGI server for running the application

## Development

### Adding New Dependencies
```powershell
# Add a new package
uv add package-name

# Add development dependencies
uv add --dev package-name
```

### Code Quality
The application includes:
- Async/await pattern for non-blocking operations
- Proper error handling with try-catch blocks
- Timeout configuration for external API calls
- JSON response formatting

## Error Handling

The `/me` endpoint includes robust error handling:
- **External API Failures**: Falls back to default message if cat fact API is unavailable
- **Network Timeouts**: 5-second timeout for external requests
- **HTTP Errors**: Graceful handling of HTTP status errors
- **General Exceptions**: Catches and logs unexpected errors

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test the endpoints
5. Submit a pull request

## License

This project is part of the HNG13 Stage 0 backend task.

## Contact

- **Developer**: Teminioluwa Adekoya
- **Email**: teminioluwaopemipo@gmail.com
- **LinkedIn**: [Profile](https://www.linkedin.com/in/teminioluwa-adekoya-6537a2294/)
- **GitHub**: [temake](https://github.com/temake)