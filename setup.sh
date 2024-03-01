#!/usr/bin/env bash

# This script is used to set up the environment for the project.
set -a; source .env; set +a
brew install --cask Ollama
OLLAMA_MODELS=$OLLAMA_MODELS open /Applications/Ollama.app
ollama create zotero -f modelfile
