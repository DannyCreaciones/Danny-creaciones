from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.environ.get('DANNY_SECRET_KEY', 'cambiar-esta-clave-antes-de-publicar-2026')

WHATSAPP = '5493885010178'
INSTAGRAM_URL = 'https://www.instagram.com/danny_creaciones1/'
# Confirmá la dirección exacta de la página de Facebook antes de publicar.
FACEBOOK_URL = 'https://www.facebook.com/danny_creaciones1'

# Productos de muestra: editá nombres, precios, descripciones e imágenes en esta lista.
# Los precios son ilustrativos; reemplazalos por los precios reales antes de vender.
PRODUCTS = [
    {'id': 1, 'name': 'Riñonera de Cuero', 'category': 'Regalos', 'price': 38000, 'description': 'Una presentación especial para sorprender.', 'image': '/static/img/cartera-negra.jpeg', 'tag': 'DESTACADO'},
    {'id': 2, 'name': 'Accesorio dorado', 'category': 'Accesorios', 'price': 30000, 'description': 'Un detalle delicado para completar tu estilo.', 'image': 'https://images.unsplash.com/photo-1611652022419-a9419f74343d?auto=format&fit=crop&w=900&q=85', 'tag': 'ELEGIDO'},
    {'id': 3, 'name': 'Caja sorpresa', 'category': 'Regalos', 'price': 22000, 'description': 'Una caja preparada con detalles para regalar.', 'image': 'https://images.unsplash.com/photo-1607344645866-009c320b63e0?auto=format&fit=crop&w=900&q=85', 'tag': 'ESPECIAL'},
    {'id': 4, 'name': 'Bolso urbano', 'category': 'Accesorios', 'price': 27900, 'description': 'Práctico, versátil y fácil de combinar.', 'image': 'https://images.unsplash.com/photo-1584917865442-de89df76afd3?auto=format&fit=crop&w=900&q=85', 'tag': 'NOVEDAD'},
    {'id': 5, 'name': 'Vela decorativa', 'category': 'Hogar', 'price': 8900, 'description': 'Un toque cálido para tus espacios.', 'image': 'https://images.unsplash.com/photo-1603006905003-be475563bc59?auto=format&fit=crop&w=900&q=85', 'tag': 'DETALLE'},
    {'id': 6, 'name': 'Set de cuidado personal', 'category': 'Regalos', 'price': 16400, 'description': 'Una opción bonita para un regalo especial.', 'image': 'https://images.unsplash.com/photo-1608571423902-eed4a5ad8108?auto=format&fit=crop&w=900&q=85', 'tag': 'FAVORITO'},
    {'id': 7, 'name': 'Taza de diseño', 'category': 'Hogar', 'price': 7500, 'description': 'Un detalle simple que acompaña cada día.', 'image': 'https://images.unsplash.com/photo-1514228742587-6b1558fcca3d?auto=format&fit=crop&w=900&q=85', 'tag': 'CLÁSICO'},
    {'id': 8, 'name': 'Accesorio de moda', 'category': 'Accesorios', 'price': 11200, 'description': 'Un complemento con personalidad.', 'image': 'https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?auto=format&fit=crop&w=900&q=85', 'tag': 'TENDENCIA'},
]

@app.context_processor
def global_vars():
    return {'whatsapp': WHATSAPP, 'instagram_url': INSTAGRAM_URL, 'facebook_url': FACEBOOK_URL, 'year': datetime.now().year}

@app.get('/')
def home():
    categories = sorted({p['category'] for p in PRODUCTS})
    return render_template('index.html', products=PRODUCTS, categories=categories)

@app.get('/legal/<page>')
def legal(page):
    pages = {
      'privacidad': ('Política de privacidad', [
        ('Datos que podemos recibir', 'Cuando nos contactás o realizás un pedido, podés compartir tu nombre, teléfono, dirección de entrega y datos necesarios para coordinar la compra.'),
        ('Uso de la información', 'Usamos esos datos únicamente para responder consultas, gestionar pedidos, coordinar entregas y brindar atención posventa.'),
        ('Pagos', 'No ingreses números de tarjeta ni claves bancarias por WhatsApp. Los pagos deben realizarse únicamente por medios acordados y seguros.'),
        ('Conservación y seguridad', 'Limitamos el uso de los datos a lo necesario para la operación. Ningún sistema conectado a internet puede garantizar seguridad absoluta.'),
        ('Tus derechos', 'Podés solicitar acceso, actualización o eliminación de tus datos escribiéndonos por WhatsApp.'),
        ('Cambios', 'Esta política puede actualizarse para reflejar cambios en el funcionamiento de la tienda. Revisá esta página antes de comprar.')]),
      'terminos': ('Términos y condiciones', [
        ('Información de productos', 'Las fotografías son ilustrativas y pueden existir pequeñas diferencias de color, presentación o disponibilidad.'),
        ('Precios y disponibilidad', 'Los precios de demostración deben reemplazarse por los valores reales. La compra se confirma cuando Danny Creaciones valida disponibilidad, precio final y forma de entrega.'),
        ('Pedidos', 'Enviar un pedido por WhatsApp no constituye una confirmación automática de stock ni de pago. Esperá la confirmación del negocio.'),
        ('Uso del sitio', 'No se permite utilizar el sitio para actividades ilícitas, intentar vulnerar su seguridad ni enviar información falsa.'),
        ('Contacto', 'Para consultas sobre estos términos, contactanos por WhatsApp.')]),
      'envios': ('Envíos y entregas', [
        ('Modalidades', 'La modalidad de envío o retiro se acuerda al confirmar cada pedido.'),
        ('Costos y plazos', 'El costo, la zona de cobertura y el tiempo estimado se informan antes de cerrar la compra. No se consideran confirmados hasta que el negocio los comunique.'),
        ('Datos de entrega', 'Revisá que el nombre, teléfono y dirección sean correctos al coordinar la entrega.'),
        ('Demoras', 'Si surge una demora, nos comunicaremos para coordinar una alternativa.')]),
      'pagos': ('Medios de pago', [
        ('Medios disponibles', 'Consultá por WhatsApp qué medios están habilitados para tu pedido. La disponibilidad puede variar.'),
        ('Mercado Pago', 'El sitio todavía no procesa pagos automáticamente. No se debe interpretar esta web como una integración activa con Mercado Pago.'),
        ('Confirmación', 'El pedido queda confirmado cuando Danny Creaciones valida el pago o acuerda expresamente otra modalidad.')]),
      'cambios': ('Cambios y devoluciones', [
        ('Antes de comprar', 'Consultá medidas, materiales, colores, personalización y disponibilidad antes de confirmar.'),
        ('Solicitudes', 'Si el producto llega dañado o recibís algo distinto de lo acordado, contactanos cuanto antes con el número de pedido y fotos.'),
        ('Evaluación', 'Cada caso se revisará conforme a la normativa argentina de defensa del consumidor aplicable. Esta información no limita derechos legales.'),
        ('Productos personalizados', 'Si el producto es personalizado, consultá previamente las condiciones específicas de cambios y devoluciones.')]),
      'faq': ('Preguntas frecuentes', [
        ('¿Cómo compro?', 'Elegí los productos, agregalos al carrito y tocá el botón para enviar el pedido por WhatsApp. Te confirmaremos disponibilidad y total.'),
        ('¿Los precios son definitivos?', 'Los productos de muestra tienen precios ilustrativos. Confirmá el precio vigente antes de pagar.'),
        ('¿Hacen envíos?', 'Consultá las opciones y costos de entrega por WhatsApp.'),
        ('¿Puedo pagar online?', 'El pago online automático no está activado en esta versión. Los medios se coordinan con el negocio.'),
        ('¿Cómo consulto por un producto?', 'Podés escribirnos desde el botón de WhatsApp de la tienda.')])
    }
    if page not in pages:
        return redirect(url_for('home'))
    title, sections = pages[page]
    return render_template('legal.html', title=title, sections=sections)

@app.get('/api/products')
def api_products():
    return jsonify(PRODUCTS)

if __name__ == '__main__':
    app.run(debug=True)
