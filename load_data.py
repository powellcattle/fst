import csv
import logging
import loans

import mongoengine

logging.basicConfig(filename="load_loans.log",
                    format="%(asctime)s %(levelname)s:%(message)s",
                    filemode="w",
                    level=logging.DEBUG,
                    datefmt="%m/%d/%Y %I:%M:%S %p")

mongoengine.connect(name="bank", host="192.168.1.130", port=27017)


loans.load_pastures(r"data/Real Estate Work In Progress.csv")

