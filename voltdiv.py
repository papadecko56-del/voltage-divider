import numpy as np
import matplotlib.pyplot as plt

# simple voltage divider


try:
     R1 = float(input("resistance in ohms: "))
     R2 = float(input("resistance in ohms: "))
     Vs = float(input("source voltage in volts: "))
    

     
     if R1 <= 0 or R2 <= 0:
       
   
          print("Error  negative or zero resistance choose positive") 
       
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

     

except ValueError:
 print("use numbers as inputs")


