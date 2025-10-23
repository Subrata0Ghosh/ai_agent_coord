#!/bin/bash
echo "🚀 Starting all AI Agent servers..."

# Start Frontend Agent
echo "➡️ Starting Frontend Agent (Node.js on port 9001)..."
cd agents/frontend_agent
nohup node server.js > ../../output/frontend.log 2>&1 &

# Start Backend Agent
echo "➡️ Starting Backend Agent (FastAPI on port 9002)..."
cd ../backend_agent
nohup uvicorn app:app --port 9002 --reload > ../../output/backend.log 2>&1 &

# Start Coordinator
echo "➡️ Starting Coordinator (FastAPI on port 8000)..."
cd ../../coordinator
nohup uvicorn app:app --port 8000 --reload > ../output/coordinator.log 2>&1 &

echo "✅ All servers started successfully!"
echo "📄 Logs available in ./output/"
