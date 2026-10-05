import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager    
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")  #instancia
def driver():
    Service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=Service)
    yield driver
    driver.quit()  


def test_001_login(driver):
    driver.get("https://www.saucedemo.com/")
    driver. find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "/inventory.html" in driver.current_url , "EROR: No se redirecciono a /inventory.html"

def test_002_verificar_titulo(driver):
    page_title = driver.title
    section_title = driver.find_element(By.CLASS_NAME, "title").text
   
    assert page_title == "Swag Labs", f"ERROR: El titulo de la pagina es incorrecto. Se esperaba 'Swag Labs' pero se obtuvo '{page_title}'"

    assert section_title == "Products", f"ERROR: El titulo de la seccion es incorrecto. Se esperaba 'Products' pero se obtuvo '{section_title}'"


def test_003_productos_visibles(driver):
    inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")

    assert len(inventory_items) > 0, "ERROR: No se encontraron productos visibles"

def test_004_validar_interfaz(driver):
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")

    assert menu_button.is_displayed(), "ERROR: El boton de menu no es visible"
    assert filtro.is_displayed(), "ERROR: El filtro de productos no es visible"


def test_005_añadir_producto_al_carrito(driver):
    first_item = driver.find_element(By.CLASS_NAME, "inventory_item")[0]

    boton_agregar = first_item.find_element(By.TAG_NAME, "button")
    boton_agregar.click()         

    assert boton_agregar.text.capitalize() == "Remove", "ERROR: El boton no cambio a 'Remove' despues de agregar el producto al carrito"     


def test_006_verifica_contador_carrito(driver):
    contador_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

    assert contador_carrito == "1", f"ERROR: El contador del carrito es incorrecto. Se esperaba '1' pero se obtuvo '{contador_carrito}'"


def test_007_navegar_carrito(driver):
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    assert "/cart.html" in driver.current_url, "ERROR: No se redirecciono a /cart.html"


def test_008_verificar_producto_en_carrito(driver):
    producto_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    assert producto_en_carrito == "Sauce Labs Backpack", f"ERROR: El producto en el carrito es incorrecto. Se esperaba 'Sauce Labs Backpack' pero se obtuvo '{producto_en_carrito}'"