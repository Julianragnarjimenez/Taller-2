m=(float(input("ingrese nota de examen matematicas: ")))
f=(float(input("ingrese nota examen fisica: ")))
q=(float(input("ingrese nota examen quimica: ")))
m1=float(input("ingrese nota de la tarea uno matematicas: " ))
m2=float(input("ingrese nota de la tarea dos matematicas: " ))
m3=float(input("ingrese nota de la tarea tres matematicas: " ))
f1=float(input("ingrese nota de la tarea uno Fisica: " ))
f2=float(input("ingrese nota de la tarea dos fisica: " ))
f3=float(input("ingrese nota de la tarea tres fisica: " ))
q1=float(input("ingrese nota de la tarea uno quimica: " ))
q2=float(input("ingrese nota de la tarea dos quimica: " ))
q3=float(input("ingrese nota de la tarea tres quimica: " ))
promediom=((m*0.90)+(((m1+t_m2+m3)/3)*0.10)
promediof=((f*.90)+((f1+f2+f3)/3)*.20)
promedioq=((q*0.85)+(((q1+q2+q3)/3)*0.15)
promedio_final=(promediom+promediof+promedioq)/3

print("promedio matematicas {promediom}, fisica {promediof}, quimica {promedioq},el promedi semestre es:{promedio_final})