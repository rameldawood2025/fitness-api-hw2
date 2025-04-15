from fastapi import FastAPI

app = FastAPI()

users = []
workouts = []
meals = []

# USERS 

@app.get("/users")
async def get_users():
    return {"users": users}

@app.post("/users")
async def add_user(name: str = ""):
    users.append(name)
    return {"users": users}

@app.delete("/users")
async def delete_user(index: int = 0):
    users.pop(index)
    return {"users": users}


# WORKOUTS 

@app.get("/workouts")
async def get_workouts():
    return {"workouts": workouts}

@app.post("/workouts")
async def add_workout(name: str = ""):
    workouts.append(name)
    return {"workouts": workouts}

@app.delete("/workouts")
async def delete_workout(index: int = 0):
    workouts.pop(index)
    return {"workouts": workouts}


# MEALS 

@app.get("/meals")
async def get_meals():
    return {"meals": meals}

@app.post("/meals")
async def add_meal(name: str = ""):
    meals.append(name)
    return {"meals": meals}

@app.delete("/meals")
async def delete_meal(index: int = 0):
    meals.pop(index)
    return {"meals": meals}
