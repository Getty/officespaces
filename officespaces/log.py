import logging

logger = None

if not logging.getLogger().hasHandlers():
  logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
  )
if not logger:
  logger = logging.getLogger(__name__)

def L_DEBUG(text):
  logger.debug(text)

def L_INFO(text):
  logger.info(text)

def L_WARN(text):
  logger.warning(text)

def L_ERROR(text):
  logger.error(text)

def L_CRITICAL(text):
  logger.critical(text)

__all__ = ['L_DEBUG','L_INFO','L_WARN','L_ERROR','L_CRITICAL']
