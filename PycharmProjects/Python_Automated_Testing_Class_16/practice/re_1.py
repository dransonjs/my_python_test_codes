import re

reg = re.compile(r"[C|P]YTHON\d+", re.I)

text = """
    <div>PyTHon1</div>
    <div>PYTHON2</div>
    <div>CyTHon</div>
"""

s = reg.findall(text)

print("\n".join(s))
