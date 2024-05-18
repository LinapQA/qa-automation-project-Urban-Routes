from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# Métodos de apoyo, métodos de espera e interacción con los elementos web

class Helpers:

    # no modificar

    def retrieve_phone_code(self) -> str:
        """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

        import json
        import time
        from selenium.common import WebDriverException
        code = None
        for i in range(10):
            try:
                logs = [log["message"] for log in self.driver.get_log('performance') if log.get("message")
                        and 'api/v1/number?number' in log.get("message")]
                for log in reversed(logs):
                    message_data = json.loads(log)["message"]
                    body = self.driver.execute_cdp_cmd('Network.getResponseBody' ,
                                                       {'requestId': message_data["params"]["requestId"]})
                    code = ''.join([x for x in body['body'] if x.isdigit()])
            except WebDriverException:
                time.sleep(1)
                continue
            if not code:
                raise Exception("No se encontró el código de confirmación del teléfono.\n"
                                "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
            return code

    def __init__(self , driver):
        self.driver = driver

    def wait_for_element(self , locator , timeout=10):
        return WebDriverWait(self.driver , timeout).until(expected_conditions.visibility_of_element_located(locator))

    def click_element(self , locator , timeout=10):
        element = self.wait_for_element(locator , timeout)
        element.click()

    def send_keys(self , locator , keys_to_send , timeout=15):
        element = self.wait_for_element(locator , timeout)
        element.send_keys(keys_to_send)

    def is_element_displayed(self , locator):
        element = self.driver.find_element(*locator)
        return element.is_displayed()

    def is_element_present(self , locator):
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0

    def is_element_active(self , locator):
        element = self.driver.find_element(*locator)
        return element.is_enabled() and element.is_displayed()

    def get_element(self , locator):
        return self.driver.find_element(*locator).get_property("value")

    def get_text(self , locator):
        element = WebDriverWait(self.driver , 10).until(expected_conditions.visibility_of_element_located(locator))
        return element.text
