Automatización de Pruebas E2E - SauceDemo

Propósito del Proyecto

Este proyecto tiene como propósito principal automatizar las pruebas de extremo a extremo (E2E) para la aplicación web de comercio electrónico de prueba SauceDemo. A través de una suite de pruebas estructurada, se validan flujos críticos del sistema como el inicio de sesión de usuarios, la visibilidad y validación del catálogo de productos, la interacción con el carrito de compras y la correcta navegación entre las distintas secciones de la plataforma.

Tecnologías Utilizadas

Python: Lenguaje de programación principal en el que está desarrollada la suite de pruebas.

Selenium WebDriver: Herramienta de automatización web para interactuar de forma simulada con el navegador Google Chrome.

Pytest: Framework de pruebas en Python que facilita la estructuración limpia de los tests mediante funciones y fixtures.

WebDriver Manager: Librería para la gestión automática de los drivers del navegador (ChromeDriver).

Pytest-HTML: Extensión de pytest para la generación de reportes detallados en formato HTML.

Cómo Instalar las Dependencias

Asegúrate de tener Python instalado en tu equipo. Luego, abre una terminal en la carpeta raíz del proyecto e instala las dependencias ejecutando los siguientes comandos:

python -m pip install pytest
python -m pip install selenium
python -m pip install webdriver-manager
python -m pip install pytest-html


Cómo Ejecutar las Pruebas

Puedes correr la suite completa de pruebas utilizando la terminal de tu preferencia (PowerShell o CMD) desde la raíz del proyecto:

Ejecución básica en la terminal:

pytest -v


Ejecución generando un reporte HTML:

Para correr las pruebas y generar un informe detallado guardado en la carpeta reports:

pytest -v --html=reports/reporte.html
