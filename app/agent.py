import os
import time
import traceback
from dotenv import load_dotenv
from groq import Groq
from typing import Literal
from app.prompt import EmailGenPrompts

load_dotenv()

Model = Literal["model_a", "model_b"]

MODEL_MAP = {
    "model_a": "llama-3.3-70b-versatile",
    "model_b": "openai/gpt-oss-120b",
}

pmpt = EmailGenPrompts()


class EmailGenerator:
    def __init__(self, api_key: str = None):
        api_key = api_key or os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not set in environment.")
        self.client = Groq(api_key=api_key)

    def generate_email(
        self,
        intent: str,
        facts: list[str],
        tone: str,
        model: Model = "model_a",
    ) -> str:
        try:
            print(f"--- generate_email | model={model} ---")
            start = time.time()

            facts_block = "\n".join(f"- {fact}" for fact in facts)
            groq_model = MODEL_MAP[model]

            if model == "model_a":
                user_prompt = pmpt.model_a_prompt.format(
                    intent=intent, tone=tone, facts_block=facts_block
                )
                temperature = 0.3
            else:
                user_prompt = pmpt.model_b_prompt.format(
                    intent=intent, tone=tone, facts_block=facts_block
                )
                temperature = 0.7

            response = self.client.chat.completions.create(
                model=groq_model,
                temperature=temperature,
                top_p=0.9,
                messages=[
                    {"role": "system", "content": pmpt.system_role},
                    {"role": "user", "content": user_prompt},
                ],
            )
            result = response.choices[0].message.content.strip()
            print(f"time taken {time.time() - start:.2f}s")
            return result

        except Exception as e:
            print(f"Error in generate_email: {str(e)}")
            traceback.print_exc()
            return f"Failed to generate email: {str(e)}"