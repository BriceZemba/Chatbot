# Gemini-Powered Research Agent: Agentic RAG Framework

[![Technical Report](https://img.shields.io/badge/Documentation-Technical%20Report-blue?style=for-the-badge)](./Technical_Report.pdf)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)

## 📋 Overview
This project implements an autonomous research-augmented conversational AI. Unlike standard chatbots, this system leverages **Agentic RAG** (Retrieval-Augmented Generation) to perform iterative web research, self-reflection, and synthesized answering using Google's Gemini-Pro models.

## 📄 Research Documentation
For a comprehensive architectural breakdown and analysis of the iterative reasoning loops, please refer to the technical report:
> **[Download Research Report (PDF)](./Technical_Report.pdf)**

## 🚀 Key Features
- **Iterative Reasoning Loop**: Powered by LangGraph to identify knowledge gaps and refine search strategies autonomously.
- **Multimodal Analysis**: Integrated vision capabilities to analyze health-related images or complex document layouts.
- **Source Traceability**: Every response is grounded with explicit citations and web-referenced data.
- **Fullstack Deployment**: A robust backend using FastAPI/LangGraph coupled with a responsive frontend (React/Streamlit).

## 🛠️ Tech Stack
- **Core AI**: Google Gemini-Pro & Gemini-Pro-Vision.
- **Orchestration**: LangGraph for stateful, cyclic multi-agent workflows.
- **Backend**: FastAPI for high-performance asynchronous API management.
- **Frontend**: Streamlit for rapid prototyping and React for industrial-grade UI.

## 💻 Quick Start
```bash
# Install dependencies
pip install google-generativeai streamlit python-dotenv langgraph fastapi

# Run the experimental chatbot
streamlit run geminichatbot.py

Google generative ai has two free models like gemini-pro and gemini-pro-vision.

## Gemini-Pro 
It's a powerful free model that can have some many advantages like answering any type of question.

## How to install it ??
```bash
pip install google-generativeai
```
## Frontend/Backend
For the frontend an the backend streamlit is a very powerful library that that manage the frontend and the backend.

## How to install Streamlit ??
```bash
pip install streamlit
```

## Explanation

After installing the useful library for the project and run it in your laptop , then you will be able to ask any question directly to gemini-pro
