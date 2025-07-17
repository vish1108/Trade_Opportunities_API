# Trade Opportunity API

This is a FastAPI-based backend for analyzing and identifying potential trade opportunities from financial data.

## 🚀 Features

- Analyze trading signals and opportunities
- Token-based authentication
- FastAPI Swagger UI for interactive API testing

## 🛠️ Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

## 📦 Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/vish1108/Trade_Opportunities_API.git
   cd Trade_Opportunities_API

2. Project setup:
   ```bash
   python -m venv venv
## On Windows
venv\Scripts\activate
## On Unix/macOS
source venv/bin/activate

3. Requrements
    ```bash
    pip install -r requirements.txt

4. Create a .env file in the root folder and add your Gemini API key:
   ```bash
   GEMINI_API_KEY=your_api_key_here

5. Start the project
   ```bash
   uvicorn main:app --reload --port 8001

Open your browser and go to:
   
   http://127.0.0.1:8000/docs

## Click on Authorization button
Authorization: test-token

then select the industry which question you want to find





