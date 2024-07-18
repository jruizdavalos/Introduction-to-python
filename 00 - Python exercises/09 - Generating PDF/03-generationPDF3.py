from fpdf import FPDF


class PDF():
  def header(self):
    pass
  
  def footer(self):
    pass

  def chapter_title(self):
    pass

  def chapter_body(self, filepath):
    with open(filepath,"rb") as fh:
      txt = fh.read().decode('latin-1')

    print(txt)
    pass

  def print_chapter(self, filepath):
    self.chapter_body(filepath)
    pass

pdf = PDF()

pdf.print_chapter("paragraph.txt")