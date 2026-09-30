import re
from typing import Any

DIFFICULTIES = {"easy", "medium", "hard"}
TYPES = {"mcq", "short_answer", "true_false", "descriptive"}

class InputError(ValueError):
    pass

def validate_request(data: dict[str, Any]) -> None:
    if not isinstance(data, dict):
        raise InputError("request must be an object")
    for key in ("topic", "question_type", "count", "difficulty"):
        if key not in data:
            raise InputError(f"missing required field: {key}")
    if not isinstance(data["topic"], str) or not data["topic"].strip():
        raise InputError("topic must be a non-empty string")
    if data["question_type"] not in TYPES:
        raise InputError("unsupported question_type")
    if not isinstance(data["count"], int) or isinstance(data["count"], bool) or not 1 <= data["count"] <= 50:
        raise InputError("count must be an integer from 1 to 50")
    if data["difficulty"] not in DIFFICULTIES:
        raise InputError("difficulty must be easy, medium, or hard")
    if data["question_type"] == "mcq":
        n = data.get("options_per_question")
        if not isinstance(n, int) or not 2 <= n <= 6:
            raise InputError("options_per_question must be an integer from 2 to 6 for MCQs")

def _facts(data: dict[str, Any]) -> list[str]:
    text = data.get("source_text", "")
    if not isinstance(text, str):
        raise InputError("source_text must be a string when provided")
    parts = [re.sub(r"\s+", " ", p).strip(" .") for p in re.split(r"(?<=[.!?])\s+|\n+", text) if p.strip()]
    return parts

def generate(data: dict[str, Any]) -> dict[str, Any]:
    validate_request(data)
    facts = _facts(data)
    topic = data["topic"].strip()
    qtype = data["question_type"]
    difficulty = data["difficulty"]
    count = data["count"]
    basis = facts or [f"User-supplied topic: {topic}"]
    questions = []
    for i in range(count):
        fact = basis[i % len(basis)]
        if qtype == "mcq":
            answer = fact
            opts = [answer]
            for j in range(1, data["options_per_question"]):
                opts.append(f"Alternative {j} for {topic}")
            options = opts
            text = f"Which statement is supported by the provided material about {topic}?"
        elif qtype == "true_false":
            answer = True
            options = [True, False]
            text = f"True or False: The following statement is supported by the provided material about {topic}: {fact}."
        elif qtype == "short_answer":
            answer = fact
            options = None
            text = f"State the key point about {topic} described in the provided material."
        else:
            answer = fact
            options = None
            text = f"Explain the following point about {topic}, using the provided material: {fact}."
        item = {
            "id": f"Q{i+1:03d}",
            "question": text,
            "type": qtype,
            "difficulty": difficulty,
            "answer": answer,
            "explanation": "The answer is grounded in the supplied source basis shown with the question.",
            "source_basis": fact,
        }
        if options is not None:
            item["options"] = options
        questions.append(item)
    return {"topic": topic, "count": count, "questions": questions}
