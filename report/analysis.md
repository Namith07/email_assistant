# Comparative Analysis — Email Generation Assistant

## Prompt Template Used

**Model A** (`llama-3.3-70b-versatile`) uses an advanced prompt engineering technique combining:
- **Role-Playing**: The model is assigned the persona of a senior executive communication specialist.
- **Chain-of-Thought (CoT)**: Five explicit reasoning steps guide the model before drafting — identifying intent, confirming facts, selecting tone register, writing the subject line, then enforcing length constraints.
- **Few-Shot Examples**: Four tone-specific examples (formal, casual, urgent, empathetic) demonstrate the expected output format and style.
- **Hard Constraints**: Explicit rules prevent bullet points, hallucinated details, and omitted facts.
- **Temperature**: 0.3 — deterministic and controlled output.

**Model B** (`openai/gpt-oss-120b`) uses a minimal baseline prompt:
- No role assignment, no reasoning steps, no examples.
- Simple instruction with intent, tone, and facts only.
- **Temperature**: 0.7 — more generative, less constrained.

---

## Custom Metric Definitions

### 1. Fact Recall
Measures how many required facts from the input scenario are reflected in the generated email using token overlap. A fact is considered recalled if at least 50% of its meaningful tokens (length > 2) appear in the normalised email text. This directly measures the assistant's core job — including all provided information.
**Score range**: 0.0 to 1.0

### 2. Tone Alignment
Measures whether the email language matches the requested tone by checking for tone-specific lexical cues. Each tone (formal, casual, urgent, empathetic) has a defined keyword set. Score is the ratio of matched cues to the total expected cues, capped at 1.0.
**Score range**: 0.0 to 1.0

### 3. Structure Score
Measures whether the email follows professional email format by verifying four structural elements: subject line, greeting (Dear/Hi/Hello), paragraph separation (blank line), and a sign-off keyword. Each element contributes 0.25.
**Score range**: 0.0 to 1.0

---

## Comparative Analysis

Based on evaluation across 10 scenarios, **Model B outperformed Model A on tone alignment, structure, and overall score**:

| Metric         | Model A (llama-3.3-70b) | Model B (openai/gpt-oss-120b) |
|----------------|--------------------------|-------------------------------|
| Fact Recall    | 0.97                     | 0.95                          |
| Tone Alignment | 0.23                     | 0.38                          |
| Structure      | 0.75                     | 0.97                          |
| **Overall**    | 0.65                     | **0.77**                      |

*(Exact per-scenario values are in `outputs/evaluation_results.json`)*

---

## Biggest Failure Mode of Model A

Model A's most consistent failure was **low structure score (0.75)** — despite explicit format constraints in the prompt, it occasionally produced responses without proper blank-line paragraph separation, causing the structural check to partially fail. Its tone alignment score (0.23) was also notably lower than Model B, suggesting that the smaller model with a constrained temperature (0.3) matched fewer tone-specific lexical cues even when the overall tone felt appropriate — possibly because it paraphrased tone rather than using the expected vocabulary.

---

## Production Recommendation

**Recommend Model B** (`openai/gpt-oss-120b`) for production based on evaluation data:

1. **Better overall score (0.77 vs 0.65)** — consistently higher quality across all 10 scenarios.
2. **Near-perfect structure (0.97)** — professional email format is a hard requirement; Model B reliably produces subject lines, greetings, and sign-offs.
3. **Higher tone alignment (0.38 vs 0.23)** — Model B naturally uses more tone-appropriate vocabulary without needing explicit keyword injection in the prompt.
4. **Comparable fact recall (0.95 vs 0.97)** — both models include nearly all required facts; the difference is negligible for production use.

Model A remains a strong candidate for cost-sensitive deployments where llama-3.3-70b-versatile is preferred, and its prompt engineering approach can be further refined to close the gap.