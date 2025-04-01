from fastapi import FastAPI
import uvicorn
import sys
import os 
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from src.textSummarizer.pipeline.prediction import PredictPipeline

text: str = "This is a sample text that needs to be summarized."

app = FastAPI()

@app.get("/", tags=['authendication'])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training completed successfully.")

    except Exception as e:
        return Response(f"An error occurred during training: {str(e)}", status_code=500)
    

@app.post("/predict")
async def predict_route(text: str):
    try:
        obj = PredictPipeline()
        text_summary = obj.predict(text)
        return {"summary": text_summary}
    
    except Exception as e:
        return Response(f"An error occurred during prediction: {str(e)}", status_code=500)
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)