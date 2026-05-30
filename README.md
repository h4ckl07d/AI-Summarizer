# 🧠 Smart Text Summarizer

An AI-powered REST API that takes any text and returns a clean, concise summary. Built with Python and FastAPI, powered by GPT-OSS 120B via Groq, and deployed on Render.

> Built during the **GDG On Campus FUTA — AI-Cloud Workshop** · 30th May, 2026

---

## 🚀 Live Demo

**Base URL:** `https://ai-summarizer-337d.onrender.com`

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Health check |
| `/summarize` | POST | Summarize any text |

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.12 |
| Framework | FastAPI |
| AI Model | GPT-OSS 120B (via Groq) |
| Deployment | Render |
| Testing | Postman |

---

## 📦 Getting Started

### Prerequisites
- Python 3.9 or above
- A free [Groq API key](https://console.groq.com)

### Installation

```bash
# Clone the repository
git clone https://github.com/h4ckl07d/AI-Summarizer.git
cd AI-Summarizer

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Mac / Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root of the project:

```env
GROQ_API_KEY=your-groq-api-key-here
PORT=8080
```

> Get your free API key at [console.groq.com](https://console.groq.com)

### Run Locally

```bash
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

The API will be running at `http://localhost:8080`

---

## 📡 API Reference

### Health Check

```http
GET /
```

**Response**
```json
{
  "status": "ok",
  "message": "Summarizer is running!"
}
```

---

### Summarize Text

```http
POST /summarize
Content-Type: application/json
```

**Request Body**

| Field | Type | Required | Description |
|---|---|---|---|
| `text` | string | Yes | The text to summarize (min. 50 characters) |

**Example Request**
```json
{
  "text": "Artificial intelligence is transforming industries at an unprecedented pace. From healthcare to finance, companies are adopting machine learning models to automate complex tasks and improve decision-making. However, this rapid adoption raises important questions around ethics, data privacy, and the need for regulatory frameworks. Experts argue that while AI can augment human capabilities, there must be careful governance to ensure technologies are developed responsibly."
}
```

**Example Response**
```json
{
  "success": true,
  "summary": "AI is rapidly transforming industries through machine learning, improving decision-making and automating tasks. However, its adoption raises concerns around ethics and data privacy, with experts calling for careful governance to ensure responsible development.",
  "characters_processed": 462
}
```

**Error Responses**

| Status | Description |
|---|---|
| `400` | Text is empty or less than 50 characters |
| `500` | Failed to generate summary |

---

## 📁 Project Structure

```
ai-summarizer/
├── main.py            ← FastAPI application
├── .env               ← Environment variables (not committed)
├── requirements.txt   ← Project dependencies
├── .gitignore         ← Files excluded from git
└── README.md          ← You are here
```

---

## 🔒 Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | Your Groq API key from console.groq.com |
| `PORT` | Port to run the server on (default: 8080) |

> ⚠️ Never commit your `.env` file. It is listed in `.gitignore` to keep your API key safe.

---

## 🌐 Deployment

This project is deployed on [Render](https://render.com) using the following settings:

| Setting | Value |
|---|---|
| Runtime | Python 3 |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn main:app --host 0.0.0.0 --port 8080` |
| Instance Type | Free |

Environment variable `GROQ_API_KEY` is set in the Render dashboard.

---

## 🤝 Contributing

This project was built as a workshop demo. Feel free to fork it and extend it with:

- A frontend interface
- Additional endpoints (keyword extraction, tone detection, translation)
- Authentication with API keys
- Request logging and monitoring

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

*GDG On Campus FUTA · AI-Cloud Workshop · 30th May, 2026*