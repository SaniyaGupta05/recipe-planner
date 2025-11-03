#!/usr/bin/env python3
"""
Basic validation script for CI/CD pipeline
"""

import os
import sys

def check_imports():
    """Check if all required packages can be imported"""
    try:
        import flask
        print("✓ Flask imported successfully")
        
        # Try to import Groq but don't fail if API key is missing
        try:
            from groq import Groq
            print("✓ Groq client imported successfully")
        except ImportError as e:
            print(f"✗ Groq import failed: {e}")
            return False
            
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False

def check_files():
    """Check if essential files exist"""
    essential_files = [
        'app/app.py',
        'requirements.txt', 
        'Dockerfile',
        '.github/workflows/ci-cd.yml'
    ]
    
    all_exist = True
    for file in essential_files:
        if os.path.exists(file):
            print(f"✓ {file} exists")
        else:
            print(f"✗ {file} missing")
            all_exist = False
            
    return all_exist

def check_environment():
    """Check environment variables"""
    if os.getenv('GROQ_API_KEY'):
        print("✓ GROQ_API_KEY is set in environment")
    else:
        print("⚠ GROQ_API_KEY not set (expected in CI environment)")

if __name__ == "__main__":
    print("Running CI/CD validation checks...")
    print("=" * 50)
    
    files_ok = check_files()
    imports_ok = check_imports() 
    check_environment()
    
    print("=" * 50)
    
    if files_ok and imports_ok:
        print("✓ All validation checks passed!")
        sys.exit(0)
    else:
        print("✗ Some validation checks failed")
        sys.exit(1)
