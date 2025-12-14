from fastapi import FastAPI

app = FastAPI(
    title = "Cylytic Backend",
    version = "1.0.0",
    description="AI-powered period and wellness tracker backend"
)

@app.get("/") 
def root():
    return {"message": "Cyclytic backend running"}
