from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()

pdf.add_page()
pdf.set_font('times', style='I', size=35)
pdf.set_fill_color(212,237,218)
pdf.set_text_color(100,40,10)
pdf.cell(0, 40, 'CS50 Shirtificate', align='C', border=1, fill=True)

pdf.image('shirtificate.png', x=0, y=80)

pdf.set_y(150)
pdf.set_font('Courier', style = 'B', size=40)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 10, f'{name} took CS50', align='C')

pdf.output('shirtificate.pdf')
