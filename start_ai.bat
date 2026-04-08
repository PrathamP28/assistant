@echo off
echo Starting AI system...

:: Start Ollama server
start "" ollama serve

:: Wait a few seconds
timeout /t 5

:: Run preload script
start "" python preload.py
