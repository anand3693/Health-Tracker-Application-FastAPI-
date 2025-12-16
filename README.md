# 🏃‍♂️ Smart Health Tracker

A FastAPI-based health tracking application that allows users to monitor fitness goals, track meals and workouts, receive automated hydration reminders, and simulate step counting using asynchronous background tasks.

---

## 🚀 Features

- 👤 User profile creation (name, age, height, weight, fitness goal)
- 🍽️ Goal-based predefined meal suggestions (weight loss / weight gain)
- 🏋️ Goal-based workout recommendations
- ➕ Add custom meals and workouts
- 💧 Automated hydration reminders using async background tasks
- 🚶 Simulated step counting with periodic updates
- 🌐 Simple and responsive HTML + CSS frontend
- ⚡ Built with FastAPI for high performance and scalability

---

## 🛠️ Tech Stack

- **Backend:** FastAPI, Python, asyncio  
- **Frontend:** HTML, CSS (Jinja2 Templates)  
- **Concurrency:** Async background tasks  
- **Server:** Uvicorn  

---

## 📂 Project Structure

health_tracker/
│
├── main.py
├── templates/
│ └── index.html
├── static/
│ └── style.css
├── requirements.txt
└── README.md

1. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

2. Install dependencies
pip install -r requirements.txt

3. Start the FastAPI server
uvicorn main:app --reload

4. Open in browser
http://127.0.0.1:8000
