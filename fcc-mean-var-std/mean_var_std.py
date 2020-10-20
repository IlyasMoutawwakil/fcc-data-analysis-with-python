import numpy as np

def calculate(liste):

    if not len(liste)==9:
        raise ValueError("List must contain nine numbers.")
    
    flat = np.array(liste)
    mat = flat.reshape((3,3))
    calculations = dict()

    calculations['mean'] = [list(np.mean(mat, axis=0)), list(np.mean(mat, axis=1)), np.mean(flat)]

    calculations['variance'] = [list(np.var(mat, axis=0)), list(np.var(mat, axis=1)), np.var(flat)]

    calculations['standard deviation'] = [list(np.std(mat, axis=0)), list(np.std(mat, axis=1)), np.std(flat)]

    calculations['max'] = [list(np.max(mat, axis=0)), list(np.max(mat, axis=1)), np.max(flat)]

    calculations['min'] = [list(np.min(mat, axis=0)), list(np.min(mat, axis=1)), np.min(flat)]
    
    calculations['sum'] = [list(np.sum(mat, axis=0)), list(np.sum(mat, axis=1)), np.sum(flat)]

    return calculations
