
---

# YouTube Video Transcript

Follow these steps to set up and run the project locally.

---

## Step 1: Create and Activate Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

*Note: On Windows, activate the environment using:*

```bash
.venv\Scripts\activate
```

---

## Step 2: Start the Database

Make sure Docker is installed and running, then execute:

```bash
docker compose -f docker-compose.db.yml up
```

This will start the database service defined in the Docker Compose file.

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Configure Environment Variables

Add your Large Language Model (LLM) API key and any other necessary variables to the `.env` file.

---

## Step 6: Launch the Streamlit App

```bash
python -m streamlit run renderPage.py
```

This will start the Streamlit server and open the app in your default web browser.

here you can enter youtube url to summarize script.

![alt text](<Screenshot 2025-04-20 at 5.58.47 PM.png>)
---