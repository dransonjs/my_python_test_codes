import re

reg = re.compile(r"[C|P]YTHON\d+", re.I)  # re.I表示对大小写不敏感

text = """
    <div>PyTHon1</div>
    <div>PYTHON2</div>
    <div>CyTHon</div>
"""

s = reg.findall(text)  # findall返回一个列表

print("\n".join(s))
