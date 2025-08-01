@echo off
:: DeFi Guardian Swarm - Quick Start Script for Windows
echo 🚀 DeFi Guardian Swarm - Quick Start
echo ==================================

:: Check if we're in the JuliaOS directory
if not exist "README.md" (
    echo ❌ Please run this script from the JuliaOS root directory
    pause
    exit /b 1
)
if not exist "backend" (
    echo ❌ Please run this script from the JuliaOS root directory
    pause
    exit /b 1
)

echo 📁 Working directory: %cd%

:: Step 1: Setup environment file
echo.
echo 📝 Setting up environment configuration...
if not exist "backend\.env" (
    if exist "backend\.env.defi_guardian_example" (
        copy "backend\.env.defi_guardian_example" "backend\.env" >nul
        echo ✅ Created .env file from DeFi Guardian example
    ) else if exist "backend\.env.example" (
        copy "backend\.env.example" "backend\.env" >nul
        echo ✅ Created .env file from example
    ) else (
        echo ❌ No .env example file found
        pause
        exit /b 1
    )
) else (
    echo ✅ .env file already exists
)

:: Step 2: Check for OpenAI API key
echo.
echo 🔑 Checking OpenAI API key...
findstr /C:"OPENAI_API_KEY=your_openai_api_key_here" "backend\.env" >nul
if %errorlevel% equ 0 (
    echo ⚠️  WARNING: OpenAI API key not configured!
    echo Please edit backend\.env and add your OpenAI API key:
    echo OPENAI_API_KEY=your_actual_api_key_here
    echo.
    pause
)

:: Step 3: Start JuliaOS backend
echo.
echo 🔧 Starting JuliaOS backend...
cd backend

:: Check for docker compose
docker compose version >nul 2>&1
if %errorlevel% equ 0 (
    echo Using docker compose...
    docker compose up -d
) else (
    docker-compose --version >nul 2>&1
    if %errorlevel% equ 0 (
        echo Using docker-compose...
        docker-compose up -d
    ) else (
        echo ❌ Docker not found. Please install Docker and try again.
        pause
        exit /b 1
    )
)

:: Wait for backend to start
echo ⏳ Waiting for backend to start...
timeout /t 15 /nobreak >nul

:: Check if backend is running
echo 🔍 Checking backend status...
curl -s http://127.0.0.1:8052/api/v1/ping >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ JuliaOS backend is running
) else (
    echo ❌ Backend not responding. Check Docker logs:
    echo docker logs backend-julia-backend-1
    pause
    exit /b 1
)

cd ..

:: Step 4: Install Python dependencies
echo.
echo 🐍 Installing Python dependencies...
cd python

:: Try pip3 first, then pip
pip3 --version >nul 2>&1
if %errorlevel% equ 0 (
    pip3 install -e .
) else (
    pip --version >nul 2>&1
    if %errorlevel% equ 0 (
        pip install -e .
    ) else (
        echo ❌ pip not found. Please install Python and pip.
        pause
        exit /b 1
    )
)

:: Install additional requirements if available
if exist "defi_guardian_requirements.txt" (
    echo 📦 Installing additional requirements...
    pip install -r defi_guardian_requirements.txt
)

cd ..

:: Step 5: Run the DeFi Guardian Swarm
echo.
echo 🚀 Starting DeFi Guardian Swarm...
python python\scripts\run_defi_guardian_swarm.py

echo.
echo 🎉 DeFi Guardian Swarm setup complete!
echo.
echo To run again in the future:
echo   1. Start backend: cd backend ^&^& docker compose up -d
echo   2. Run swarm: python python\scripts\run_defi_guardian_swarm.py
pause
