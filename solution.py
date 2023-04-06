import pandas as pd
import numpy as np


chat_id = 664256606

def solution(x: np.array) -> float:
    return ((x+32)/10).mean()
