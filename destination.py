import os

def create_resume_tex(filename="resume.tex"):
  """
  Generates a LaTeX file for a mock resume with clean formatting.
  """

  with open(filename, "w") as f:
    f.write("\\documentclass[11pt,letterpaper]{article}\n")
    f.write("\\usepackage[margin=1in]{geometry}\n")
    f.write("\\usepackage{hyperref}\n")
    f.write("\\usepackage{titlesec}\n")
    f.write("\\usepackage{enumitem}\n")
    f.write("\\usepackage{fontawesome5}\n")
    f.write("\\usepackage{xcolor}\n")
    f.write("\\usepackage{graphicx}\n")
    f.write("\\hypersetup{colorlinks=true, linkcolor=blue, filecolor=magenta, urlcolor=cyan}\n")
    f.write("\\titleformat{\\section}[block]{\Large\\bfseries}{\thesection.}{1em}{}\n")
    f.write("\\titleformat{\\subsection}[block]{\large\\bfseries}{\thesubsection.}{1em}{}\n")
    f.write("\\begin{document}\n")
    f.write("\\begin{center}\n")
    f.write("\\Huge{\\bfseries Your Name}\\\\\n")
    f.write("\\large{\\bfseries Your Address}\\\\\n")
    f.write("\\large{\\bfseries Your Phone Number}\\\\\n")
    f.write("\\large{\\bfseries Your Email}\\\\\n")
    f.write("\\large{\\bfseries Your LinkedIn Profile URL}\\\\\n")
    f.write("\\end{center}\n")
    f.write("\\vspace{1cm}\n")
    f.write("\\section{Summary}\n")
    f.write("A highly motivated and skilled professional with [Number] years of experience in [Your Field]. Proven ability to [Your Skills and Achievements]. Seeking a challenging role where I can contribute my expertise and drive to achieve [Your Goals].\n")
    f.write("\\vspace{1cm}\n")
    f.write("\\section{Experience}\n")
    f.write("\\subsection{Company Name \\hfill [Dates]}\n")
    f.write("\\begin{itemize}[noitemsep,topsep=0pt]\n")
    f.write("\\item {\\bfseries Role Title} \\hfill [Location]\n")
    f.write("\\item [List your responsibilities and accomplishments]\n")
    f.write("\\end{itemize}\n")
    f.write("\\vspace{1cm}\n")
    f.write("\\section{Education}\n")
    f.write("\\subsection{University Name \\hfill [Dates]}\n")
    f.write("{\\bfseries Degree} \\hfill [Major]\n")
    f.write("\\vspace{1cm}\n")
    f.write("\\section{Skills}\n")
    f.write("[List your skills]\n")
    f.write("\\end{document}\n")

def convert_tex_to_docx(tex_filename, docx_filename):
  """
  Converts a LaTeX file to a Word document using Pandoc.
  """

  os.system(f"pandoc {tex_filename} -o {docx_filename}")

if __name__ == "__main__":
  create_resume_tex()
  convert_tex_to_docx("resume.tex", "resume.docx")
  print("Resume created as resume.docx")
