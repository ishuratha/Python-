str='a123'
#str='123'
try:
i=float(str)
except=(ValueError,TyprError):
print('\nnot numeric')
print()
