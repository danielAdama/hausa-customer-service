# Hausa Customer Service AI

This application is a Flask-based API that uses the LangChain framework and Groq for Natural Language Processing. It enables an AI customer support agent fluent in Hausa to interact conversationally with users.

---
<img width="1680" alt="Screenshot 2024-11-14 at 17 41 19" src="https://github.com/user-attachments/assets/4b97c28d-09a8-4d07-ade2-6009863580b1">

![WhatsApp Image 2024-11-14 at 17 56 17](https://github.com/user-attachments/assets/201adad1-149a-4143-8257-fa8c9d3c7928)

## Features

- **Hausa Language Support**: Receives and responds to messages in Hausa.
- **LLM-Powered**: Utilizes Llama 3 model for generating responses.
- **Flask Backend**: Provides RESTful API endpoints for easy integration.
- **Environment Configuration**: Securely stores and uses API keys via environment variables.
- **CORS Support**: Allows cross-origin requests.
---

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.9+
- Poetry (Python dependency manager)
- A Groq API key

---

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/danielAdama/hausa-customer-service.git
   cd hausa-customer-service/api
   ```

2. **Set up Poetry**:
   Install Poetry globally if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Install dependencies using Poetry**:
   ```bash
   poetry install
   ```

4. **Activate the virtual environment**:
   ```bash
   poetry shell
   ```

---

### Environment Setup

1. **Create a `.env` file** in the `api/` directory with the following content:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

2. Replace `your_groq_api_key_here` with your actual Groq API key.

---

### Running the Application

1. **Start the Flask server**:
   ```bash
   poetry run python main.py
   ```

2. The server will run on `http://127.0.0.1:5000/` by default.

---

### Usage

- **API Endpoint**: `POST /api/assistant/`

- **Request Body**:
  ```json
  {
      "message": "Your message in Hausa here"
  }
  ```

- **Example cURL Command**:
  ```bash
  curl -X POST http://127.0.0.1:5000/api/assistant/ \
       -H "Content-Type: application/json" \
       -d '{"message": "Ina so in taimako"}'
  ```

- **Response**:
  ```json
  {
      "response": "Your AI-generated response in Hausa"
  }
  ```

---

## Directory Structure

```
hausa-customer-service/
├── api/
│   ├── main.py          # Entry point for the Flask application
│   ├── pyproject.toml   # Poetry project configuration
│   ├── poetry.lock      # Dependency lock file
│   └── .env             # Environment variables
├── frontend/            # Frontend assets (if applicable)
└── README.md            # Project documentation
```

---

## License

This project is licensed under the MIT License.

---

For further inquiries, feel free to reach out to [adamadaniel321@gmail.com](mailto:adamadaniel321@gmail.com).
