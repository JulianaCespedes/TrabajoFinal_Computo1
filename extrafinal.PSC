// Juliana CŽspedes Mosquera C.C. 1.000.305.547

Algoritmo Extra_Final
	
	//Se pide al usuario que ingrese un valor para la velocidad inicial y la posici—n inicial; y se le asigna el valor a la gravedad.
	
	g <- 9.8 
	
	Escribir "Ingrese la velocidad inicial"
	Leer v
	Escribir "Ingrese la posici—n inicial"
	Leer x
	
	//Se pide al usuario el valor del ‡ngulo en un mientras que permite reingresar el valor si no est‡ en el rango.
	
	i <- 0
	
	Mientras i = 0 Hacer
		Escribir "Ingrese el ‡ngulo inicial (en grados) - El angulo debe ser menor de 90 grados"
		Leer a
		Si a > 90 Entonces
			Escribir "Error, ingres— un angulo mayor de 90."
			i <- 0
		SiNo
			i <- 1
		Fin Si
	Fin Mientras
	
	//El valor de los ‡ngulos ingresados en grados, se convierte en radianes.
	
	rad <- (pi * a)/ 180
	
	//Se desarrollan las ecuaciones del movimiento parab—lico.
	
	vx <- v * cos(rad)
	vy <- v * sen(rad)
	
	tvuelo <- (2*v*sen(rad))/g
	xtotal <- x + vx*tvuelo
	
	tsubida <- tvuelo/2
	alturamaxima <- vy*(tsubida) - (g * (tsubida*tsubida) / 2)
	vyfinal <- vy - g*tvuelo
	vxfinal <- vx
	
	vfinal <- raiz((vxfinal*vxfinal) + (vyfinal*vyfinal))
	
	//Se devuelven los resultados necesarios para el an‡lisis.(tiempo de vuelo, velocidad final, distancia recorrida y altura maxima)
	
	Escribir "El tiempo de vuelo es: ", tvuelo
	Escribir "La velocidad final es: ", vfinal
	Escribir "La distancia recorrida por el proyectil es:  ", xtotal
	Escribir "La altura maxima del proyectil es: ", alturamaxima
	
	
FinAlgoritmo