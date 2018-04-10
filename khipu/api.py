# -*- coding: utf-8 -*-
from . import services
from .exceptions import KhipuError


class Khipu(object):
    """
    Método formal para la comunicacion con Khipu
    """

    def __init__(self, receiver_id, secret_key):
        self.receiver_id = receiver_id
        self.secret_key = secret_key

        self.services = [
            'GetBanks',
            'CreatePayment',
            'GetPayment',
        ]

    def service(self, service_name,  **kwargs):
        """
        Llamar los servicios disponibles de Khipu.
        @Parametros:
            service_name: Nombre del servicio requerido de Khipu.
            kwargs: Dict con data que necesita el servicio.
        @Return
            Objeto Request que responde Khipu.
        """
        if service_name in self.services:
            if self.receiver_id and self.secret_key:
                service = getattr(services, service_name)(self.receiver_id, self.secret_key, service_name, **kwargs)
                return service.response()
            else:
                msg = """
                    Necessary authentication for the service {} {} {}
                    """.format(
                    service_name,
                    self.receiver_id,
                    self.secret_key)
                raise KhipuError(msg)
        else:
            msg = "Service does not exist {}".format(service_name)
            raise KhipuError(msg)
