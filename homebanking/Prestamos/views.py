from django.shortcuts import render
from .forms import createPrestamo
from .models import Prestamo
import sqlite3
from django.shortcuts import render

def prestamos(request): 
    loan_form = createPrestamo
    verificacion = False

    if request.method == "POST":
        #Traemos los datos enviados
        loan_form = loan_form(data=request.POST)
        #Chequeamos que los datos son validos, de ser asi, los asignamos a una variable
        if loan_form.is_valid():
            name = request.POST.get('name','')
            last_name = request.POST.get('last_name','')
            dni = request.POST.get('dni','')
            start_date = request.POST.get('start_date','')
            valor = int(request.POST.get('valor',''))
            loan_type = request.POST.get('loan_type','')
            loan_status = request.POST.get('loan_status','')
            
            sqliteconnection = sqlite3.connect('ITBANK.db')
            
            cursor = sqliteconnection.cursor()
            cursor.execute('SELECT customer_id FROM cliente WHERE customer_DNI = ' + dni)
            customer_id = cursor.fetchall()
            customer_id = str(customer_id[0][0])
            cursor.execute('SELECT type_account_id FROM cuenta WHERE customer_id = ' + customer_id)
            type_account_id = cursor.fetchall()
            type_account_id = str(type_account_id[0][0])
            
            if type_account_id == '1':
                if valor <= 100000:
                    verificacion = True
            elif type_account_id == '2':
                if valor <= 300000:
                    verificacion = True
            elif type_account_id == '3':
                if valor <= 500000:
                    verificacion = True
            
            if verificacion:
                prestamo = Prestamo(name = name, last_name= last_name ,dni = dni, start_date= start_date, valor = valor, loan_type=loan_type,loan_status= loan_status)
                prestamo.save()
            
            return render(request,'prestamos/prestamos.html',{'nombre': name, 'apellido': last_name, 'verif':verificacion})

    return render(request,'prestamos/prestamos.html',{'form': loan_form})