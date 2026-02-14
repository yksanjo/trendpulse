# TrendPulse - Real-Time GitHub Trending Monitor

<p align="center">
  <img src="https://img.shields.io/badge/Python-FastAPI-00d4aa?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/RealTime-WebSockets-ff6b35?style=for-the-badge&logo=websocket" alt="WebSocket">
</p>

Real-time GitHub trending monitor with live updates, notifications, and trend predictions. Stay ahead of the curve with instant alerts when repos go viral.

## 🌟 Features

- **Real-time Monitoring** - Live WebSocket updates when trending repos change
- **Instant Notifications** - Browser notifications for viral repos
- **Trend Predictions** - ML-powered predictions of which repos will trend
- **Watchlist** - Track specific repos and get alerts
- **Historical Trends** - View trending data over time
- **Multi-language Support** - Track trends across all programming languages

## 🚀 Quick Start

```bash
# Install dependencies
cd backend
pip install -r requirements.txt

# Run the server
python -m uvicorn app.main:app --reload

# Open frontend
cd ../frontend
python -m http.server 8080
```

## 📁 Project Structure

```
trendpulse/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── routers/
│   │   │   ├── trends.py
│   │   │   └── notifications.py
│   │   └── services/
│   │       ├── scraper.py
│   │       ├── websocket_manager.py
│   │       └── predictor.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── app.js
└── README.md
```

## 🔌 API Endpoints

- `GET /api/trends` - Get current trending repos
- `GET /api/trends/stream` - WebSocket for real-time updates
- `POST /api/watchlist` - Add repo to watchlist
- `GET /api/predictions` - Get predicted trending repos

---

Built with ⚡ for developers who want to stay ahead of trends
