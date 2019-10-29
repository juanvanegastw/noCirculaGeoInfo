import unittest
from ..src.toolutils import clean_data
from ..src.toolutils import structure_message


class TestMessageParser(unittest.TestCase):
    def test_should_remove_no_ascii_characters(self):
        message_with_special_characters = "5️⃣ y 6️⃣"

        clean_message = clean_data(message_with_special_characters)

        self.assertEqual(clean_message, "5 y 6")

    def test_should_return_holograma_1_2_when_included_in_message(self):
        message = "##HoyNoCircula aplica para coches con holograma 1 y 2, engomado amarillo y terminación"\
                  " de placa5️⃣ y 6️⃣ #MovilidadCDMX"

        structured_message = structure_message(message)

        self.assertEqual(structured_message['hologramas'], [1, 2])

    def test_should_return_placas_5_y_when_included_in_message(self):
        message = "##HoyNoCircula aplica para coches con holograma 1 y 2, engomado amarillo y terminación"\
                  " de placa5️⃣ y 6️⃣ #MovilidadCDMX"

        structured_message = structure_message(message)

        self.assertEqual(structured_message['placas'], [5, 6])

    def test_should_return_color_when_included_in_message(self):
        message = "##HoyNoCircula aplica para coches con holograma 1 y 2, engomado amarillo y terminación" \
                  " de placa5️⃣ y 6️⃣ #MovilidadCDMX"

        structured_message = structure_message(message)

        self.assertEqual(structured_message['color'], 'amarillo')

    def test_should_return_holograma_1_y_2(self):
        message = "#HoyNoCircula Martes 29 de octubre en la #ZMVM para vehículos con #EngomadoRosa con terminación de placas 7 y 8, holograma 1 y 2."

        structured_message = structure_message(message)

        self.assertEqual(structured_message['hologramas'], [1, 2])

    def test_should_return_placas_7_y_8(self):
        message = "#HoyNoCircula Martes 29 de octubre en la #ZMVM para vehículos con #EngomadoRosa con terminación de placas 7 y 8, holograma 1 y 2."

        structured_message = structure_message(message)

        self.assertEqual(structured_message['placas'], [7, 8])

    def test_should_return_color_amarillo(self):
        message = "#HoyNoCircula Martes 29 de octubre en la #ZMVM para vehículos con #EngomadoRosa con terminación de placas 7 y 8, holograma 1 y 2."

        structured_message = structure_message(message)

        self.assertEqual(structured_message['color'], 'Rosa')

