import os
from dotenv import load_dotenv

def load_configuration():
    """Load environment variables from .env file."""
    load_dotenv()
    os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
