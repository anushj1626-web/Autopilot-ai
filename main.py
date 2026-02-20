from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS (frontend can access backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Employee data
employees = [
    {"name": "Guna", "efficiency": 90},
    {"name": "Senthil", "efficiency": 20},
    {"name": "Chandra", "efficiency": 60},
    {"name": "Anbu", "efficiency": 85}
]

tasks = []

# Risk prediction logic
def predict_delay(efficiency):

    if efficiency < 60:
        return "HIGH"

    elif 60 <= efficiency <= 70:
        return "MEDIUM"

    else:
        return "NO"


# Home route
@app.get("/")
def home():
    return {"message": "AutoPilot AI Backend Running"}


# Generate tasks
@app.get("/generate")
def generate_tasks():

    global tasks
    tasks = []

    for i in range(len(employees)):

        employee = employees[i]

        delay = predict_delay(employee["efficiency"])

        task = {
            "task_id": i+1,
            "task_name": f"Task {i+1}",
            "assigned_to": employee["name"],
            "efficiency": employee["efficiency"],
            "delay_risk": delay,
            "status": "Assigned"
        }

        tasks.append(task)

    return tasks


# Get tasks
@app.get("/tasks")
def get_tasks():
    return tasks