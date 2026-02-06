import pandas as pd
import numpy as np

exam_data = {
    "name:": ["James", "Muhammad", "Rayaan", "Alissa", "Dana", "Micheal", "Zohran"],
    "score:": [85.0, 45.0, 86.0, 21.0, 67.0, 78.0, 92.0],
    "Attempts:": [3, 2, 3, 1, 2, 3, 1],
    "Qualify:": ["yes", "no", "yes", "no", "yes", "yes", "yes"]

}

labrls = ["a", "b", "c", "d", "e", "f", "g"]
df = pd.DataFrame(exam_data, index=labrls)
print("Original DataFrame:")
print(df.info())
print(df[df["Attempts:"]>2])
print(df["Attempts:"])