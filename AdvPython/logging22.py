import logging

logging.basicConfig(
    filename="output.log", 
    level=logging.DEBUG, 
    format="%(asctime)s - %(levelname)s - %(message)s"
    )


try:
    logging.debug("program executed started")
    
except Exception as e:
     logging.error("Error")
     logging.critical("CRITICAL")
finally:
      logging.info("information of the code")  
    
    
# logging.debug("program executed started")
# logging.info("information of the code")
# logging.warning("this is a warning")
# logging.error("Error")
# logging.critical("CRITICAL")