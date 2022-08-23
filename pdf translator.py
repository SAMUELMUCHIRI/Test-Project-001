from pdfrw import PdfReader
x = PdfReader('example.pdf')
print(x.info)