from selenium import webdriver
import data
import main
import helpers


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = main.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.configure_address()
        assert routes_page.helpers.get_element(routes_page.from_field) == address_from
        assert routes_page.helpers.get_element(routes_page.to_field) == address_to

    def test_select_comfort_fare(self):
        routes_page = main.UrbanRoutesPage(self.driver)
        routes_page.select_comfort_fare()
        # Validación para seleccionar la tarifa comfort por el atributo "active" en la clase
        assert routes_page.helpers.is_element_active(routes_page.card_active)

    def test_add_phone_number(self):
        routes_page = main.UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        routes_page.add_phone_number()
        # Validación del campo "Número de teléfono" con la clase np-text
        assert routes_page.helpers.get_text(routes_page.phone_number_button) == phone_number
        assert routes_page.helpers.get_element(routes_page.code_sms)

    def test_add_credit_card(self):
        routes_page = main.UrbanRoutesPage(self.driver)
        card_code = data.card_code
        routes_page.add_credit_card()
        # Validación del campo "Número de tarjeta" con la clase pp-text
        assert routes_page.helpers.is_element_present(routes_page.payment_method)
        assert routes_page.helpers.get_element(routes_page.card_code_field) == card_code

    def test_write_message_to_driver(self):
        routes_page = main.UrbanRoutesPage(self.driver)
        message_for_driver = data.message_for_driver
        routes_page.write_message_to_driver()
        assert routes_page.helpers.get_element(routes_page.message) == message_for_driver

    def test_request_blanket_and_tissues(self):
        routes_page = main.UrbanRoutesPage(self.driver)
        routes_page.request_blanket_and_tissues()
        assert routes_page.helpers.is_element_displayed(routes_page.slider)

    def test_order_ice_creams(self):
        routes_page = main.UrbanRoutesPage(self.driver)
        routes_page.order_ice_creams()
        # Validación del campo contador sea igual a 2 al pedir los helados
        ice_creams_count = routes_page.helpers.get_text(routes_page.counter_value)
        assert ice_creams_count == "2"

    def test_modal_appears_to_search_taxi(self):
        routes_page = main.UrbanRoutesPage(self.driver)
        routes_page.modal_appears_to_search_taxi()
        # Validación del modal  para buscar un taxi con la clase order-header-title
        assert routes_page.helpers.is_element_displayed(routes_page.taxi_modal)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
