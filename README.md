# fastapi-practice

### Clone the repository

```bash
git clonegit@github.com:christiandls444/fastapi-practice.git
```

### Create a virtual environment

```bash
Mac/Linux: python3 -m venv .venv | Windows: python -m venv .venv
```

### Activate the virtual environment

```bash
Mac/Linux: source .venv/bin/activate | Windows: .venv\Scripts\activate
```

### Install the dependencies

```bash
pip install -r requirements.txt
```

### Run the server

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload | Remove: --reload for production
```

### Stop the server

```bash
Ctrl + C
```

### Deactivate the virtual environment

```bash
deactivate
```

