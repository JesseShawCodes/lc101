from test import testEqual

def remove(substr,original_string):
    return "Testing"
    # your code here

testEqual(remove('an', 'banana'), 'bana')
testEqual(remove('cyc', 'bicycle'), 'bile')
testEqual(remove('iss', 'Mississippi'), 'Missippi')
testEqual(remove('egg', 'bicycle'), 'bicycle')
testEqual(remove('oo', 'Yahoohoo'), 'Yahhoo')
