from boofuzz import *
import random 


class Float(BasePrimitive):
    def __init__(self, name=None, default_value:float=0.0, s_format:str='.1f', f_min:float=0.0, f_max:float=100.0, max_mutations:int=1000, seed=None, *args, **kwargs):
        super(Float, self).__init__(name=name, default_value=str(default_value), *args, **kwargs)
        
        self.s_format = s_format
        self.f_min = f_min
        self.f_max = f_max
        self.max_mutations = max_mutations
        self.seed = seed
    
    def mutations(self, default_value: float): 
        last_val = None
        if self.seed is not None:
            random.seed(self.seed)

        for i in range(self.max_mutations):
            if i == 0:
                current_val = default_value
            else:
                current_val = random.uniform(self.f_min, self.f_max)

            current_val = f'%{self.s_format}' % float(current_val)

            if last_val == current_val:
                continue
            last_val = current_val
            yield current_val 

    def encode(self, value, mutation_context=None):
        return value.encode()

    def num_mutations(self, default_value):
        return self.max_mutations


def s_float(value=0.0, s_format=".1f", f_min:float=0.0, f_max:float=100.0, max_mutations:int=1000, fuzzable=True, name=None): 
    blocks.CURRENT.push(
        Float(
            name=name,
            default_value=value,
            s_format=s_format,
            f_min=f_min,
            f_max=f_max,
            max_mutations=max_mutations,
            fuzzable=fuzzable,
        )
    )
