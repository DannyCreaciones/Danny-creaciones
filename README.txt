DANNY CREACIONES PRO — TIENDA FLASK
===================================

IMPORTANTE: este proyecto es una versión nueva e independiente. NO borres tu proyecto actual hasta probar este.

REQUISITOS
- Windows 10/11
- Python 3.10 o posterior
- Conexión a internet para cargar Google Fonts y fotografías remotas

INSTALACIÓN
1. Extraé el ZIP en una carpeta, por ejemplo: Documentos\DannyCreacionesPro.
2. Abrí esa carpeta en el Explorador de archivos.
3. En la barra de dirección del Explorador escribí cmd y presioná Enter.
4. En la terminal ejecutá:
   python -m venv .venv
   .venv\Scripts\activate
   python -m pip install -r requirements.txt
   python app.py
5. Abrí en el navegador: http://127.0.0.1:5000
6. Para detener el servidor, volvé a la terminal y presioná Ctrl+C.

DISEÑO Y SECCIONES
- Inicio, catálogo de productos con filtros, carrito, contacto y pie de página completo.
- Páginas de preguntas frecuentes, envíos, medios de pago, cambios/devoluciones, privacidad y términos.
- Botón flotante de WhatsApp y armado del pedido con productos, cantidades y total estimado.
- Estética negro y dorado, tipografías Bodoni Moda y Montserrat, estilo editorial francés elegante.

ANTES DE PUBLICAR
1. En app.py editá PRODUCTS para poner tus productos, precios reales, descripciones y fotos.
2. Los productos y precios incluidos son DEMOSTRATIVOS; no vender con ellos sin revisarlos.
3. El logo todavía es tipográfico. Cuando tengas tu logo, agregalo en static/img y podemos integrarlo.
4. Verificá que Facebook URL sea la dirección exacta de tu página.
5. Ajustá las políticas a tus condiciones reales y a la legislación aplicable.
6. El carrito envía el pedido por WhatsApp. El pago automático con Mercado Pago NO está integrado. Para habilitarlo hay que configurar credenciales oficiales de Mercado Pago en el servidor; nunca pongas claves privadas en HTML o JavaScript.
7. Flask debug está habilitado solo para desarrollo local. Antes de publicar, desactivá debug y usá un servidor de producción.
8. Para publicar en internet necesitás hosting compatible con Python/Flask y configurar dominio, HTTPS y variables de entorno.

DATOS YA CONFIGURADOS
WhatsApp: +54 9 388 501 0178
Instagram: @danny_creaciones1
Facebook: facebook.com/danny_creaciones1 (verificar URL)

CAMBIAR EL CATÁLOGO
Abrí app.py con Bloc de notas o Visual Studio Code. Buscá PRODUCTS. Cada producto tiene id, name, category, price, description, image y tag.
Para cambiar una foto, reemplazá la URL del campo image por una URL pública o por una ruta de archivo dentro de static/img, por ejemplo /static/img/producto-1.jpg.

AVISO
Las políticas incluidas son textos base informativos, no asesoramiento jurídico. Los precios y productos son ejemplos. El sitio es una base funcional para desarrollo; no es aún una tienda publicada en internet.
