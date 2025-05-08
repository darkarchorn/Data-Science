import logging
## logging setting
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ],
    force=True
)

logger = logging.getLogger("ArithmethicApp")

def add(a,b):
    logger.debug(f"Adding {a} and {b}...")
    result = a + b
    logger.debug(f"{a} + {b} = {result}")
    return result

def sub(a,b):
    logger.debug(f"Substracting {a} and {b}...")
    result = a - b
    logger.debug(f"{a} - {b} = {result}")
    return result

def mul(a,b):
    logger.debug(f"Multiplying {a} and {b}...")
    result = a * b
    logger.debug(f"{a} * {b} = {result}")
    return result

def divide(a,b):
    try:
        logger.debug(f"Diving {a} and {b}...")
        result = a / b
        logger.debug(f"{a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    
a, b = 3, 4
add(a,b)
sub(a,b)
mul(a,b)
divide(a,b-b)

