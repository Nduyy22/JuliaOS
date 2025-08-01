#!/usr/bin/env python3
"""
DeFi Guardian Swarm Setup Script

This script helps you set up and run the DeFi Guardian Swarm system
on the JuliaOS framework.

Usage:
    python setup_defi_guardian.py [--check-only]
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 11):
        print("❌ Python 3.11 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version}")
    return True

def check_juliaos_backend():
    """Check if JuliaOS backend is accessible"""
    try:
        import requests
        response = requests.get("http://127.0.0.1:8052/api/v1/ping", timeout=5)
        if response.status_code == 200:
            print("✅ JuliaOS backend is running")
            return True
        else:
            print(f"❌ JuliaOS backend returned status {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Cannot connect to JuliaOS backend: {e}")
        print("Make sure to run: cd backend && docker compose up")
        return False

def check_juliaos_package():
    """Check if juliaos package is installed"""
    try:
        import juliaos
        print("✅ juliaos package is installed")
        return True
    except ImportError:
        print("❌ juliaos package not found")
        print("Install with: cd python && pip install -e .")
        return False

def check_openai_api_key():
    """Check if OpenAI API key is configured"""
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key and len(api_key) > 10:
        print("✅ OpenAI API key is configured")
        return True
    else:
        print("❌ OpenAI API key not found")
        print("Set OPENAI_API_KEY in your .env file")
        return False

def check_env_file():
    """Check if .env file exists in backend directory"""
    backend_dir = Path(__file__).parent / "backend"
    env_file = backend_dir / ".env"
    
    if env_file.exists():
        print("✅ .env file found in backend directory")
        return True
    else:
        print("❌ .env file not found in backend directory")
        print("Copy from: cp backend/.env.example backend/.env")
        return False

def install_dependencies():
    """Install required dependencies"""
    print("\n🔧 Installing dependencies...")
    
    # Install base juliaos package
    try:
        subprocess.run([
            sys.executable, "-m", "pip", "install", "-e", "python/"
        ], check=True, cwd=Path(__file__).parent)
        print("✅ Installed juliaos package")
    except subprocess.CalledProcessError:
        print("❌ Failed to install juliaos package")
        return False
    
    # Install additional requirements
    requirements_file = Path(__file__).parent / "python" / "defi_guardian_requirements.txt"
    if requirements_file.exists():
        try:
            subprocess.run([
                sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
            ], check=True)
            print("✅ Installed additional requirements")
        except subprocess.CalledProcessError:
            print("❌ Failed to install additional requirements")
            return False
    
    return True

def setup_env_file():
    """Setup .env file if it doesn't exist"""
    backend_dir = Path(__file__).parent / "backend"
    env_file = backend_dir / ".env"
    example_file = backend_dir / ".env.example"
    guardian_example = backend_dir / ".env.defi_guardian_example"
    
    if not env_file.exists():
        if guardian_example.exists():
            print("📝 Setting up .env file from DeFi Guardian example...")
            try:
                with open(guardian_example, 'r') as src:
                    content = src.read()
                with open(env_file, 'w') as dst:
                    dst.write(content)
                print("✅ Created .env file from DeFi Guardian example")
                print("⚠️  Please edit backend/.env and add your OpenAI API key")
                return True
            except Exception as e:
                print(f"❌ Failed to create .env file: {e}")
                return False
        elif example_file.exists():
            print("📝 Setting up .env file from example...")
            try:
                with open(example_file, 'r') as src:
                    content = src.read()
                with open(env_file, 'w') as dst:
                    dst.write(content)
                print("✅ Created .env file from example")
                print("⚠️  Please edit backend/.env and add your OpenAI API key")
                return True
            except Exception as e:
                print(f"❌ Failed to create .env file: {e}")
                return False
    
    return True

def run_system_check():
    """Run comprehensive system check"""
    print("🔍 DeFi Guardian Swarm - System Check")
    print("=" * 50)
    
    checks = [
        ("Python Version", check_python_version),
        ("Environment File", check_env_file),
        ("JuliaOS Package", check_juliaos_package),
        ("OpenAI API Key", check_openai_api_key),
        ("JuliaOS Backend", check_juliaos_backend),
    ]
    
    all_passed = True
    for name, check_func in checks:
        print(f"\n📋 Checking {name}...")
        if not check_func():
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All checks passed! System is ready to run.")
        print("\nTo start DeFi Guardian Swarm:")
        print("python python/scripts/run_defi_guardian_swarm.py")
    else:
        print("❌ Some checks failed. Please fix the issues above.")
    
    return all_passed

def setup_system():
    """Setup the complete system"""
    print("🚀 DeFi Guardian Swarm - System Setup")
    print("=" * 50)
    
    # Check Python version first
    if not check_python_version():
        return False
    
    # Setup .env file
    if not setup_env_file():
        return False
    
    # Install dependencies
    if not install_dependencies():
        return False
    
    # Run final check
    print("\n🔍 Running final system check...")
    return run_system_check()

def main():
    parser = argparse.ArgumentParser(description="Setup DeFi Guardian Swarm system")
    parser.add_argument("--check-only", action="store_true", 
                       help="Only run system check, don't install anything")
    args = parser.parse_args()
    
    if args.check_only:
        success = run_system_check()
    else:
        success = setup_system()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
