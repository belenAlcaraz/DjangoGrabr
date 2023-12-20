
# Django Grabr

## Descripción

Django Grabr es una aplicación inspirada en el concepto de la plataforma Grabr. Permite a los usuarios compradores publicar productos que desean adquirir, ofreciendo una recompensa por su entrega. Los usuarios viajeros pueden realizar ofertas de entrega para ganar la recompensa.

## Características Principales

- Publicación de productos por parte de usuarios compradores.
- Ofertas de entrega realizadas por usuarios viajeros.
- Sistema de recompensas para incentivar la entrega de productos.
- Gestión de ubicaciones para las transacciones.
- Seguimiento del estado de los productos y las ofertas.

## Requisitos Previos

- Python
- Django
- Pillow

## Uso

1. Publica productos.
2. Realiza ofertas de entrega.
3. Gestionar estados de oferta. 

## Tecnologías Utilizadas

- Django
- HTML/CSS
- Bootstrap

## Instalación

1. **Clonar el Repositorio:**

    ```bash
    git clone https://github.com/belenAlcaraz/DjangoGrabr.git
    ```

2. **Instalar las Dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Aplicar Migraciones:**

    ```bash
    python manage.py migrate
    ```

4. **Crear un Superusuario:**

    ```bash
    python manage.py createsuperuser
    ```

    Sigue las instrucciones para crear una cuenta de superusuario, que te permitirá acceder al panel de administración.

5. **Iniciar el Servidor de Desarrollo:**

    ```bash
    python manage.py runserver
    ```


## Conclusión

¡Listo! Django Grabr está instalado y en funcionamiento. Explora la aplicación en [http://localhost:8000/](http://localhost:8000/) y accede al panel de administración en [http://localhost:8000/admin/](http://localhost:8000/admin/) con las credenciales del superusuario.


