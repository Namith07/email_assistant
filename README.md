# Email Generation Assistant

An LLM-powered email generation assistant with advanced prompt engineering and a custom evaluation framework comparing two models.

## Project Structure
email_assistant/
├── app/
│ ├── agent.py
│ ├── prompt.py 
│ ├── evaluate.py 
│ ├── scenarios.py 
│ └── main.py 
├── outputs/
│ └── evaluation_results.json 
├── model_compare.py 
├── analysis.md 
├── requirements.txt
└── .env 


## Models Compared

| Label   | Model ID                  | Prompt Style                     |
|---------|---------------------------|----------------------------------|
| Model A | llama-3.3-70b-versatile   | Advanced (Role + CoT + Few-Shot) |
| Model B | openai/gpt-oss-120b            | Baseline (minimal)               |

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API key
Create a `.env` file in the project root:

Get a free key at https://console.groq.com

### 3. Run the evaluation (Model A vs Model B)
```bash
python model_compare.py
```
Results are saved to `outputs/evaluation_results.json`.

### 4. Run the API server
```bash
uvicorn app.main:app --reload
```

## API Usage

**POST** `/generate`
```json
{
  "intent": "Follow up after a client meeting",
  "facts": ["Met on Tuesday", "Client wants automation", "Send pricing deck by Friday"],
  "tone": "formal",
  "model": "model_a"
}
```
Use `"model": "model_a"` or `"model": "model_b"`.

**GET** `/health` — Returns `{"status": "ok"}`

## Custom Evaluation Metrics

1. **Fact Recall** — Token overlap: were all input facts included in the email?
2. **Tone Alignment** — Lexical cue matching: does the language match the requested tone?
3. **Structure Score** — Format check: subject line, greeting, paragraph separation, sign-off.

See `analysis.md` for full metric definitions and comparative results.