# **Exercițiul 5 — Provocare**
# Scrie în `misc.py` un program care:
# 1. Creează un dicționar cu 3 studenți — cheia = nume, valoarea = listă de 3 notea
# 2. Calculează și afișează media fiecărui student
# 3. Afișează studentul cu cea mai mare medie
# 4. Folosind un set, afișează câte note distincte există în total
# 5. Stochează datele fiecărui student ca tuple `(medie, status)` unde status = `"Promovat"` dacă media >= 5

students = {
    "Bogdan": [10, 8, 10],
    "Sofia":  [10, 10, 10],
    "Milena": [9, 10, 10],
}

# Cerinta 2 — media fiecărui student
condensedStudents = {}
for key, notes in students.items():
    average = sum(notes) / len(notes)
    print(f"Media studentului {key} este: {average:.2f}")
    condensedStudents[key] = average

# Cerinta 3 — studentul cu cea mai mare medie
top_student = max(condensedStudents, key=condensedStudents.get)
print(f"Studentul cu cea mai mare medie: {top_student} — {condensedStudents[top_student]:.2f}")

# Cerinta 4 — note distincte cu set
grades = set()
for key, notes in students.items():
    grades.update(notes)
print(f"Totalitatea notelor distincte este: {len(grades)}")

# Cerinta 5 — tuple (medie, status) per student
for key, value in condensedStudents.items():
    status = "Promovat" if value >= 5 else "Picat"
    stud = (value, status)
    print(f"{key}: {stud}")