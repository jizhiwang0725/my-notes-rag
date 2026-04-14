# My Notes RAG

<!-- Badges: Add these if you set up CI/CD (e.g., GitHub Actions) -->
<!-- [![Build Status](https://img.shields.io/github/actions/workflow/status/yourusername/my-notes-rag/ci.yml)](https://github.com/yourusername/my-notes-rag/actions) -->
<!-- [![License](https://img.shields.io/github/license/yourusername/my-notes-rag)](LICENSE) -->

A Retrieval-Augmented Generation (RAG) system that ingests user notes and answers questions based on them. Built with Python,  , and OpenAI for intelligent, context-aware responses.

## Features

- **Note Ingestion**: Upload and process text/PDF notes into a searchable vector database.
- **Question Answering**: Ask questions and get AI-generated answers grounded in your notes.
- **Modular Design**: Separate components for ingestion, retrieval, and generation for easy extension.
- **Privacy-Focused**: Local storage with optional encryption for sensitive notes.
- **Web/CLI Interface**: Simple API or command-line tool for interaction.

## Table of Contents

- [My Notes RAG](#my-notes-rag)
  - [Features](#features)
  - [Table of Contents](#table-of-contents)
  - [Goal of the project](#goal-of-the-project)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Steps](#steps)
  - [Usage](#usage)
    - [Quick Start](#quick-start)
    - [Web Interface (if implemented)](#web-interface-if-implemented)
    - [Examples](#examples)
  - [Configuration](#configuration)
  - [API Reference](#api-reference)
  - [Development](#development)
    - [Project Structure](#project-structure)
  - [Contributing](#contributing)
  - [License](#license)
  - [Changelog](#changelog)
  - [Support](#support)

## Goal of the project ##

Build a personal RAG assistant that ingests notes and answers questions based only on those notes  

## Installation

### Prerequisites
- Python 3.10 or higher
- OpenAI API key (sign up at [OpenAI](https://platform.openai.com/))

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/my-notes-rag.git
   cd my-notes-rag
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your `OPENAI_API_KEY` to `.env`

## Usage

### Quick Start
1. Add notes to `data/notes/` (e.g., `.txt` or `.pdf` files).
2. Run the app:
   ```bash
   python src/app.py
   ```
3. Ask a question via CLI:
   ```bash
   python src/app.py ask "What are the key points from my meeting notes?"
   ```

### Web Interface (if implemented)
- Start the server: `uvicorn src.app:app --reload`
- Open `http://localhost:8000` and upload notes/ask questions.

### Examples
- Upload notes: `python src/app.py upload data/notes/sample.txt`
- Query: `python src/app.py ask "Summarize my project ideas"`

## Configuration

- Edit `src/config.py` for settings like embedding model or vector DB path.
- Environment variables in `.env`:
  - `OPENAI_API_KEY`: Your OpenAI key
  - `VECTOR_DB_PATH`: Path to vector database (default: `data/vector_db/`)

## API Reference

If using FastAPI, document endpoints here (auto-generated via `/docs`).

- `POST /upload-notes`: Upload notes for ingestion.
- `POST /ask-question`: Submit a question and get an answer.

## Development

### Project Structure
```
my-notes-rag/
├── src/                 # Source code
├── data/                # Notes and vector DB
├── tests/               # Unit tests
├── docs/                # Documentation
└── README.md            # This file
```

## Contributing

1. Fork the repo.
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m "Add your feature"`
4. Push and open a PR.

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

## Changelog

- **v0.1.0** (2026-04-12): Initial release with basic RAG pipeline.
- See [CHANGELOG.md](CHANGELOG.md) for full history.

## Support

- Issues: [GitHub Issues](https://github.com/yourusername/my-notes-rag/issues)
- Docs: [docs/](docs/)
- Email: your.email@example.com

---

*Built with ❤️ for personal knowledge management.*
