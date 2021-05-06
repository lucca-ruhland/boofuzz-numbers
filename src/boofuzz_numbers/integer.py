from boofuzz import *
import random


class Int(BasePrimitive):
    def __init__(self, name=None, default_value:int=0, s_format:str='i', i_min:int=0, i_max:int=100, max_mutations:int=1000, seed=None, *args, **kwargs):
        super(Int, self).__init__(name=name, default_value=str(default_value), *args, **kwargs)

        self.s_format = s_format
        self.i_min = i_min
        self.i_max = i_max
        self.max_mutations = max_mutations
        self.seed = seed

    def mutations(self, default_value: int):
        last_val = None
        if self.seed is not None:
            random.seed(self.seed)

        for i in range(self.max_mutations):
            if i == 0:
                current_val = default_value
            else:
                current_val = random.randint(self.i_min, self.i_max)

            current_val = f'%{self.s_format}' % int(current_val)

            if last_val == current_val:
                continue
            last_val = current_val
            yield current_val

    def encode(self, value, mutation_context=None):
        return value.encode()

    def num_mutations(self, default_value):
        return self.max_mutations


def s_int(value=0, s_format="i", i_min:int=0, i_max:int=100, max_mutations:int=1000, fuzzable=True, name=None):
    blocks.CURRENT.push(
        Float(
            name=name,
            default_value=value,
            s_format=s_format,
            i_min=i_min,
            i_max=i_max,
            max_mutations=max_mutations,
            fuzzable=fuzzable,
        )
    )
