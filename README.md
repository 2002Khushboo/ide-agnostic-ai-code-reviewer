# IDE-Agnostic Local AI Code Reviewer

A lightweight, offline, IDE-agnostic AI assistant for reviewing code — designed to work with **Keil**, **Visual Studio**, **VS Code**, and other legacy or restricted development environments.
This tool runs alongside your editor, not inside it.

## Why This Project Exists

Most AI coding tools today:
- Depend heavily on modern IDE plugins
- Require cloud APIs and paid subscriptions
- Are difficult or impossible to use with legacy tools like **Keil**
- Auto-generate code instead of encouraging understanding

This project explores a different idea:

> **What if AI acted as a reviewer and reasoning companion, not an autocomplete engine — and worked with any IDE?**

The goal is not to replace Copilot, but to support:
- Embedded and legacy workflows
- Offline or privacy-restricted environments
- Learning-focused and safety-critical development

## Features

- ✅ **IDE-agnostic** — works with Keil, Visual Studio, VS Code, or any editor
- ✅ **Offline & private** — uses a local LLM via Ollama
- ✅ **No plugins required**
- ✅ **Hotkey-based workflow**
- ✅ **Non-intrusive** — suggestions only, no auto-editing
- ✅ **Suitable for embedded and regulated environments**

## How It Works

1. Copy code from any IDE
2. Press a global hotkey (`Ctrl + Shift + A`)
3. A small floating window displays AI feedback:
   - Potential issues
   - Bad practices
   - Improvement suggestions
   - General code review notes

The AI model runs **locally** on your machine.  
No code is sent to the cloud.

## Tech Stack

- **Language:** Python 3
- **UI:** Tkinter
- **Clipboard:** `pyperclip`
- **Hotkeys:** `keyboard`
- **Local LLM Runtime:** Ollama
- **Model (default):** `codellama:7b`

## Project Structure
```
.
├── main.py # Entry point, hotkey + app glue
├── ui.py # Floating window UI
├── ai_client.py # Local LLM (Ollama) integration
├── requirements.txt
└── README.md
```

## Setup & Run

### 1. Install Ollama
Download and install Ollama from:
https://ollama.com

Verify installation:
```ollama --version```
### 2. Pull a coding model
```ollama run codellama:7b```

The model will download on first run.

Exit with:
```/bye```
### 3. Install Python dependencies
```pip install -r requirements.txt```
### 4. Run the application
```python main.py```

A floating window should appear.

### 5. Use the tool
Copy code from Keil / Visual Studio / VS Code

Press Ctrl + Shift + A

Review AI feedback in the floating window

## Known Limitations
This is an early prototype by design.

❌ No project-wide context

❌ No AST or symbol awareness

❌ No inline code editing

❌ Slower than cloud-based AI (local models)

These tradeoffs are intentional to preserve:

IDE independence
Privacy
Simplicity
Compatibility with legacy tools

## Philosophy
AI should assist thinking, not replace it.

This tool is intentionally designed to suggest, not inject — acting more like a senior engineer reviewing your code than an autocomplete engine.

## Status
This project is an experimental prototype intended for learning, exploration, and discussion around IDE-agnostic AI tooling.

Feedback, ideas, and critique are welcome.
