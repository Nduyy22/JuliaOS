#!/bin/bash
# DeFi Guardian Swarm - Quick Start Script for Linux/Mac
# Windows users: use quick_start.bat

echo "🚀 DeFi Guardian Swarm - Quick Start"
echo "=================================="

# Check if we're in the JuliaOS directory
if [ ! -f "README.md" ] || [ ! -d "backend" ]; then
    echo "❌ Please run this script from the JuliaOS root directory"
    exit 1
fi

echo "📁 Working directory: $(pwd)"

# Step 1: Setup environment file
echo ""
echo "📝 Setting up environment configuration..."
if [ ! -f "backend/.env" ]; then
    if [ -f "backend/.env.defi_guardian_example" ]; then
        cp backend/.env.defi_guardian_example backend/.env
        echo "✅ Created .env file from DeFi Guardian example"
    elif [ -f "backend/.env.example" ]; then
        cp backend/.env.example backend/.env
        echo "✅ Created .env file from example"
    else
        echo "❌ No .env example file found"
        exit 1
    fi
else
    echo "✅ .env file already exists"
fi

# Step 2: Check for OpenAI API key
echo ""
echo "🔑 Checking OpenAI API key..."
if grep -q "OPENAI_API_KEY=your_openai_api_key_here" backend/.env || grep -q "OPENAI_API_KEY=$" backend/.env; then
    echo "⚠️  WARNING: OpenAI API key not configured!"
    echo "Please edit backend/.env and add your OpenAI API key:"
    echo "OPENAI_API_KEY=your_actual_api_key_here"
    echo ""
    read -p "Press Enter after you've updated the API key, or Ctrl+C to exit..."
fi

# Step 3: Start JuliaOS backend
echo ""
echo "🔧 Starting JuliaOS backend..."
cd backend
if command -v docker-compose >/dev/null 2>&1; then
    echo "Using docker-compose..."
    docker-compose up -d
elif command -v docker >/dev/null 2>&1 && docker compose version >/dev/null 2>&1; then
    echo "Using docker compose..."
    docker compose up -d
else
    echo "❌ Docker not found. Please install Docker and try again."
    exit 1
fi

# Wait for backend to start
echo "⏳ Waiting for backend to start..."
sleep 10

# Check if backend is running
echo "🔍 Checking backend status..."
if curl -s http://127.0.0.1:8052/api/v1/ping >/dev/null; then
    echo "✅ JuliaOS backend is running"
else
    echo "❌ Backend not responding. Check Docker logs:"
    echo "docker logs backend-julia-backend-1"
    exit 1
fi

cd ..

# Step 4: Install Python dependencies
echo ""
echo "🐍 Installing Python dependencies..."
cd python
if command -v pip3 >/dev/null 2>&1; then
    pip3 install -e .
elif command -v pip >/dev/null 2>&1; then
    pip install -e .
else
    echo "❌ pip not found. Please install Python and pip."
    exit 1
fi

# Install additional requirements if available
if [ -f "defi_guardian_requirements.txt" ]; then
    echo "📦 Installing additional requirements..."
    pip install -r defi_guardian_requirements.txt
fi

cd ..

# Step 5: Run the DeFi Guardian Swarm
echo ""
echo "🚀 Starting DeFi Guardian Swarm..."
python python/scripts/run_defi_guardian_swarm.py

echo ""
echo "🎉 DeFi Guardian Swarm setup complete!"
echo ""
echo "To run again in the future:"
echo "  1. Start backend: cd backend && docker compose up -d"
echo "  2. Run swarm: python python/scripts/run_defi_guardian_swarm.py"
