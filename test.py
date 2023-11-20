from glantix_vendor import Glantix
from Kenya_computer_vendor import Kenyacomputer

v = Glantix()
k = v.item('desktop', name='dell')
print(k)
print("*" * 10)
print()
r = Kenyacomputer()
#m = r.item('desktop', name='idea')
#print(m)

#print(v.all())
