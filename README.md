## 1. 项目名称

AI-Test-Lab

## 2. 项目简介

一个面向AI应用测试与评测的企业级测试平台。

## 3. 核心能力

- 使用 DeepEval 评测 LLM 应用的回答质量
- 使用 OpenCompass 评测基础模型的通用能力
- 使用 Ragas 评测 RAG 应用
- 使用 LangSmith 追踪和分析 LLM 调用链
- 管理 Benchmark 与测试数据集
- 生成 Allure、JSON 和 HTML 评测报告
- 通过 GitHub Actions 执行自动化回归评测

## 4. 架构图

    CLI / API
                             │
                             ▼
                    Evaluation Engine
                             │
          ┌──────────────────┐
          │                          │
   	  ▼                           ▼                                     ▼
      DeepEval              OpenCompass                   Ragas
          │                  │                     │
          └──────────────────|
                                          ▼
                                     LLM Adapter

    ┌──────────────────┼
          ▼                  ▼                  ▼
        OpenAI           DeepSeek             Qwen

Benchmark / Dataset ──► Evaluation Task ──► Reports未来会迭代哪些能力？

## 5. 项目目录



## 6. 快速开始

建设中

## 7. Roadmap

# 8. 项目背景

本项目用于将零散的 AI 测试知识沉淀为可运行、可测试、
可持续集成的工程化项目，并逐步形成完整的 LLM 应用与
基础模型评测能力。
