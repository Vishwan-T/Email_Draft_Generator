# 📧 AI Email Draft Generator

A modern web application that generates professional email drafts using AI-powered language models through the Groq API. Built with Flask and styled with Tailwind CSS for a sleek, responsive user interface.

![](https://github.com/Vishwan-T/Email_Draft_Generator/blob/main/Input.png)
![](https://github.com/Vishwan-T/Email_Draft_Generator/blob/main/Output.png)

## ✨ Features

- **AI-Powered Email Generation**: Leverages Groq's language models to create contextual email content
- **Multiple Tone Options**: Choose from professional, casual, friendly, or apologetic tones
- **Modern UI**: Clean, gradient-based design with responsive layout

## 🚀 Demo

The application provides:
1. A form to input your email request and select tone
2. AI processing through Groq API
3. Formatted email output with copy functionality
4. Navigation to generate additional emails

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, Tailwind CSS
- **AI Service**: Groq API
- **Template Engine**: Jinja2
- **Markdown Processing**: Python-markdown

## 📋 Prerequisites

- Python 3.7 or higher
- Groq API key (sign up at [Groq](https://groq.com))

## 🔧 Installation

1. **Clone the repository** 
2. **Install dependencies**
3. **Set up environment variables**
4. **Run the application**
5. **Open your browser**
Navigate to `http://localhost:5000`


## 🎯 Usage

1. **Enter Your Request**: Describe what kind of email you need (e.g., "Write a leave application for medical reasons")

2. **Select Tone**: Choose from:
   - Professional (default)
   - Casual
   - Friendly
   - Apologetic

3. **Generate**: Click the "Generate Email" button

4. **Copy & Use**: Review the generated email and copy it to your clipboard



## 🔑 API Configuration

The application uses the Groq API with the following configuration:
- Model: `openai/gpt-oss-20b`
- Temperature: 0.7 (balanced creativity)
- Endpoint: `https://api.groq.com/openai/v1/chat/completions`

## 🎨 Customization

### Adding New Tones
Edit the `<select>` options in `templates/index.html`:


