import PyPDF2

try:
    pdf_holder = []
    src = input("Enter the path of the pdf: ")
    merger = PyPDF2.PdfMerger()
    while src != "end":
        pdf_holder.append(src)
        src = input("Enter the path of the pdf: ")
    for filename in pdf_holder:
        pdf_file = open(filename, "rb")
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        merger.append(pdf_reader)
    pdf_file.close()

    path = input("Give it a path for new  PDF: ")
    merger.write(path)
except:
    print("Error!")
