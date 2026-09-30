from typing import Callable

class ToolRegistry:
    def __init__(self):
        self._tools: dict[str, Callable] = {}

    def register(self, name: str, executor: Callable) -> None:
        if not name or name in self._tools:
            raise ValueError("tool name must be non-empty and unique")
        self._tools[name] = executor

    def discover(self) -> list[str]:
        return sorted(self._tools)

    def execute(self, name: str, request: dict) -> dict:
        if name not in self._tools:
            return {"ok": False, "error": {"type": "unknown_tool", "message": name}}
        try:
            return self._tools[name](request)
        except Exception as exc:
            return {"ok": False, "error": {"type": "execution_error", "message": str(exc)}}
