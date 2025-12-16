from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import asyncio

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# ------------------ Data Model ------------------
class UserData:
    def __init__(self):
        self.reset()

    def reset(self):
        self.name = None
        self.age = 0
        self.height = 0
        self.weight = 0
        self.goal = None
        self.meals = []
        self.workouts = []
        self.steps = 0

user = UserData()

# ------------------ Predefined Suggestions ------------------
def predefined_meals_and_workouts(goal: str):
    if goal == "loss":
        meals = [
            {"name": "Grilled Chicken Salad", "calories": 350, "protein": 30},
            {"name": "Vegetable Soup", "calories": 250, "protein": 10},
        ]
        workouts = [
            {"name": "Running", "duration": 30},
            {"name": "HIIT", "duration": 20},
        ]
    else:  # gain
        meals = [
            {"name": "Peanut Butter Sandwich", "calories": 600, "protein": 25},
            {"name": "Protein Shake", "calories": 450, "protein": 40},
        ]
        workouts = [
            {"name": "Weight Training", "duration": 45},
            {"name": "Strength Training", "duration": 40},
        ]
    return meals, workouts

# ------------------ Background Tasks ------------------
async def hydration_task():
    while True:
        await asyncio.sleep(20)
        if user.name:
            print("💧 Reminder: Drink water!")

async def step_counter_task():
    while True:
        await asyncio.sleep(10)
        if user.name:
            user.steps += 100

@app.on_event("startup")
async def start_tasks():
    asyncio.create_task(hydration_task())
    asyncio.create_task(step_counter_task())

# ------------------ Routes ------------------
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "user": user}
    )

@app.post("/create-user")
def create_user(
    name: str = Form(...),
    age: int = Form(...),
    height: int = Form(...),
    weight: int = Form(...),
    goal: str = Form(...)
):
    user.reset()
    user.name = name
    user.age = age
    user.height = height
    user.weight = weight
    user.goal = goal

    # 🔥 Load predefined meals & workouts
    meals, workouts = predefined_meals_and_workouts(goal)
    user.meals.extend(meals)
    user.workouts.extend(workouts)

    return RedirectResponse("/", status_code=303)

@app.post("/add-meal")
def add_meal(
    meal_name: str = Form(...),
    calories: int = Form(...),
    protein: int = Form(...)
):
    if user.name:
        user.meals.append({
            "name": meal_name,
            "calories": calories,
            "protein": protein
        })
    return RedirectResponse("/", status_code=303)

@app.post("/add-workout")
def add_workout(
    workout_name: str = Form(...),
    duration: int = Form(...)
):
    if user.name:
        user.workouts.append({
            "name": workout_name,
            "duration": duration
        })
    return RedirectResponse("/", status_code=303)
