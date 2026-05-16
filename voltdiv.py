import numpy as np
import matplotlib.pyplot as plt

# simple voltage divider
R1 = float(input("resistance in ohms: "))
R2 = float(input("resistance in ohms: "))
Vs = float(input("source voltage in volts: "))



try:
   R2 / (R1 + R2)
 
   if R1 < 0 or R2 < 0:
       
   
        print("Error  negative resistance choose positive") 
     


   else:
        V_out = Vs * (R2 / (R1 + R2))
        print(f"Output voltage:{V_out} V")

        labels = ['R1 drop', 'R2 drop(Vout)']
        values = [Vs - V_out, V_out]
        plt.bar(labels, values, color=['#3b82f6', '#00e5ff'])
        plt.title('Voltage Divider')
        plt.xlabel('Values')
        plt.ylabel('Voltage (V)')
        plt.show()
except ZeroDivisionError: 
    print("zero division use positives")
