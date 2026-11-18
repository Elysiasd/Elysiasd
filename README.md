<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/hero-dark.svg">
  <img src="./assets/hero-light.svg" alt="张宇杰 · Yujie Zhang — AI Agent tooling, model gateway, agent evaluation" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/typing-dark.svg">
  <img src="./assets/typing-light.svg" alt="正在做：把多个 AI 编程 Agent 装进同一个工作台" width="760">
</picture>

</div>

## 主线项目

<table>
<tr>
<td width="50%" valign="top">

### [BootAgent](https://github.com/MaimoryLab/BootAgent) &nbsp; ![stars](https://img.shields.io/github/stars/MaimoryLab/BootAgent?style=flat-square&label=%E2%98%85&color=C9501C)

本地 AI 编程 Agent 工作台。检测、安装、配置 10 种编程 Agent 与 5 个内置模型服务。

`Go` `Wails v3` `React`

**发起人 / 核心开发** — 443 次提交中的 239 次（53%）

</td>
<td width="50%" valign="top">

### [AI-Inbox](https://github.com/MaimoryLab/AI-Inbox) &nbsp; ![stars](https://img.shields.io/github/stars/MaimoryLab/AI-Inbox?style=flat-square&label=%E2%98%85&color=6A655E)

扫描 Codex、Claude Code、Cursor 的本地会话，抽取待办卡片并绑定原文证据。

`TypeScript` `React` `MCP`

</td>
</tr>
<tr>
<td valign="top">

### [MoM](https://github.com/MaimoryLab/MoM) &nbsp; ![stars](https://img.shields.io/github/stars/MaimoryLab/MoM?style=flat-square&label=%E2%98%85&color=6A655E)

Mixture-of-Models 网关：fan-out 廉价 advisor 后聚合结果。

`TypeScript`

</td>
<td valign="top">

### [codeoff](https://github.com/MaimoryLab/codeoff) &nbsp; ![stars](https://img.shields.io/github/stars/MaimoryLab/codeoff?style=flat-square&label=%E2%98%85&color=6A655E)

远程控制本机 Codex 会话。

`Dart` `Go`

</td>
</tr>
</table>

## 个人项目

| 项目 | 说明 | 栈 |
| :--- | :--- | :--- |
| [**intent-translator**](https://github.com/Elysiasd/intent-translator) | 自然语言数据需求 → 结构化元数据查询。语用访问的最小原型，含冻结数据集与回归评测 | Python |
| [**imagenet-translator**](https://github.com/Elysiasd/imagenet-translator) | 自然语言图像检索请求 → Milvus 查询 | Python |
| [**NiuLai**](https://github.com/Elysiasd/NiuLai) | DeepSeek Harness 的水墨风主题插件，零依赖 | JavaScript |
| [**ThinkingA**](https://github.com/Elysiasd/ThinkingA) | 想法 → 开发 Plan → 本地 AI CLI Prompt | TypeScript |
| [**AI-Infra-Learning**](https://github.com/Elysiasd/AI-Infra-Learning) | 存储方向 AI Infra 的学习路线与实验 | Python |

## 技术栈

<div align="center">

**语言**<br>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript">
<img src="https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white" alt="Go">
<img src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">

**大模型与应用**<br>
<img src="https://img.shields.io/badge/Anthropic-191919?style=for-the-badge&logo=anthropic&logoColor=white" alt="Anthropic">
<img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI">
<img src="https://img.shields.io/badge/MCP-1A1A1A?style=for-the-badge" alt="MCP">
<img src="https://img.shields.io/badge/SSE-FF7A45?style=for-the-badge" alt="SSE">

**工程**<br>
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
<img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="pytest">

</div>

## 近一年

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/contrib-dark.svg">
  <img src="./assets/contrib-light.svg" alt="近一年贡献热力图，两个账号合并统计" width="100%">
</picture>

</div>

<sub>合并 [Elysiasd](https://github.com/Elysiasd) 与 [yujiezhang-ops](https://github.com/yujiezhang-ops) 两个账号，每日自动重建。</sub>

## 正在学习

面向大模型应用开发的八周计划：协议与流式 → 网关 → RAG → Agent → 评测 → 原理。

| 周 | 主题 | 产出 |
| :--- | :--- | :--- |
| 1 | LLM 接口与 SSE 流式 | 可用的客户端与流式解析 |
| 2 | 模型网关 | 多协议透传与用量计量 |
| 3 | RAG | 切块、检索、召回评估 |
| 4 | Agent 与 MCP | 结构化抽取与工具调用 |
| 5–6 | 工具链与评测 | 读懂既有项目、做迷你评测框架 |
| 7–8 | 原理与表达 | Transformer 基础、模拟面试 |

## 联系

<div align="center">

<a href="mailto:zyj1456017580@163.com"><img src="https://img.shields.io/badge/Email-zyj1456017580%40163.com-C9501C?style=flat-square&logo=maildotru&logoColor=white" alt="Email"></a>
<a href="https://github.com/yujiezhang-ops"><img src="https://img.shields.io/badge/GitHub-yujiezhang--ops-141414?style=flat-square&logo=github&logoColor=white" alt="GitHub"></a>

</div>

<sub>华中科技大学 · 计算机科学与技术 · 2023 – 2027 · 在 PPIO 派欧云</sub>
