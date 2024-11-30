
# QuotesApp: Scalable Multi-Service Application

## Overview
**QuotesApp** is a containerized, multi-service application designed to serve inspirational quotes efficiently. It uses:

- **FastAPI**: A high-performance backend framework for API development.
- **MongoDB**: A NoSQL database for managing and storing quotes.
- **NGINX**: A lightweight web server and reverse proxy for load balancing and scaling.

The application is orchestrated using Docker Compose, enabling seamless deployment and scalability.

---

## Features
- 🚀 **FastAPI**: High-performance, asynchronous API for serving and managing quotes.
- 📦 **MongoDB**: Secure and scalable NoSQL database for data persistence.
- 🔄 **NGINX**: Reverse proxy and load balancer for efficient scaling.
- 🛠️ **Docker Compose**: Simplified service orchestration for development and production environments.

---

## Prerequisites
Ensure the following tools are installed on your system:
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.10+](https://www.python.org/downloads/) (for development)

---

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Amit145/QuotesApp.git
cd QuotesApp
```

### 2. Set Up Environment Variables
Create a `.env` file in the root directory to store configuration variables. For example:
```
MONGO_INITDB_ROOT_USERNAME=admin
MONGO_INITDB_ROOT_PASSWORD=admin123
MONGO_DB=quotesdb
```

### 3. Start the Application
Use Docker Compose to start all services:
```bash
docker-compose up --build
```

### 4. Access the Application
- **Backend API**: Visit `http://localhost:90/docs` for the Swagger UI.
- **Frontend (via NGINX)**: Access the app at `http://localhost`.

---

## Project Structure
```plaintext
QuotesApp/
├── backend/                # FastAPI backend
│   ├── main.py             # API routes and logic
│   ├── database.py         # MongoDB connection setup
│   ├── models.py           # Data models for the API
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # Docker configuration for FastAPI
├── nginx/
│   ├── nginx.conf          # NGINX configuration for load balancing
│   └── Dockerfile          # Docker configuration for NGINX
├── docker-compose.yml      # Docker Compose configuration
├── README.md               # Project documentation
└── sample_quotes.txt       # Sample quotes for populating MongoDB
```

---

## API Endpoints

### Base URL: `http://localhost:8000`
1. **GET /quotes**
   - Fetches all quotes from the database.
2. **POST /quotes**
   - Adds a new quote to the database.
   - Request Body:
     ```json
     {
       "author": "Author Name",
       "text": "Inspirational Quote"
     }
     ```

---

## Development Guide

### Backend Development
1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the FastAPI app locally:
   ```bash
   uvicorn main:app --reload
   ```

### NGINX Configuration
The `nginx.conf` file is pre-configured for reverse proxy and load balancing. Modify it as needed for specific use cases.

---

## Contributing
We welcome contributions! Please fork the repository, make changes, and submit a pull request. 

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to modify or add additional details! Let me know if you need further assistance.