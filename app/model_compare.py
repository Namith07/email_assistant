import traceback
from app.agent import EmailGenerator, MODEL_MAP
from app.evaluate import METRIC_DEFINITIONS, evaluate_email, save_results, summarize_results
from app.scenarios import SCENARIOS


def run_comparison() -> dict:
    try:
        print("--- run_comparison ---")
        generator = EmailGenerator()

        all_results = {
            "models": {m: {"model_id": MODEL_MAP[m]} for m in MODEL_MAP},
            "metric_definitions": METRIC_DEFINITIONS,
            "comparisons": {},
        }

        for model in ("model_a", "model_b"):
            print(f"\n{'='*40}\nModel: {model.upper()} ({MODEL_MAP[model]})\n{'='*40}")
            model_results = []

            for scenario in SCENARIOS:
                print(f"  Scenario {scenario['id']}: {scenario['intent'][:40]}")
                generated_email = generator.generate_email(
                    intent=scenario["intent"],
                    facts=scenario["facts"],
                    tone=scenario["tone"],
                    model=model,
                )
                scores = evaluate_email(generated_email, scenario)
                print(f"  Scores: {scores}")

                model_results.append({
                    "scenario_id": scenario["id"],
                    "intent": scenario["intent"],
                    "tone": scenario["tone"],
                    "facts": scenario["facts"],
                    "generated_email": generated_email,
                    "reference_email": scenario["reference_email"],
                    "scores": scores,
                })

            all_results["comparisons"][model] = {
                "results": model_results,
                "average_scores": summarize_results(model_results),
            }
            print(f"  Averages: {all_results['comparisons'][model]['average_scores']}")

        save_results("outputs/evaluation_results.json", all_results)
        return all_results

    except Exception as e:
        print(f"Error in run_comparison: {str(e)}")
        traceback.print_exc()
        return {}


if __name__ == "__main__":
    results = run_comparison()
    print("\n--- FINAL COMPARISON ---")
    for model in ("model_a", "model_b"):
        avg = results["comparisons"][model]["average_scores"]
        print(f"{model.upper()} ({MODEL_MAP[model]}): {avg}")