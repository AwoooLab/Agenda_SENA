"""Prueba inicial del modelo de citas."""

import unittest

from src.model import Cita


class ModeloTest(unittest.TestCase):
    def test_convertir_cita_a_diccionario(self):
        cita = Cita("Clase", "2026-10-23", "18:00")
        datos = cita.a_diccionario()
        self.assertEqual(datos["titulo"], "Clase")
        self.assertEqual(datos["hora"], "18:00")


if __name__ == "__main__":
    unittest.main()
