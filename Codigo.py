from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

# URL da aplicação
URL = "http://www.vanilton.net/triangulo/"

# Configuração do WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Substitua por Edge() ou Firefox() conforme necessário
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# Função genérica para preencher o formulário e obter o resultado
def verificar_triangulo(driver, lado1, lado2, lado3):
    driver.get(URL)

    # Preencher os campos de entrada
    driver.find_element(By.NAME, "lado1").send_keys(str(lado1))
    driver.find_element(By.NAME, "lado2").send_keys(str(lado2))
    driver.find_element(By.NAME, "lado3").send_keys(str(lado3))
    
    # Submeter o formulário
    driver.find_element(By.XPATH, "//button[text()='Verificar']").click()

    # Capturar e retornar a mensagem do resultado
    return driver.find_element(By.ID, "resultado").text

# Testes
def test_triangulo_equilatero(driver):
    resultado = verificar_triangulo(driver, 5, 5, 5)
    assert resultado == "Equilátero"

def test_triangulo_isosceles(driver):
    resultado = verificar_triangulo(driver, 5, 5, 8)
    assert resultado == "Isósceles"

def test_triangulo_escaleno(driver):
    resultado = verificar_triangulo(driver, 6, 8, 10)
    assert resultado == "Escaleno"

def test_nao_forma_triangulo(driver):
    resultado = verificar_triangulo(driver, 1, 2, 3)
    assert resultado == "Os valores fornecidos não formam um triângulo."

def test_valores_invalidos(driver):
    resultado = verificar_triangulo(driver, -1, 0, 2)
    assert resultado == "Os valores fornecidos não são válidos."
