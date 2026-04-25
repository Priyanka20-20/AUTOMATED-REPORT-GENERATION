from fpdf import FPDF

with open("Students.txt", "r") as file:
    lines = file.readlines()

students = []
student = {}

for line in lines:
    line = line.strip()

    if line == "":
        if student:
            students.append(student)
            student = {}
    else:
        if ":" in line:
            key, value = line.split(":", 1)
            student[key.strip()] = value.strip()

if student:
    students.append(student)

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=10)

for stu in students:
    pdf.add_page()

    pdf.set_font("Arial", "B", 18)
    pdf.cell(200, 10, "DALMIA COLLEGE", ln=True, align='C')

    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 20, "STUDENT REPORT CARD", ln=True, align='C')

    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, f"Name: {stu.get('Name','')}", ln=True)

    pdf.ln(5)

    pdf.set_x(30)

    col_width = 80
    mark_width = 40

    pdf.set_fill_color(200, 220, 255)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(col_width, 10, "Subject", border=1, align='C', fill=True)
    pdf.cell(mark_width, 10, "Marks", border=1, align='C', fill=True, ln=True)

    pdf.set_font("Arial", size=12)

    marks = []

    for subject in stu:
        if subject != "Name":
            mark = int(stu[subject])
            marks.append(mark)

            pdf.set_x(30)
            pdf.cell(col_width, 10, subject, border=1, align='C')
            pdf.cell(mark_width, 10, str(mark), border=1, align='C', ln=True)

    total = sum(marks) if marks else 0
    average = total / len(marks) if marks else 0
    percentage = (total / (len(marks) * 100)) * 100 if marks else 0

    pdf.ln(5)

    pdf.cell(200, 10, f"Total: {total}", ln=True)
    pdf.cell(200, 10, f"Average: {average:.2f}", ln=True)
    pdf.cell(200, 10, f"Percentage: {percentage:.2f}%", ln=True)

    if percentage >= 90:
        grade = "A+"
        remark = "Excellent"
    elif percentage >= 75:
        grade = "A"
        remark = "Very Good"
    elif percentage >= 60:
        grade = "B"
        remark = "Good"
    else:
        grade = "C"
        remark = "Needs Improvement"

    pdf.cell(200, 10, f"Grade: {grade}", ln=True)
    pdf.cell(200, 10, f"Remarks: {remark}", ln=True)

    pdf.ln(10)

    pdf.cell(100, 30, "Teacher Signature______________", ln=False)
    pdf.cell(100, 30, "Principal Signature______________", ln=True)

pdf.cell(200, 70, txt= "--- End of Report ---", ln=True, align='C')


pdf.output("final_report_card.pdf")

print("Final Report Card created successfully!")
