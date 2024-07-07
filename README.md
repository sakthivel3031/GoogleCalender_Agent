# GoogleCalender_Agent
An Googlecalender Agent is an fastAPI application which is used for Manage our Googlecalender by our Natural language.

### To Create Credentials ,

```
https://google-calendar-simple-api.readthedocs.io/en/latest/getting_started.html
```



### To download model just run below code,
```
from huggingface_hub import snapshot_download
from pathlib import Path

mistral_models_path = Path.home().joinpath('mistral_models', '7B-Instruct-v0.3')
mistral_models_path.mkdir(parents=True, exist_ok=True)

snapshot_download(repo_id="mistralai/Mistral-7B-Instruct-v0.3", allow_patterns=["params.json", "consolidated.safetensors", "tokenizer.model.v3"], local_dir=mistral_models_path)
```