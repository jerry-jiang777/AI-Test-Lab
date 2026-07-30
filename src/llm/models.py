from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class LLMRequest:
    """统一的模型请求对象。"""

    prompt: str # 用户输入的提示词
    system_prompt: str | None = None # 系统提示词，用于引导模型的行为
    temperature: float = 0.0 # 温度参数，用于控制模型的随机性
    max_tokens: int | None = None # 最大生成的 token 数量
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """这个函数是一个钩子函数，用于在实例化完成后进行验证。"""
        if not self.prompt.strip():
            raise ValueError("prompt 不能为空")

        if not 0.0 <= self.temperature <= 2.0:
            raise ValueError("temperature 必须在 0.0 到 2.0 之间")

        if self.max_tokens is not None and self.max_tokens <= 0:
            raise ValueError("max_tokens 必须大于 0")


@dataclass(frozen=True)
class LLMResponse:
    """统一的模型响应对象。"""

    content: str
    model: str
    provider: str
    usage: dict[str, int] = field(default_factory=dict) # 模型调用的 token 数量
    raw_response: Any = None # 模型返回的原始响应