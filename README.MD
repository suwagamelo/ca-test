# CS Quiz Engine 🧠

A Flask-based Computer-Based Test (CBT) application for CSC 202 Final CA.  
Students answer 20 Computer Science questions, get a timestamped score, and see a full question breakdown.

## What the App Does

- Displays **20 multiple-choice CS questions** covering OOP, Data Structures, Algorithms, Python, Web Development, and Version Control
- Tracks the student's **score and grade** (A–F)
- Shows a **timestamped result page** with a per-question breakdown (correct/wrong)
- Stores a **history of all submitted tests** (most recent first)

## Tech Stack

- **Python + Flask** — backend web framework  
- **OOP** — `Question` and `TestResult` classes with `__init__` and custom methods  
- **Stack (LIFO)** — results stored with `.append()` and viewed in reverse  
- **datetime module** — timestamps every submission  
- **Jinja2** — HTML templating  

## How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/cs-quiz-engine.git
cd cs-quiz-engine
```

### 2. Install Flask
```bash
pip install flask
```

### 3. Run the app
```bash
python app.py
