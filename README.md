# AI CMO Automation

AI-powered Chief Marketing Officer automation combining Python AI agents with Node.js marketing workflows.

## Architecture

This project uses a hybrid approach:
- **Python**: AI agents for content generation, analytics, and strategy
- **Node.js**: Marketing workflow automation and orchestration

## Project Structure

```
AI CMO/
├── python/                 # Python AI agents
│   ├── agents/            # AI agent implementations
│   │   ├── content_agent.py      # Content generation
│   │   ├── analytics_agent.py    # Marketing analytics
│   │   └── strategy_agent.py     # Strategy development
│   ├── utils/             # Utility functions
│   └── main.py            # Python entry point
├── src/                   # Node.js workflows
│   ├── workflows/         # Marketing automation workflows
│   │   ├── contentGenerator.js   # Content generation
│   │   └── campaignManager.js    # Campaign management
│   └── index.js           # Node.js entry point
└── requirements.txt       # Python dependencies
```

## Setup

### Python Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Node.js Setup
```bash
# Install dependencies
npm install
```

### Environment Variables
```bash
# Copy example env file
cp .env.example .env

# Add your API keys to .env
```

## Usage

### Run Python Agents
```bash
python python/main.py
```

### Run Node.js Workflows
```bash
npm run dev
```

## Features

### AI Agents (Python)
- **Content Agent**: Generate and optimize marketing content
- **Analytics Agent**: Analyze campaign performance and predict trends
- **Strategy Agent**: Develop marketing strategies and competitive analysis

### Workflows (Node.js)
- **Content Generation**: Blog posts, social media, email campaigns
- **Campaign Management**: Create, schedule, and analyze campaigns
- **Social Media Automation**: Multi-platform posting and engagement

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT
