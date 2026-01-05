# Gold Rate API 📈

A lightweight Free to use FastAPI service that scrapes real-time gold prices (XAU/USD) from TradingView.

Built with [FastAPI](https://fastapi.tiangolo.com/) • Hosted on [Render](https://render.com)

---

## Features

- 🔄 Real-time gold price data from TradingView
- ⚡ Fast async scraping with aiohttp
- 🛡️ Rate limiting to prevent abuse
- 📦 Caching to reduce scraping frequency
- 🌐 CORS enabled for frontend integration

---

## Quick Start

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/health` | Health check |
| GET | `/api/v1/gold` | Current gold rate (XAU/USD) |

### Example Request

```bash
curl https://rate.onrender.com/api/v1/gold
```

### Example Response

```json
{
  "gold_rate": 2419.965,
  "cached": false
}
```

---

## Local Development

### Prerequisites

- Python 3.9+

### Installation

```bash
git clone https://github.com/yourusername/gold-rate-api.git
cd gold-rate-api
pip install -r requirements.txt
```

### Run the Server

```bash
uvicorn main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

### Interactive Docs

FastAPI provides automatic documentation:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| FastAPI | Web framework |
| aiohttp | Async HTTP client |
| BeautifulSoup4 | HTML parsing |
| SlowAPI | Rate limiting |
| Uvicorn | ASGI server |

---

## Project Structure

```text
├── main.py           # FastAPI app and routes
├── scrapper.py       # TradingView scraper
├── requirements.txt  # Dependencies
└── README.md
```

---

## Rate Limits

To prevent abuse, the API enforces the following limits:

- **10 requests per minute** per IP address
- Responses are cached for **60 seconds**

Exceeding the limit returns:

```json
{
  "error": "Rate limit exceeded. Try again later."
}
```

---

## Deployment

This project is configured for Render deployment.

| Setting | Value |
|---------|-------|
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn main:app --host 0.0.0.0 --port $PORT` |

---

## Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/awesome`)
3. Commit your changes (`git commit -m 'Add awesome feature'`)
4. Push to the branch (`git push origin feature/awesome`)
5. Open a Pull Request

For bugs or suggestions, please [open an issue](https://github.com/yourusername/gold-rate-api/issues).

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
