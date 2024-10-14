# eyeofgod_list_request

This project handles requests from a phone list to the eyeofgod Telegram bot.

## Installation

### Set up Virtual Environment

1. Install venv:
```
python -m venv venv
```

2. Activate venv:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

### Install Dependencies

Install required packages:
```
pip install -r requirements.txt
```

### Configuration

1. Create `phone_list.txt` from `phone_list.txt.example`
2. Create `.env` file from `.env.example`

## Usage

### Windows
Run the batch file:
run.bat

### macOS and Linux
Execute the Python script:
```
python main.py
```

## Project Structure
eyeofgod_list_request/
├── venv/
├── main.py
├── requirements.txt
├── phone_list.txt
├── .env
├── run.bat
└── README.md