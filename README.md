# zotero-qa

QA your Zotero collections with Mistral LLM

```
set -a; source .env; set +a
brew install --cask Ollama
OLLAMA_MODELS=$OLLAMA_MODELS open /Applications/Ollama.app
ollama create zotero -f modelfile
```
