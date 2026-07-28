## AI-Test-Lab是一个面向LLM应用测试与基础模型评测的企业级自动化测试平台。

### 项目目标：

致力于构建一个"系统架构合理"的，高内聚低耦合的，面向LLM应用测试与基础模型评测的企业级自动化测试平台。

### 总体架构：

接口层

↓

任务编排层

↓

评测引擎层

↓

模型适配层

↓

数据层

↓

可观测性层

↓

报告层

### 各个层级的职责

#### 1. 接口层：Interface Layer

负责接手用户请求，未来支持 CLI、REST API 和 Web 页面。

#### 2. 任务编排层 Task Layer

负责创建评测任务、读取配置、选择数据集、控制执行流程。

#### 3. 评测引擎层 Evaluation Layer

提供统一评测入口，根据任务类型调用 DeepEval、OpenCompass、或 Ragas

#### 4. 模型适配层 LLM Adapter Layer

屏蔽 OpenAI、DeepSeek、Qwen、Ollama等不同接口差异，对上一层提供统一的generate( ) 或 invoke( )方法。

#### 5. 数据层 Data Layer

负责管理Benchmark、Dataset、Prompt 和期望结果。

#### 6. 可观测性层 Observability Layer

使用日志和 LangSmith 记录调用链、耗时、输入、输出和异常。

#### 7. 报告层 Report Layer

统一输出JSON、HTML、和Allure 报告。

### 未来拓展方向

- 支持更多 LLM Provider
- 支持 Prompt A/B 测试
- 支持 RAG 检索与生成质量评测
- 支持自定义评测指标
- 支持批量 Benchmark 回归
- 支持 GitHub Actions 自动执行
- 支持 Allure 和 HTML 可视化报告
- 支持 FastAPI 和 Web 管理页面
- 支持 Docker 容器化部署
