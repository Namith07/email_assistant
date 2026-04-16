import json
import re
import traceback
from statistics import mean

TONE_KEYWORDS: dict[str, list[str]] = {
    "formal": [
        "dear", "regards", "sincerely", "appreciate", "please",
        "kindly", "writing", "would like", "ensure", "request"
    ],
    "casual": [
        "hi", "thanks", "hope", "let me know", "feel free",
        "happy to", "wanted to", "doing well", "just", "catch"
    ],
    "urgent": [
        "urgent", "immediately", "as soon as possible", "deadline", "priority",
        "mandatory", "action required", "critical", "today", "confirm"
    ],
    "empathetic": [
        "apologize", "apologise", "sorry", "understand", "patience",
        "inconvenience", "sincerely", "grateful", "frustrating", "support"
    ],
}

METRIC_DEFINITIONS = {
    "fact_recall": (
        "Measures how many required facts are reflected in the generated email using token overlap. "
        "A fact is considered recalled if at least 50% of its meaningful tokens appear in the email."
    ),
    "tone_alignment": (
        "Measures how well the email language matches the requested tone by checking for "
        "tone-specific lexical cues."
    ),
    "structure": (
        "Measures whether the email follows professional format: subject line, greeting, "
        "body separation, and sign-off."
    ),
    "overall": "Average of fact_recall, tone_alignment, and structure.",
}


def normalize_text(text: str) -> str:
    return re.sub(r"[^\w\s]", " ", text.lower()).strip()


def fact_recall_score(email: str, facts: list[str]) -> float:
    try:
        email_norm = normalize_text(email)
        hits = 0
        for fact in facts:
            tokens = [t for t in re.findall(r"\w+", fact.lower()) if len(t) > 2]
            if not tokens:
                continue
            overlap = sum(1 for t in tokens if t in email_norm)
            if overlap / len(tokens) >= 0.5:
                hits += 1
        return round(hits / len(facts), 2)
    except Exception as e:
        print(f"Error in fact_recall_score: {str(e)}")
        traceback.print_exc()
        return 0.0


def tone_alignment_score(email: str, tone: str) -> float:
    try:
        email_norm = normalize_text(email)
        keywords = TONE_KEYWORDS.get(tone.lower(), [])
        if not keywords:
            return 0.0
        matches = sum(1 for kw in keywords if normalize_text(kw) in email_norm)
        score = min(1.0, matches / len(keywords))
        return round(score, 2)
    except Exception as e:
        print(f"Error in tone_alignment_score: {str(e)}")
        traceback.print_exc()
        return 0.0


def structure_score(email: str) -> float:
    try:
        # Normalise line endings (handles \r\n on Windows)
        email_clean = email.replace("\r\n", "\n").replace("\r", "\n")
        text_lower = email_clean.lower()
        text_norm = normalize_text(email_clean)

        checks = [
            # Subject line present
            bool(re.search(r"^subject[\s:]", text_lower, re.MULTILINE)),
            # Greeting at start of a line
            bool(re.search(r"(^|\n)(dear|hi|hello|hey)\b", text_lower)),
            # At least one blank line separating paragraphs
            bool(re.search(r"\n\s*\n", email_clean)),
            # Sign-off present
            any(kw in text_norm for kw in [
                "best regards", "kind regards", "regards",
                "sincerely", "thanks", "best", "warm regards", "yours"
            ]),
        ]
        return round(sum(checks) / len(checks), 2)
    except Exception as e:
        print(f"Error in structure_score: {str(e)}")
        traceback.print_exc()
        return 0.0


def evaluate_email(email: str, scenario: dict) -> dict:
    scores = {
        "fact_recall": fact_recall_score(email, scenario["facts"]),
        "tone_alignment": tone_alignment_score(email, scenario["tone"]),
        "structure": structure_score(email),
    }
    scores["overall"] = round(mean(scores.values()), 2)
    return scores


def summarize_results(results: list[dict]) -> dict:
    metrics = ["fact_recall", "tone_alignment", "structure", "overall"]
    return {m: round(mean(item["scores"][m] for item in results), 2) for m in metrics}


def save_results(path: str, payload: dict) -> None:
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)
        print(f"Results saved to {path}")
    except Exception as e:
        print(f"Error saving results: {str(e)}")
        traceback.print_exc()