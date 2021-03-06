import numpy as np
import matplotlib.pyplot as plt
from step.step import step_function
from os import path, makedirs

# plt.rcParams['font.family'] = "Noto Sans CJK JP"
plt.rcParams['font.family'] = "IPAexGothic"

if not path.exists("img"):
    makedirs("img")

# class speaker:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print(f"My name is {self.name}, I'm {self.age}")


# trump = speaker(name = "hoge", age = 49)
# trump.speak()

x = np.arange(-3, 3, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="dashed", label="cos")

plt.xlabel("横軸")
plt.ylabel("縦軸")

plt.title("sin & cos")
plt.legend()

plt.savefig( path.abspath('img/plots.png') )



y = step_function(x)
print(y)