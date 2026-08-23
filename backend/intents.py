# Intent definitions for the VaultOfCodes AI Support Chatbot

INTENTS = {
    "course_inquiry": {
        "description": "Questions about courses, course content, duration, fees, enrollment, or access.",
        "examples": [
            "What courses are available?",
            "How can I enroll in a course?",
            "What is included in the course?"
        ]
    },

    "training_inquiry": {
        "description": "Questions about training programs and training-related information.",
        "examples": [
            "What training programs are available?",
            "Tell me about your training."
        ]
    },

    "internship_inquiry": {
        "description": "Questions about internships, eligibility, application, duration, assignments, or certificates.",
        "examples": [
            "What internships are available?",
            "How can I apply for an internship?",
            "How long is the internship?"
        ]
    },

    "workshop_inquiry": {
        "description": "Questions about workshops.",
        "examples": [
            "What workshops do you provide?",
            "Are there any upcoming workshops?"
        ]
    },

    "certificate_query": {
        "description": "Questions about downloading, receiving, or correcting certificates.",
        "examples": [
            "Where can I download my certificate?",
            "My certificate is not showing."
        ]
    },

    "certificate_verification": {
        "description": "Questions specifically about certificate verification.",
        "examples": [
            "How do I verify my certificate?",
            "Where can I verify a certificate?"
        ]
    },

    "offer_letter_query": {
        "description": "Questions about offer letters, downloading them, missing offer letters, or incorrect details.",
        "examples": [
            "Where can I find my offer letter?",
            "My offer letter is missing."
        ]
    },

    "enrollment_query": {
        "description": "Questions about enrollment or joining a course, training, or internship.",
        "examples": [
            "How do I enroll?",
            "How can I join the program?"
        ]
    },

    "payment_query": {
        "description": "Payment, refund, transaction, or payment-related problems.",
        "examples": [
            "I made a payment but did not get access.",
            "I want a refund.",
            "My payment failed."
        ]
    },

    "website_navigation": {
        "description": "Questions asking where to find a page, course, internship, certificate, or other website information.",
        "examples": [
            "Where can I find internships?",
            "Where can I find free courses?"
        ]
    },

    "technical_support": {
        "description": "Technical problems that the chatbot cannot resolve.",
        "examples": [
            "The website is not working.",
            "I cannot access my course."
        ]
    },

    "human_support": {
        "description": "The student explicitly wants human support or has an issue requiring manual assistance.",
        "examples": [
            "I want to talk to a human.",
            "Connect me with support."
        ]
    },

    "general_query": {
        "description": "General questions related to VaultOfCodes.",
        "examples": [
            "What is VaultOfCodes?",
            "Tell me about VaultOfCodes."
        ]
    },

    "unknown": {
        "description": "Questions that cannot be confidently classified.",
        "examples": [
            "Tell me something random.",
            "What is the weather?"
        ]
    }
}


# Intents that should normally be escalated to human support
ESCALATION_INTENTS = {
    "payment_query",
    "technical_support",
    "human_support"
}


def get_intent_names():
    """Return all available intent names."""
    return list(INTENTS.keys())


def get_intent_description(intent_name):
    """Return the description of an intent."""
    return INTENTS.get(intent_name, {}).get("description", "")