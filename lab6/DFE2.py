import os
p = "example.txt" 
print(os.access(p, os.F_OK))
print(os.access(p, os.R_OK))
print(os.access(p, os.W_OK))
print(os.access(p, os.X_OK))
