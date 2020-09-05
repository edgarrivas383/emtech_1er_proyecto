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
  else:
    print('Selección incorrecta')
else:
  print('No tienes usuario registrado')


id_producto = 0

