from pdfrw import PdfReader
x = PdfReader('source.pdf')
x.keys()
['/Info', '/Size', '/Root']
x.Info
{'/Producer': '(cairo 1.8.6 (http://cairographics.org))',
 '/Creator': '(cairo 1.8.6 (http://cairographics.org))'}
x.Root.keys()
['/Type', '/Pages']