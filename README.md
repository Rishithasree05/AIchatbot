# 🤖 VaultOfCodes AI Support Chatbot

An AI-powered customer/student support chatbot built for **VaultOfCodes**.  
The chatbot provides first-level support for questions related to internships, courses, training programs, enrollment, certificates, offer letters, website navigation, and general support.

---

## 📌 Project Overview

The VaultOfCodes AI Support Chatbot is designed to provide students and website visitors with quick and reliable answers to frequently asked questions.

Instead of requiring students to contact support for every basic query, the chatbot uses an AI-powered conversational interface to understand user questions, classify their intent, retrieve relevant information from a structured knowledge base, and generate a helpful response.

For issues that require account-specific information or human intervention, the chatbot redirects the user to the VaultOfCodes support team.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Provide instant first-level support to students.
- Answer frequently asked questions about courses and internships.
- Help users navigate important website pages.
- Provide information about enrollment and training programs.
- Handle certificate and offer-letter related queries.
- Identify questions that require human support.
- Reduce repetitive support requests.
- Provide a simple and user-friendly AI chat interface.

---

## ✨ Key Features

### 💬 AI Chat Interface

Users can interact with the chatbot through a modern conversational interface.

### 🧠 Intent Classification

User questions are classified into predefined intents such as:

- Course Inquiry
- Training Inquiry
- Internship Inquiry
- Workshop Inquiry
- Certificate Query
- Certificate Verification
- Offer Letter Query
- Enrollment Query
- Payment Query
- Website Navigation
- Technical Support
- Human Support
- General Query
- Unknown Query

### 📚 Knowledge Base

The chatbot uses a structured JSON knowledge base containing verified information about:

- VaultOfCodes
- Available offerings
- Internship information
- Support contact details
- Website pages
- System limitations

### 🤖 OpenRouter AI Integration

The backend uses the **OpenRouter API** to communicate with the selected AI model.

The API key is stored securely in an environment variable and is **not included in the GitHub repository**.

### 🛡️ Human Escalation

Certain issues are automatically redirected to human support, including:

- Payment problems
- Technical problems
- Account-specific issues
- Requests requiring manual verification
- Requests to speak with human support

### 🌐 Website Navigation

The chatbot can guide users to relevant website sections such as:

- `/`
- `/about-us`
- `/courses`
- `/internships`

### ⚡ Real-Time Responses

The React frontend communicates with the Flask backend through a REST API.

---

# 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │      User           │
                    │  Chatbot Interface  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   React Frontend    │
                    │      + Vite         │
                    └──────────┬──────────┘
                               │
                               │ HTTP POST
                               ▼
                    ┌─────────────────────┐
                    │    Flask Backend    │
                    │     REST API        │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
          ┌──────────────────┐   ┌──────────────────┐
          │ Intent           │   │ Knowledge Base   │
          │ Classification   │   │ JSON             │
          └────────┬─────────┘   └────────┬─────────┘
                   │                      │
                   └──────────┬───────────┘
                              ▼
                    ┌─────────────────────┐
                    │    OpenRouter AI    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ AI Generated        │
                    │ Response            │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   React Chat UI     │
                    └─────────────────────┘
