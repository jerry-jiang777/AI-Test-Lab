from collections.abc import Callable

from src.llm.base import BaseLLM
from src.llm.models import LLMRequest, LLMResponse


class MockLLM(BaseLLM):
    """用于测试的模拟模型，不会访问真实外部服务。"""

    def __init__(
        self,
        response_text: str = "这是一个模拟模型响应。",
        response_factory: Callable[[LLMRequest], str] | None = None,
    ) -> None:
        super().__init__(model="mock-model", provider="mock")
        self._response_text = response_text
        self._response_factory = response_factory

    def generate(self, request: LLMRequest) -> LLMResponse:
        if self._response_factory is not None:
            content = self._response_factory(request)
        else:
            content = self._response_text

        return LLMResponse(
            content=content,
            model=self.model,
            provider=self.provider,
            usage={
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_tokens": 0,
            },
        )