from lifestore_file import lifestore_products,lifestore_sales, lifestore_searches

################       VENTAS 

contador = 0
total_ventas = []

for producto in lifestore_products:
  for venta in lifestore_sales:
    if producto[0] == venta[1]:
      contador +=1

  formato_ideal = [producto[0], producto[1],contador]
  total_ventas.append(formato_ideal)
  contador = 0

#print(total_ventas)

#for total in total_ventas:
  #print('Producto: ', total[1], 'Se vendió: ', total[2])



x = sorted(total_ventas, key=lambda x:x[2])
#menor_ventas = print(x[0:51])
#for i in x:
  #print('Producto: ', i[1], 'Se vendió: ', i[2])

y = sorted(total_ventas, key=lambda x:x[2], reverse=True)
#mayores_ventas = print(y[0:51])
#for i in y:
  #print('Producto: ', i[1], 'Se vendió: ', i[2])




#########################    BUSQUEDAS

contador1 = 0
totales1 = []

for producto in lifestore_products:
  for search in lifestore_searches:
    if producto[0]==search[1]:
      contador1 +=1 

  formato = [producto[0], producto[1], contador1]
  totales1.append(formato)
  contador = 0

#for i in totales1:
  #print('Producto: ',i[1], 'Se buscó: ',i[2])

low_search = sorted(totales1, key=lambda x:x[2])

hight_search = sorted(totales1, key=lambda x:x[2], reverse=True)


############## STOCK

stock = sorted(lifestore_products, key=lambda x:x[4])
#print(stock)

#for i in stock:
  #print('Producto: ' , i[1], 'STOCK: ', i[4])


#######RESEÑAS 

contador = 0
suma_score = 0
productos_promedio = [] 
for producto in lifestore_products:
  for venta in lifestore_sales:
    if producto[0] == venta[1]:
      contador += 1
      suma_score += venta[2]
  promedio = suma_score / contador
  final = [producto[0], producto[1], promedio]
  productos_promedio.append(final)

#print(productos_promedio)

#for i in productos_promedio:
  #print('Producto: ',i[1], 'Score: ',i[2])

peor_ra = sorted(productos_promedio, key=lambda x:x[2])
#worst_rank = print(peor_ra[0:21])


best_ra = sorted(productos_promedio, key=lambda x:x[2], reverse=True)
#best_rank = print(best_ra[0:21])

##########################################INGRESO 


n_ventas = []

for list in total_ventas:
  for number in list:
    final = [list[2]]

  n_ventas.append(final)



result_nventas = []
for sublist in n_ventas:
    for item in sublist:

        result_nventas.append(item)
    


#####


precio = []

for list in lifestore_products:
  for number in list:
    final = [list[2]]

  precio.append(final)



result_precio = []
for sublist1 in precio:
  for item1 in sublist1:

    result_precio.append(item1)



def sumar(lista):
  suma = 0

  for numero in lista:
    suma += numero

  return suma



numero_de_ventas = (sumar(result_nventas))
promedio_de_ventas_mensual = numero_de_ventas/12

ingreso_por_producto = []

for num1, num2 in zip(result_nventas, result_precio):
  ingreso_por_producto.append(num1 * num2)

#print(ingreso_por_producto)

ingreso_total = (sumar(ingreso_por_producto))
ingreso_mensual = (sumar(ingreso_por_producto)/12)

usuario_admin = 'admin'
passw = '123456'

user = input('Ingresar usuario: ')
password = input('Ingresar contraseña: ')

if user == usuario_admin and password == passw:
  print('Tienes acceso total')
  print('Bienvenido a Life Store!')
  print('Elegir opción')
  print('1- Listado de Productos con menos ventas')
  print('2- Listado de Productos con mas busquedas')
  print('3- Listado de Productos con mayores ventas')
  print('4- Listado de Productos con menos ventas')
  print('5- Listado de Productos por stock')
  print('6- Productos mejor rankeados')
  print('7- Productos peor rankeados')
  print('8- Ventas anuales')
  print('9- Promedio de ventas mensuales')
  print('10- Ingreso Total')
  print('11- Ingreso Mensual')
  elección = input('Ingresa opción: ')
  if elección == '1':
    print('Productos con menores ventas: ', x[0:51])
    elección = input('Ingresa opción: ')
  elif elección == '2':
    print(hight_search)
    elección = input('Ingresa opción: ')
  elif elección == '3':
    print('Productos con mayores ventas: ', y[0:51])
    elección = input('Ingresa opción: ')
  elif elección == '4':
    print(low_search)
    elección = input('Ingresa opción: ')
  elif elección == '5':
    print(stock)
    elección = input('Ingresa opción: ')
  elif elección == '6':
    print('Productos mejor rankeados: ', best_ra[0:21])
    elección = input('Ingresa opción: ')
  elif elección == '7':
    print('Productos peor rankeados: ', peor_ra[0:21])
    elección = input('Ingresa opción: ')
  elif elección == '8':
    print('Ventas anuales: ', numero_de_ventas)
    elección = input('Ingresa opción: ')
  elif elección == '9':
    print('Promedio mensual de ventas: ', promedio_de_ventas_mensual)
    elección = input('Ingresa opción: ')
  elif elección == '10':
    print('Ingreso total: ', ingreso_total)
    elección = input('Ingresa opción: ')
  elif elección == '11':
    print('Ingreso mensual promedio: ', ingreso_mensual)
    elección = input('Ingresa opción: ')
  else:
    print('Selección incorrecta')
else:
  print('No tienes usuario registrado')


id_producto = 0

