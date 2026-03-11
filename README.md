# ✈️ Travel Booking Chatbot

> A rule-based conversational chatbot that answers travel booking queries — built with a **Flask** backend and an **HTML** frontend.

---

## 📌 Project Overview

This project is a travel-focused chatbot that acts as a customer support assistant for a transport/booking service. Users interact with the bot through a simple web interface, and it responds to common booking-related questions using keyword matching logic in Python.

The project demonstrates how to build a lightweight, functional end-to-end chatbot from scratch — no external AI API or machine learning required.

---

## 🤖 How It Works

The chatbot uses a **rule-based keyword matching** approach:

1. The user submits a message via the web form (`index.html`)
2. The form sends a `POST` request to the Flask backend (`app.py`)
3. The `get_response()` function checks the message for known keywords
4. A matching response is returned and rendered back on the page

---

## 💬 Supported Queries

| User Intent | Trigger Keywords | Bot Response |
|-------------|-----------------|--------------|
| Operating hours | `"24 hours"`, `"operate"` | Confirms 24/7 availability |
| Refunds & cancellations | `"refund"`, `"cancel"` | Explains the 24-hour cancellation policy |
| Driver contact details | `"contact"`, `"driver"` | Shares driver details policy (2hrs before departure via SMS) |
| Anything else | — | Prompts user to ask about hours, refunds, or driver contact |

---

## 🗂️ Repository Structure

```
Travel-chatbot/
│
├── app.py          # Flask backend — routing & chatbot logic
├── index.html      # Frontend — chat interface
└── README.md
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Frontend | HTML |
| Chatbot Logic | Rule-based keyword matching |
| Communication | HTTP POST form submission |

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/Setur413/Travel-chatbot.git
   cd Travel-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install flask
   ```

3. **Start the Flask server**
   ```bash
   python app.py
   ```

4. **Open the chatbot in your browser**
   ```
   http://127.0.0.1:5000
   ```

---

## 💡 Example Interactions

```
User:  Do you operate 24 hours?
Bot:   Yes, we operate 24 hours every day.

User:  Can I get a refund if I cancel?
Bot:   Yes, we offer refunds for cancellations made 24 hours before departure.

User:  How do I contact my driver?
Bot:   For security reasons, we only share driver contact details 2 hours
       before departure via SMS.

User:  What's the weather like?
Bot:   I'm here to help with booking-related queries. Try asking about
       operation hours, refunds, or driver contact.
```

---

## 📌 Potential Improvements

- [ ] Add more keyword rules (e.g., pricing, luggage, pickup locations)
- [ ] Upgrade to NLP-based intent detection using spaCy or an LLM API
- [ ] Replace form-based submission with a real-time chat using JavaScript/AJAX
- [ ] Add session memory so the bot can reference earlier messages in a conversation
- [ ] Deploy to a cloud platform (Render, Railway, or Heroku)

---

*Author: Jonah Tarus*
