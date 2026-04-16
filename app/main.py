import traceback
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.agent import EmailGenerator, MODEL_MAP, Model

app = FastAPI(title="Email Generation Assistant", version="1.0.0")
generator: EmailGenerator = None


class EmailRequest(BaseModel):
    intent: str
    facts: list[str]
    tone: str
    model: Model = "model_a"


@app.on_event("startup")
def startup_event():
    global generator
    try:
        generator = EmailGenerator()
        print("EmailGenerator initialized.")
    except Exception as e:
        print(f"Startup error: {str(e)}")
        traceback.print_exc()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/generate")
def generate_email(request: EmailRequest):
    try:
        if not generator:
            raise HTTPException(status_code=500, detail="Generator not initialized.")
        email = generator.generate_email(
            intent=request.intent,
            facts=request.facts,
            tone=request.tone,
            model=request.model,
        )
        return {
            "model": request.model,
            "model_id": MODEL_MAP[request.model],
            "intent": request.intent,
            "tone": request.tone,
            "email": email,
        }
    except Exception as e:
        print(f"Error in /generate: {str(e)}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))