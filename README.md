# My Notes RAG

A Retrieval-Augmented Generation (RAG) system that ingests user notes and answers questions based on them. Built with Python, and OpenAI for intelligent, context-aware responses.

## Features

- **Note Ingestion**: Upload and process text/PDF notes into a searchable vector database.
- **Question Answering**: Ask questions and get AI-generated answers grounded in your notes.
- **Modular Design**: Separate components for ingestion, retrieval, and generation for easy extension.

## Table of Contents

- [My Notes RAG](#my-notes-rag)
  - [Features](#features)
  - [Table of Contents](#table-of-contents)
  - [Goal of the project](#goal-of-the-project)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Steps](#steps)
  - [Quick Start](#quick-start)
  - [Configuration](#configuration)
  - [Development](#development)
    - [Project Structure](#project-structure)

## Goal of the project

Build a personal RAG assistant that ingests notes and answers questions based only on those notes

## Installation

### Prerequisites

- Python 3.13 (recommended; dependencies are currently locked against this version)
- OpenAI API key (sign up at [OpenAI](https://platform.openai.com/))

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/jizhiwang0725/my-notes-rag.git
   cd my-notes-rag
   ```

2. Create a virtual environment:

   ```bash
   python3.13 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   `requirements.txt` locks the
   resolved dependency versions for the tested Python environment.

## Quick Start

1. Add notes to `data/notes/` (e.g., `.txt` or `.pdf` files).
2. From the repository root, run the app as a module:
   ```bash
   ./.venv/bin/python -m src.app
   ```
3. Type your question in the interactive prompt. Enter `q` to quit.

## Configuration

No environment variables or OpenAI API key are required. The current code uses
the local Phi-3 model, the `all-MiniLM-L6-v2` embedding model, and stores the
vector database in `data/vector_db/`.

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

_Built with ❤️ for personal knowledge management._
