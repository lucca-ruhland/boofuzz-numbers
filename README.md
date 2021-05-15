# boofuzz-numbers
Add boofuzz support for float and integer primitives

# Installation
From source:
```
git clone https://github.com/lucca-ruhland/boofuzz-numbers.git
python3 -m venv venv
source venv/bin/activate
pip3 install boofuzz-numbers
```

# Examples
Float example:
```python
from boofuzz import *
from boofuzz_numbers import s_float


s_initialize('float_test')
if s_block_start('float_value'):
    s_float(value=42.0,          # default value
            s_format='.2f',      # string format, for example %.2f
            f_min=-50.0,         # minimal float value
            f_max=99.9,          # maximal float value
            max_mutations=50,    # Number of how many different float values will be generated
            fuzzable=True,       # if True: will be fuzzed
            name='MyFloatName'   # name of the primitive
            )
s_block_end('float_value')
```
Integer example:
```python
from boofuzz import *
from boofuzz_numbers import s_int


s_initialize('int_test')
if s_block_start('integer_value'):
    s_float(value=30,              # default value
            f_min=10,              # minimal int value
            f_max=40,              # maximal int value
            max_mutations=100,     # Number of how many different float values will be generated
            fuzzable=True,         # if True: will be fuzzed
            name='MyIntName'       # name of the primitive
            )
s_block_end('integer_value')
```
