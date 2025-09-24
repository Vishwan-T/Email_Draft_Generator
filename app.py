from flask import Flask, render_template, request
import requests
import os
import markdown

app = Flask(__name__)

# Load API key from environment variable
API_KEY = os.getenv("GROQ_API_KEY")  # make sure you export/set this in your system
API_URL = "https://api.groq.com/openai/v1/chat/completions"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate_email():
    # Get user input from form
    prompt = request.form.get("prompt", "")
    tone = request.form.get("tone", "professional")

    # Prepare headers
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Prepare request body
    body = {
        "model": "openai/gpt-oss-20b",
        "messages": [
            {"role": "system", "content": f"You are an assistant that writes {tone} emails."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    # Send request
    response = requests.post(API_URL, headers=headers, json=body)

    # Handle API errors
    if response.status_code != 200:
        err = response.json()
        return render_template("result.html", email=f"<p>⚠️ Error: {err}</p>")

    # Parse response
    result = response.json()
    email_text = result["choices"][0]["message"]["content"]

    # Convert Markdown to HTML for better formatting
    email_html = markdown.markdown(email_text)

    # Render result page
    return render_template("result.html", email=email_html)


if __name__ == "__main__":
    app.run(debug=True)
