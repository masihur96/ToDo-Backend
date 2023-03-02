from fastapi import FastAPI
from routers import task,user

app=FastAPI()

#Health Check
@app.get('/',tags=['Health Check'])
def Health():
    return {'data':'Your connection is healthy'}
app.include_router(task.router)
app.include_router(user.router)