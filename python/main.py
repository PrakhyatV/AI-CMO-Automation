import os
from dotenv import load_dotenv
from agents.content_agent import ContentAgent
from agents.analytics_agent import AnalyticsAgent
from agents.strategy_agent import StrategyAgent

load_dotenv()

def main():
    """Main entry point for Python-based AI agents"""
    print("🤖 AI CMO Agents Starting...")
    
    # Initialize agents
    content_agent = ContentAgent()
    analytics_agent = AnalyticsAgent()
    strategy_agent = StrategyAgent()
    
    print("✅ All agents initialized successfully!")
    print("📊 Available agents:")
    print("  - Content Agent: Generate marketing content")
    print("  - Analytics Agent: Analyze marketing data")
    print("  - Strategy Agent: Develop marketing strategies")

if __name__ == "__main__":
    main()
