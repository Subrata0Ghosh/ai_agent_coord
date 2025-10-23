#!/bin/bash
echo "🛑 Stopping all running AI Agent servers..."
pkill -f "uvicorn"
pkill -f "node"
echo "✅ All servers stopped."
