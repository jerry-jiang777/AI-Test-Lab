import pytest

from src.llm import LLMRequest, MockLLM


def test_mock_llm_returns_configured_response() -> None:
    llm = MockLLM(response_text="北京是中国的首都。")
    request = LLMRequest(prompt="北京是哪个国家的首都？")

    response = llm.generate(request)

    assert response.content == "北京是中国的首都。"
    assert response.model == "mock-model"
    assert response.provider == "mock"
    assert response.usage["total_tokens"] == 0


def test_mock_llm_supports_dynamic_response() -> None:
    llm = MockLLM(
        response_factory=lambda request: f"收到问题：{request.prompt}"
    )
    request = LLMRequest(prompt="什么是LLM评测？")

    response = llm.generate(request)

    assert response.content == "收到问题：什么是LLM评测？"


def test_request_rejects_empty_prompt() -> None:
    with pytest.raises(ValueError, match="prompt 不能为空"):
        LLMRequest(prompt="   ")


@pytest.mark.parametrize("temperature", [-0.1, 2.1])
def test_request_rejects_invalid_temperature(
    temperature: float,
) -> None:
    with pytest.raises(
        ValueError,
        match="temperature 必须在 0.0 到 2.0 之间",
    ):
        LLMRequest(
            prompt="测试问题",
            temperature=temperature,
        )