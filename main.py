import PyPDF2
file1 = input("Enter the first file name: ")
file2 = input("Enter the second file name: ")
pdfiles = [file1, file2]
merger = PyPDF2.PdfMerger()

for filename in pdfiles:
    pdfile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfile)
    merger.append(pdfReader)
pdfile.close()
merger.write("merged.pdf")