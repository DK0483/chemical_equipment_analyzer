# Chemical Equipment Parameter Visualizer

An industrial dashboard to analyze chemical equipment performance using CSV data.

## Project Overview

This project simulates an industrial monitoring system used in chemical plants
to analyze equipment health, detect abnormal behavior, and recommend corrective actions.

## Key Engineering Highlights

- Threshold-based risk detection (pressure & temperature)
- Health score calculation for overall system status
- Actionable recommendations for operators
- Interactive visual analytics (bar, line charts)
- Dark/Light industrial dashboard UI
- Exportable insights for reporting (CSV / JSON)

## Tech Stack

- Frontend : React + Chart.js (Visualization & UI)
- Backend : Django REST Framework (API & analytics)
- Data Processing : Pandas for analytics (health scoring & insights)

## Application Screenshots

### Web Application

![Web Dashboard](photos/web-1.jpeg)
![Web Dashboard](photos/web-2.jpeg)
![Web Dashboard](photos/web-3.jpeg)

### Desktop Application

![Desktop App](photos/desktop_app-1.jpeg)

## Setup Instructions

## Backend Setup (Django)

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Web Frontend Setup (React)

### Install Dependencies

```bash
cd frontend
npm install
```

## Desktop Application Setup (PyQt5)

The desktop application provides an offline industrial dashboard with the same
analytics, charts, and insights as the web frontend.

### Prerequisites

- Python 3.9+
- Virtual environment (recommended)
- Backend API running locally

### Setup Steps

1. Navigate to the desktop app directory:
   ```bash
   cd desktop-app
   ```
2. Create and activate virtual environment:
   python -m venv venv
   source venv/bin/activate # macOS / Linux
   venv\Scripts\activate # Windows
3. Install required dependencies:
   pip install pyqt5 matplotlib requests
4. Start backend server (from project root):
   python manage.py runserver
5. python manage.py runserver
   python main.py

## Demo & Live Links

### 🎥 Project Demo Video

Watch the complete walkthrough of the web and desktop application:  
👉 **Video Demo:** https://youtu.be/YOUR_VIDEO_LINK_HERE

### 🌐 Live Web Application

Access the deployed web dashboard:  
👉 **Live URL (Netlify):** https://your-project-name.netlify.app

> Note: Backend API must be running locally or hosted for full functionality.
