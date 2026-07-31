from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.llm import LLMRequest, MockLLM


def main() -> None:
    llm = MockLLM(
        response_factory=lambda request: (
            f"Mock 模型已收到问题：{request.prompt}"
        )
    )

    request = LLMRequest(
        prompt="DeepEval 和 OpenCompass 有什么区别？",
        temperature=0.0,
    )

    response = llm.generate(request)

    print(f"Provider: {response.provider}")
    print(f"Model: {response.model}")
    print(f"Content: {response.content}")


if __name__ == "__main__":
    main()
