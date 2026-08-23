import { useState } from "react";
import "./App.css";

const API_URL = "http://127.0.0.1:5000/api/chat";

function App() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const suggestions = [
    "What internships are available?",
    "How can I apply?",
    "What courses do you offer?",
    "How can I contact support?",
  ];

  // Send message to Flask backend
  const sendMessage = async (text) => {
    const userMessage = (text ?? "").trim();

    if (!userMessage || loading) {
      return;
    }

    console.log("SEND BUTTON CLICKED");
    console.log("Sending message:", userMessage);

    // Show user's message
    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: userMessage,
      },
    ]);

    setMessage("");
    setLoading(true);

    try {
      console.log("Calling backend:", API_URL);

      const response = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: userMessage,
        }),
      });

      console.log("Backend status:", response.status);

      const data = await response.json();

      console.log("Backend response:", data);

      if (!response.ok) {
        throw new Error(
          data.error || "Backend request failed"
        );
      }

      // Show AI response
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content:
            data.response ||
            "Sorry, I couldn't generate a response.",
        },
      ]);

    } catch (error) {
      console.error("Chat error:", error);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content:
            "Sorry, I couldn't connect to the AI service. Please make sure the Flask backend is running.",
        },
      ]);

    } finally {
      setLoading(false);
    }
  };

  // Enter key
  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      sendMessage(message);
    }
  };

  return (
    <div className="app">

      {/* Background effects */}
      <div className="glow glow-one"></div>
      <div className="glow glow-two"></div>

      {/* Navbar */}
      <header className="navbar">

        <div className="brand">

          <div className="brand-icon">
            ✦
          </div>

          <div>
            <h2>VaultOfCodes</h2>
            <span>AI Support</span>
          </div>

        </div>

        <div className="nav-status">
          <span className="status-dot"></span>
          AI Assistant Online
        </div>

      </header>

      {/* Main */}
      <main className="main">

        {/* Hero */}
        <section className="hero-section">

          <div className="ai-orb">
            <div className="orb-inner">
              ✦
            </div>
          </div>

          <div className="badge">
            <span>✦</span>
            AI-Powered Support
          </div>

          <h1>
            Your questions.
            <br />
            <span>Instantly answered.</span>
          </h1>

          <p className="subtitle">
            Meet the VaultOfCodes AI Assistant — your intelligent
            companion for internships, courses, applications and support.
          </p>

        </section>

        {/* Chat Card */}
        <section className="chat-card">

          {/* Chat Header */}
          <div className="chat-header">

            <div className="assistant-profile">

              <div className="mini-orb">
                ✦
              </div>

              <div>
                <h3>VaultofCodes AI Assistant</h3>

                <p>
                  <span className="online-dot"></span>
                  Always here to help
                </p>
              </div>

            </div>

            <div className="header-badge">
              AI
            </div>

          </div>

          {/* Conversation */}
          <div className="conversation">

            {/* Welcome message */}
            <div className="message-row">

              <div className="message-avatar">
                ✦
              </div>

              <div className="ai-message">

                <span className="message-label">
                  Vault AI
                </span>

                <p>
                  Hi there! 👋 I'm your VaultOfCodes AI Assistant.
                  How can I help you today?
                </p>

                <span className="time">
                  Just now
                </span>

              </div>

            </div>

            {/* User + AI messages */}
            {messages.map((msg, index) => (

              <div
                className={`message-row ${
                  msg.role === "user"
                    ? "user-row"
                    : ""
                }`}
                key={index}
              >

                {/* AI avatar */}
                {msg.role === "assistant" && (
                  <div className="message-avatar">
                    ✦
                  </div>
                )}

                <div
                  className={
                    msg.role === "user"
                      ? "user-message"
                      : "ai-message"
                  }
                >

                  <span className="message-label">
                    {msg.role === "user"
                      ? "You"
                      : "Vault AI"}
                  </span>

                  <p>
                    {msg.content}
                  </p>

                  <span className="time">
                    Just now
                  </span>

                </div>

              </div>

            ))}

            {/* Loading */}
            {loading && (

              <div className="message-row">

                <div className="message-avatar">
                  ✦
                </div>

                <div className="ai-message">

                  <span className="message-label">
                    Vault AI
                  </span>

                  <p className="typing">
                    Thinking
                    <span>.</span>
                    <span>.</span>
                    <span>.</span>
                  </p>

                </div>

              </div>

            )}

          </div>

          {/* Suggestions */}
          <div className="suggestions-section">

            <p className="suggestion-title">
              Popular questions
            </p>

            <div className="suggestions">

              {suggestions.map((item, index) => (

                <button
                  type="button"
                  key={index}
                  onClick={() => sendMessage(item)}
                  disabled={loading}
                >
                  <span>✦</span>
                  {item}
                </button>

              ))}

            </div>

          </div>

          {/* Input */}
          <div className="input-area">

            <div className="input-wrapper">

              <input
                type="text"
                placeholder="Ask Vault AI anything..."
                value={message}
                onChange={(e) =>
                  setMessage(e.target.value)
                }
                onKeyDown={handleKeyDown}
                disabled={loading}
              />

              <button
                type="button"
                className="send-button"
                onClick={() => {
                  console.log("SEND BUTTON CLICKED");
                  sendMessage(message);
                }}
                disabled={
                  loading ||
                  !message.trim()
                }
                aria-label="Send message"
              >

                <svg
                  width="20"
                  height="20"
                  viewBox="0 0 24 24"
                  fill="none"
                >

                  <path
                    d="M22 2L11 13"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  />

                  <path
                    d="M22 2L15 22L11 13L2 9L22 2Z"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  />

                </svg>

              </button>

            </div>

            <p className="privacy">
              ✦ AI-generated responses may occasionally be inaccurate.
            </p>

          </div>

        </section>

        {/* Features */}
        <section className="features">

          <div className="feature">

            <div className="feature-icon">
              ⚡
            </div>

            <div>
              <h4>Instant Support</h4>
              <p>Get answers in seconds</p>
            </div>

          </div>

          <div className="feature">

            <div className="feature-icon">
              ◈
            </div>

            <div>
              <h4>Smart Assistance</h4>
              <p>Understands your questions</p>
            </div>

          </div>

          <div className="feature">

            <div className="feature-icon">
              ♢
            </div>

            <div>
              <h4>Human Escalation</h4>
              <p>Support when you need it</p>
            </div>

          </div>

        </section>

      </main>

      {/* Footer */}
      <footer>

        <span>
          © 2026 VaultOfCodes
        </span>

        <span>
          Powered by AI • Built for learners
        </span>

      </footer>

    </div>
  );
}

export default App;