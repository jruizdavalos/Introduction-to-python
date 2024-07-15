from fpdf import FPDF

class PDF(FPDF):
  def header(self):
    self.image("00 - Python exercises/09 - Generating PDF/logo.png", 10,8,33)


pdf= PDF()

pdf.add_page()
pdf.set_font("helvetica","B",16)

pdf.cell(40,10,"Hello world")

pdf.output("00 - Python exercises/09 - Generating PDF/sample2.pdf")