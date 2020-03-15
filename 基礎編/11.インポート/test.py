import testmod
 
test_class_1 = testmod.TestClass()
test_class_1.test_method('1')
 
 
from testmod import TestClass
 
test_class_2 = TestClass()
test_class_2.test_method('2')

#別名インポート – as
from datetime import datetime
datetime.today()
 
from datetime import datetime as d
d.today()