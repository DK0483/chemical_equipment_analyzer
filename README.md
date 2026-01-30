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

![Web Dashboard](screenshots/web_dashboard.png)

### Desktop Application

![Desktop App](screenshots/desktop_app.png)

## Setup Instructions

## Backend Setup (Django)

cd backend
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Web Frontend Setup (React)

### Install Dependencies

cd frontend
npm install
