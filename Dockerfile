# שלב 1 — בסיס: פייתון רשמי
FROM python:3.11-slim

# שלב 2 — הגדרת תיקיית עבודה בתוך הקונטיינר
WORKDIR /app

# שלב 3 — העתקת קבצי requirements
COPY requirements.txt .

# שלב 4 — התקנת התלויות
RUN pip install --no-cache-dir -r requirements.txt

# שלב 5 — העתקת כל הפרויקט לתוך הקונטיינר
COPY . .

# שלב 6 — פתיחת פורט 8000 (לא חובה אבל מומלץ)
EXPOSE 8000

# שלב 7 — הפעלת השרת
CMD ["uvicorn", "src.server:app", "--host", "0.0.0.0", "--port", "8000"]