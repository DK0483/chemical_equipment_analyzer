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

## How to Run

1. Start backend: `python manage.py runserver`
2. Start frontend: `npm start`
3. Upload CSV to visualize insights
