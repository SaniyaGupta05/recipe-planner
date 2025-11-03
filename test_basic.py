import os
import sys

# Add the app directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

try:
    # Test basic imports
    import flask
    from groq import Groq
    print("✓ All imports successful")
    
    # Test environment variable
    if os.getenv('GROQ_API_KEY'):
        print("✓ GROQ_API_KEY is set")
    else:
        print("⚠ GROQ_API_KEY not set (this is expected in CI)")
        
    print("✓ Basic validation passed")
    
except Exception as e:
    print(f"✗ Validation failed: {e}")
    sys.exit(1)
