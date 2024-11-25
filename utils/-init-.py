import logging

def configurar_logger():
    """
    Configura un logger para la aplicación.
    """
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
    return logging.getLogger(__name__)
