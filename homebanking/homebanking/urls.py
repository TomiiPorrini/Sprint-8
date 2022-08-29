from django.contrib import admin
from django.urls import path, include
from django.urls import path
from Prestamos import views as views_prestamos
from Tarjetas import views as views_tarjetas
from Cuentas import views as views_cuentas
from movimientos import views as views_movimientos
from Login import views as views_login
from django.urls import include
from django.conf import settings
from api import views as api_views

# from Login import views as views_login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_login.login_page, name='login'),
    path('registro/', views_login.register, name='register'),
    path('home/', views_login.home, name='home'),
    path('prestamos/', views_prestamos.prestamos, name='prestamos'),
    path('tarjetas/', views_tarjetas.tarjetas, name='tarjetas'),
    path('cuentas/', views_cuentas.cuentas, name='cuentas'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('movimientos/',views_movimientos.movimientos, name='movimientos'),
    path('api/cliente/info/<int:customer_DNI>/',api_views.InfoCliente.as_view(), name='api_info_cliente'),
    path('api/cliente/cuenta/<int:customer_DNI>/',api_views.SaldoYCuentaCliente.as_view(), name='api_saldoYcuenta_cliente'),
    path('api/cliente/prestamo/<int:customer_DNI>/',api_views.MontoPrestamosCliente.as_view(), name='api_monto_prestamo_cliente'),
    path('api/cliente/tarjeta/<int:customer_DNI>/',api_views.TarjetasCliente.as_view(), name="api_cliente_tarjeta"),
    path('api/cliente/direccion/<int:customer_DNI>/',api_views.DireccionCliente.as_view(), name="api_cliente_modi_Direccion"),
    path('api/cliente/sucursal/<int:branch_id>/',api_views.PrestamosSucursal.as_view(), name="api_prestamos_sucursal"),
    path('api/prestamo/',api_views.SolicitudPrestamo.as_view(), name="api_solicitud_prestamo"),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

