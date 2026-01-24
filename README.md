# Gemini-Powered Research Agent: Agentic RAG Framework

[![Technical Report](https://img.shields.io/badge/Documentation-Technical%20Report-blue?style=for-the-badge)](./Technical_Report.pdf)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)

## 📋 Overview

The **Gemini-Powered Research Agent** is an autonomous, research-augmented conversational AI system designed to perform **iterative web research, self-reflection, and knowledge synthesis**. Unlike standard chatbots, this system leverages **Agentic RAG (Retrieval-Augmented Generation)** combined with Google’s **Gemini-Pro models** to provide accurate, evidence-based, and multimodal responses.

The agent is capable of understanding complex queries, retrieving relevant external knowledge, analyzing both text and images, and generating **citations-backed answers**, making it ideal for research, technical analysis, and educational purposes.

---

## 📄 Research Documentation

A comprehensive technical breakdown, architectural details, and experimental results are available in our report:

> **[Download Technical Report (PDF)](./Technical_Report.pdf)**

---

## 🚀 Key Features

* **Iterative Reasoning Loop**: Uses **LangGraph** to detect gaps in knowledge, plan search strategies, retrieve information, and refine answers dynamically.
* **Multimodal Analysis**: Supports **text and image inputs**, allowing analysis of charts, diagrams, PDFs, and medical images using Gemini-Pro-Vision.
* **Source Traceability**: Every answer includes explicit references and citations for verified, reproducible results.
* **Fullstack Deployment**: Combines **FastAPI** backend for high-performance APIs with **Streamlit/React** frontends for interactive and scalable user experiences.
* **Autonomous Multi-Agent Workflows**: Uses modular sub-agents to independently handle search, analysis, and reasoning tasks within the same conversation.

---

## 🛠️ Tech Stack

| Component     | Technology                            | Purpose                                            |
| ------------- | ------------------------------------- | -------------------------------------------------- |
| Core AI       | Google Gemini-Pro & Gemini-Pro-Vision | Large-scale reasoning and multimodal understanding |
| Orchestration | LangGraph                             | Multi-agent iterative reasoning loops              |
| Backend       | FastAPI                               | Asynchronous, high-performance API handling        |
| Frontend      | Streamlit & React                     | Rapid prototyping and production-ready UI          |

---

## 💻 Quick Start

### 1. Install Dependencies

```bash
pip install google-generativeai streamlit python-dotenv langgraph fastapi
```

### 2. Run the Chatbot

```bash
streamlit run geminichatbot.py
```

### 3. Gemini-Pro Models

* **Gemini-Pro**: Text-based model capable of reasoning, answering questions, and synthesizing knowledge.
* **Gemini-Pro-Vision**: Extends Gemini-Pro with image and multimodal processing for charts, diagrams, and visual data analysis.

Install the models via Python:

```bash
pip install google-generativeai
```

---

## 🔹 Frontend & Backend Details

* **Streamlit**: Provides an interactive interface for experimenting with the agent and visualizing results in real time.
* **React**: Optional for production-grade web applications, allowing a modern, scalable UI.
* **FastAPI**: Handles backend logic, routing, and asynchronous API calls to the agent, ensuring **scalability and low-latency responses**.

---

## 📖 Detailed Explanation

The Gemini-Powered Research Agent is designed to **autonomously research and reason** by iterating through the following workflow:

1. **Query Analysis** – Understands user input and identifies knowledge gaps.
2. **External Knowledge Retrieval** – Uses LangGraph to fetch relevant web content, papers, or databases.
3. **Self-Reflection & Reasoning** – Evaluates retrieved data to synthesize accurate, high-confidence responses.
4. **Answer Generation** – Produces a detailed, evidence-backed response, including citations and references.
5. **Multimodal Processing** – If needed, incorporates images, charts, or PDFs into reasoning for richer answers.

This system bridges the gap between **static LLM responses** and **dynamic research capabilities**, enabling both practical applications and experimental research.

---

## 📎 References

All sources are explicitly cited in responses. For academic or professional use, references can be extracted from generated outputs.

