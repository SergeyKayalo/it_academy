import logging

#1
logging.basicConfig(
    level=logging.INFO,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s - %(lineno)d',
    datefmt = '%Y-%m-%d %H:%M:%S',
    filemode = 'w',
    filename = 'appsession.log'
)

logging.debug("debug test")
logging.info("info test")
logging.critical("critical test")



#2
def repeat_string(text, count):
    assert type(text) == str, "text should be a string"
    assert type(count) == int, "count should be an integer"
    for i in range(count):
        print(text)


repeat_string("text", 3)



#3
logger = logging.getLogger(__name__)
info_handler = logging.FileHandler('combined.log')
info_handler.setLevel(logging.INFO)
error_handler = logging.FileHandler('crit_errors.log')
error_handler.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s - %(filename)s - %(lineno)d')
info_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)
logger.addHandler(info_handler)
logger.addHandler(error_handler)

logger.info("info test")
logger.warning("warn test")
logger.error("error test")



#4
logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s - %(lineno)d',
    datefmt = '%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
    force=True   #сброс предыдущих настроек из задания 1
)
user_data = {"name": "Alice"}
try:
    print (user_data["age"])
except KeyError:
    logging.exception("user_data key error")



#5
def process_payment(amount):
    try:
        assert amount > 0
    except AssertionError:
        logger.exception("amount should be positive")
        return False
    logger.info("Платеж на сумму X проведен успешно")
    return True

process_payment(1)