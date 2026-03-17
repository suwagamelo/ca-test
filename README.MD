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
git clone https://github.com/suwagamelo/cs-quiz-engine.git
cd cs-quiz-engine
```

### 2. Install Flask
```bash
pip install flask
```

### 3. Run the app
```bash
python app.py
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
```

### 4. Open in your browser
Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

That's it! No database or extra setup needed.

## Project Structure

```
cbt_app/
├── app.py          # Flask routes (home, test, result, history)
├── models.py       # OOP classes: Question, TestResult + question bank
├── templates/
│   ├── base.html   # Shared layout
│   ├── home.html   # Landing page
│   ├── test.html   # Quiz form (all 20 questions)
│   ├── result.html # Timestamped result page
│   └── history.html# All past results
└── README.md
```

## Grading Requirements Met

| Requirement | Implementation |
|---|---|
| OOP (Lecture 4) | `Question` class with `check_answer()`, `TestResult` class with score/grade logic |
| Data Structure (Lecture 5A) | Stack — `results_history.append()` + reversed display |
| Standard API (Lecture 5B) | `datetime.now()` timestamps every submission |
| Flask Web UI | 4 routes: `/`, `/test`, `/result`, `/history` |
| GitHub | 20+ commits, this README |
