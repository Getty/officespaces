import logging

logger = None

if not logging.getLogger().hasHandlers():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)u %(message)s'
    )
if not logger:
    logger = logging.getLogger(__name__)


def L_DEBUG(text):
    logger.debug(text, stacklevel=2)


def L_INFO(text):
    logger.info(text, stacklevel=2)


def L_WARN(text):
    logger.warning(text, stacklevel=2)


def L_ERROR(text):
    logger.error(text, stacklevel=2)


def L_CRITICAL(text):
    logger.critical(text, stacklevel=2)


__all__ = ['L_DEBUG', 'L_INFO', 'L_WARN', 'L_ERROR', 'L_CRITICAL']

L_DEBUG("Loaded officespaces.log")
