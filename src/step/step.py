import numpy

def step_function(x: numpy.ndarray) -> numpy.ndarray:
    """
    ステップ関数の実装

    Parameters
    -----
    x : numpy.ndarray
        numpyで生成された配列
    
    Returns
    -----
    y : numpy.ndarray
        データ項ごとにステップ関数の条件を満たしているかBooleanの判定を行う
    """
    y = x > 0
    return y.astype(numpy.int)