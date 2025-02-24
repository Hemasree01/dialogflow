import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="My Chatbot", layout="wide")

st.title("Chat with Dialogflow")

# Embed Dialogflow Messenger
html_code = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
  <meta http-equiv="Pragma" content="no-cache" />
  <meta http-equiv="Expires" content="0" />
  
  <link rel="stylesheet" href="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/themes/df-messenger-default.css">
  <script src="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/df-messenger.js"></script>
</head>
<body>

<df-messenger
  location="us-central1"
  project-id="resolute-winter-447814-t5"
  agent-id="d1c9667d-9e33-4bf8-8e92-36ede758bc37"
  language-code="en"
  max-query-length="-1"
  allow-feedback="all">
  <df-messenger-chat-bubble chat-title="demo"></df-messenger-chat-bubble>
</df-messenger>

<style>
  df-messenger {
    z-index: 999;
    position: fixed;
    bottom: 16px;
    right: 16px;
    --df-messenger-font-color: #000;
    --df-messenger-font-family: "Google Sans", sans-serif;
    --df-messenger-chat-background: #f3f6fc;
    --df-messenger-message-user-background: #d3e3fd;
    --df-messenger-message-bot-background: #fff;
  }
</style>

<script>
  document.addEventListener('DOMContentLoaded', () => {
    const dfMessenger = document.querySelector('df-messenger');

    // Render a custom text message from the agent
    dfMessenger.renderCustomText('Hello! How can I assist you today?', true);

    // Render a custom card response
    const payload = [
      {
        "type": "info",
        "title": "Info item title",
        "subtitle": "Info item subtitle",
        "image": {
          "rawUrl": "https://example.com/images/logo.png"
        },
        "anchor": {
          "href": "https://example.com",
          "target": "_blank"
        }
      }
    ];
    dfMessenger.renderCustomCard(payload);

    // Send a query to the Dialogflow API
    dfMessenger.sendQuery('Describe shipping costs.');

    // Set query parameters
    const queryParameters = {
      parameters: {
        timeZone: "America/New_York"
      }
    };
    dfMessenger.setQueryParameters(queryParameters);

    // Set context for personalization
    const metadata = {
      "subscription plan": "Business Premium Plus",
      "devices owned": [
        { model: "Google Pixel 7" },
        { model: "Google Pixel Tablet" }
      ]
    };
    dfMessenger.setContext(metadata);

    // Open the chat window
    const dfMessengerBubble = document.querySelector('df-messenger-chat-bubble');
    dfMessengerBubble.openChat();
  });
</script>

</body>
</html>
"""

components.html(html_code, height=700)
