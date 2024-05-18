from selenium.webdriver.common.by import By
from helpers import Helpers


class UrbanRoutesPage:
    from_field = (By.ID , 'from')
    to_field = (By.ID , 'to')
    call_taxi = (By.XPATH , "(//button[@type='button'])[3]")
    # Selector CSS para hacer click en la tarifa comfort
    card_comfort = (By.CSS_SELECTOR , ".tcard:nth-child(5) > .tcard-title")
    # Selector que permite validar que realmente se selecciono la tarifa comfort
    card_active = (By.CSS_SELECTOR , ".active > .tcard-icon > img")
    # Selector para validar el campo del número de teléfono
    phone_number_button = (By.CSS_SELECTOR , '.np-text')
    phone_number_card = (By.CSS_SELECTOR , ".active .label")
    phone_number_field = (By.ID , "phone")
    next_button = (By.CSS_SELECTOR , ".active .button")
    code_sms = (By.ID , 'code')
    confirm_button = (By.CSS_SELECTOR , ".active .button:nth-child(1)")
    # Selector para validar el campo del número de tarjeta de crédito
    payment_method = (By.CSS_SELECTOR , ".pp-text")
    credit_card = (By.CSS_SELECTOR , ".disabled > .pp-title")
    credit_card_field = (By.CSS_SELECTOR , "#number")
    card_number_field = (By.ID , "number")
    code_field = (By.CSS_SELECTOR , ".card-code-input > #code")
    card_code_field = (By.XPATH , "(//input[@id='code'])[2]")
    out_tab = (By.CSS_SELECTOR , ".unusual > form")
    add_button = (By.CSS_SELECTOR , ".pp-buttons > .button:nth-child(1)")
    close_button = (By.CSS_SELECTOR , ".payment-picker .active > .close-button")
    message_field = (By.CSS_SELECTOR , "div:nth-child(3) > .input-container > .label")
    message = (By.ID , "comment")
    slider = (By.CSS_SELECTOR , ".r:nth-child(1) .slider")
    counter = (By.CSS_SELECTOR , ".r:nth-child(1) .counter-plus")
    # Selector para validar que el contador sea igual a 2
    counter_value = (By. CSS_SELECTOR , ".r:nth-child(1) .counter-value")
    taxi_mode = (By.CSS_SELECTOR , ".smart-button-main")
    # Selector para validar que aparezca el modal para buscar un tax
    taxi_modal = (By.CSS_SELECTOR , ".order-header-title")

    def __init__(self , driver):
        self.driver = driver
        self.helpers = Helpers(self.driver)

    def configure_address(self):
        # Escribir dirección en el campo "Desde"
        self.helpers.send_keys(self.from_field , "East 2nd Street, 601")
        # Escribir dirección en el campo "Hasta"
        self.helpers.send_keys(self.to_field , "1300 1st St")

    def select_comfort_fare(self):
        # Esperar hasta que el botón "Pedir un taxi" esté presente y sea clickeable
        self.helpers.click_element(self.call_taxi)
        # Esperar hasta que la tarifa "Comfort"esté presente y sea clickeable
        self.helpers.click_element(self.card_comfort)
        self.helpers.click_element(self.card_active)

    def add_phone_number(self):
        # Hacer click en el campo "Número de teléfono"
        self.helpers.click_element(self.phone_number_button)
        # Esperar hasta que la ventana emergente "Introduce tu número de teléfono" esté presente y sea clickeable
        self.helpers.click_element(self.phone_number_card)
        # Escribir número de teléfono
        self.helpers.send_keys(self.phone_number_field , "+1 123 123 12 12")
        # Hacer click en el botón "Siguiente"
        self.helpers.click_element(self.next_button)
        # Escribir el código sms
        code_sms = self.helpers.retrieve_phone_code()
        self.driver.find_element(*self.code_sms).send_keys(code_sms)
        # Esperar hasta que el botón "Confirmar" esté presente y sea clickeable
        self.helpers.click_element(self.confirm_button)

    def add_credit_card(self):
        # Hacer click en el campo "Método de pago"
        self.helpers.click_element(self.payment_method)
        # Esperar hasta que la ventana emergente "Método de pago" esté presente y sea clickeable "Agregar tarjeta"
        self.helpers.click_element(self.credit_card)
        # Esperar hasta que la ventana "Agregar tarjeta" esté presente y sea clickeable el campo "Número de tarjeta"
        self.helpers.click_element(self.credit_card_field)
        # Escribir el número de tarjeta
        self.helpers.send_keys(self.card_number_field , "1234 5678 9100")
        # Hacer click en el campo "Código"
        self.helpers.click_element(self.code_field)
        # Escribir el código
        self.helpers.send_keys(self.card_code_field , "111")
        # Simular que el usuario presiona TAB
        self.driver.find_element(*self.out_tab).click()
        # Hacer click en el botón "Agregar"
        self.helpers.click_element(self.add_button)
        # Cerrar la ventana emergente "Método de pago"
        self.helpers.click_element(self.close_button)

    def write_message_to_driver(self):
        # Hacer click en el campo "Mensaje para el conductor"
        self.driver.find_element(*self.message_field).click()
        # Escribir mensaje
        self.helpers.send_keys(self.message , "Muéstrame el camino al museo")

    def request_blanket_and_tissues(self):
        # Seleccionar manta y pañuelos
        self.driver.find_element(*self.slider).click()

    def order_ice_creams(self):
        # Pedir dos helados
        for _ in range(2):
            self.driver.find_element(*self.counter).click()

    def modal_appears_to_search_taxi(self):
        # Hacer click en el botón "Pedir taxi"
        self.helpers.click_element(self.taxi_mode)


