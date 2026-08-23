import json
import os
import requests

from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv

from intents import INTENTS, ESCALATION_INTENTS
from prompts import (
    SYSTEM_PROMPT,
    build_intent_prompt,
    build_response_prompt,
    UNKNOWN_RESPONSE,
    ESCALATION_RESPONSE
)


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

load_dotenv()

app = Flask(__name__)
CORS(app)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

OPENROUTER_MODEL = os.getenv(
    "OPENROUTER_MODEL",
    "z-ai/glm-5.2:free"
)


# ---------------------------------------------------------
# Load Knowledge Base
# ---------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

KNOWLEDGE_BASE_PATH = os.path.join(
    BASE_DIR,
    "knowledge_base.json"
)

with open(
    KNOWLEDGE_BASE_PATH,
    "r",
    encoding="utf-8"
) as file:
    KNOWLEDGE_BASE = json.load(file)


# ---------------------------------------------------------
# OpenRouter AI Function
# ---------------------------------------------------------

def call_ai(prompt):
    """
    Send a prompt to OpenRouter and return the AI response.
    """

    if not OPENROUTER_API_KEY:
        raise Exception(
            "OPENROUTER_API_KEY is not configured."
        )

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",

        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },

        json={
            "model": OPENROUTER_MODEL,

            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        },

        timeout=60
    )

    response.raise_for_status()

    data = response.json()

    if "choices" not in data or not data["choices"]:
        raise Exception(
            "No response was returned by OpenRouter."
        )

    return data["choices"][0]["message"]["content"].strip()


# ---------------------------------------------------------
# Intent Classification
# ---------------------------------------------------------

def classify_intent(user_message):
    """
    Classify the user's message into one of the
    predefined intents.
    """

    if not OPENROUTER_API_KEY:
        print("OpenRouter API key is missing.")
        return "unknown"

    prompt = build_intent_prompt(user_message)

    try:

        detected_intent = call_ai(prompt)

        print(
            "AI raw intent response:",
            repr(detected_intent)
        )

        # Remove markdown formatting
        detected_intent = (
            detected_intent
            .replace("`", "")
            .strip()
        )

        # Sometimes the model may return multiple lines.
        # Take the first non-empty line.
        detected_intent = next(
            (
                line.strip()
                for line in detected_intent.splitlines()
                if line.strip()
            ),
            ""
        )

        print(
            "Cleaned intent:",
            repr(detected_intent)
        )

        # Make sure the returned intent is valid
        if detected_intent in INTENTS:
            return detected_intent

        print(
            "Invalid intent:",
            repr(detected_intent)
        )

        return "unknown"

    except Exception as error:

        print(
            "Intent classification error:",
            error
        )

        return "unknown"


# ---------------------------------------------------------
# Generate Final AI Response
# ---------------------------------------------------------

def generate_ai_response(
    user_message,
    intent,
    conversation_history=""
):
    """
    Generate the final chatbot response using
    the knowledge base and OpenRouter.
    """

    if not OPENROUTER_API_KEY:
        return (
            "The AI service is not configured yet. "
            "Please contact our support team for assistance."
        )

    knowledge_base_text = json.dumps(
        KNOWLEDGE_BASE,
        indent=2,
        ensure_ascii=False
    )

    prompt = (
        SYSTEM_PROMPT
        + "\n\n"
        + build_response_prompt(
            knowledge_base=knowledge_base_text,
            intent=intent,
            user_message=user_message,
            conversation_history=conversation_history
        )
    )

    try:

        return call_ai(prompt)

    except Exception as error:

        print(
            "AI response error:",
            error
        )

        return (
            "I'm sorry, I'm unable to process your request "
            "right now. Please contact our support team "
            "for assistance."
        )


# ---------------------------------------------------------
# Home Route
# ---------------------------------------------------------

@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "success": True,
        "message":
            "VaultOfCourse AI Support Chatbot API is running."
    })


# ---------------------------------------------------------
# Health Check
# ---------------------------------------------------------

@app.route("/api/health", methods=["GET"])
def health():

    return jsonify({
        "success": True,
        "backend": "running",
        "ai_configured": bool(OPENROUTER_API_KEY),
        "model": OPENROUTER_MODEL
    })


# ---------------------------------------------------------
# Chat API
# ---------------------------------------------------------

@app.route("/api/chat", methods=["POST"])
def chat():

    data = request.get_json(
        silent=True
    ) or {}

    user_message = data.get(
        "message",
        ""
    ).strip()

    conversation_history = data.get(
        "conversation_history",
        ""
    )

    # Check empty message
    if not user_message:

        return jsonify({
            "success": False,
            "error": "Message is required."
        }), 400


    # -----------------------------------------------------
    # 1. Classify Intent
    # -----------------------------------------------------

    intent = classify_intent(
        user_message
    )


    # -----------------------------------------------------
    # 2. Unknown Questions
    # -----------------------------------------------------

    if intent == "unknown":

        return jsonify({
            "success": True,
            "intent": "unknown",
            "response": UNKNOWN_RESPONSE,
            "escalate": True
        })


    # -----------------------------------------------------
    # 3. Human Escalation
    # -----------------------------------------------------

    if intent in ESCALATION_INTENTS:

        return jsonify({
            "success": True,
            "intent": intent,
            "response": ESCALATION_RESPONSE,
            "escalate": True
        })


    # -----------------------------------------------------
    # 4. Generate Normal AI Response
    # -----------------------------------------------------

    response = generate_ai_response(
        user_message=user_message,
        intent=intent,
        conversation_history=conversation_history
    )


    # -----------------------------------------------------
    # 5. Return Response
    # -----------------------------------------------------

    return jsonify({
        "success": True,
        "intent": intent,
        "response": response,
        "escalate": False
    })


# ---------------------------------------------------------
# Run Flask Application
# ---------------------------------------------------------

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )