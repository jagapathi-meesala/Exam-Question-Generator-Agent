from core.generator import generate

def execute(request: dict) -> dict:
    try:
        return {"ok": True, "result": generate(request)}
    except ValueError as exc:
        return {"ok": False, "error": {"type": "validation_error", "message": str(exc)}}
