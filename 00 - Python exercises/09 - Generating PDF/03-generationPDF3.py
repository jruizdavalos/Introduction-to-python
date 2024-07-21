from fpdf import FPDF


class PDF(FPDF):
  def header(self):
    pass
  
  def footer(self):
    pass

  def chapter_title(self):
    pass

  def chapter_body(self, filepath):

    with open(filepath,"rb") as fh:
      txt = fh.read().decode('latin-1')
    self.set_font("Times", size=12)
    self.multi_cell(0,5,txt)
    self.ln()
    self.set_font(style="I")
    self.cell(0, 5, "(End of excernt)")
    pass

  def print_chapter(self, filepath):
    self.chapter_body(filepath)
    pass

pdf = PDF()
txt=open("C:/Users/54112/Desktop/python/pythonProject/00 - Python exercises/09 - Generating PDF/para.txt","r")

pdf.print_chapter("C:/Users/54112/Desktop/python/pythonProject/00 - Python exercises/09 - Generating PDF/para.txt")
#pdf.output("sample4.pdf")
print(txt.read())