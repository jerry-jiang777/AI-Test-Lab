from abc import ABC, abstractmethod
from src.llm.models import LLMRequest, LLMResponse


class BaseLLM(ABC):
    """所有大模型客户端必须遵守的统一接口。"""

    def __init__(self, model: str, provider: str) -> None:
        if not model.strip():
            raise ValueError("model 不能为空")
        if not provider.strip():
            raise ValueError("provider 不能为空")
        self.model = model
        self.provider = provider


    @property
    def provider(self) -> str:
        return self.provider


    @abstractmethod
    def generate(self, request: LLMRequest) -> LLMResponse:
        """根据请求生成模型响应。"""
        raise NotImplementedError("generate 方法必须在子类中实现")