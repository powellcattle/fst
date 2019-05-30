import csv
import logging
import inspect

import util
from nosql import Loan


def load_pastures(_file_name):
    try:
        with open(_file_name, "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(reader, None)
            for row in reader:
                loan = Loan()
                loan.customer_name = util.to_upper_or_none(row[0])
                loan.approval_date = util.to_date_or_none(row[1])
                loan.appraisal_ordered = util.to_date_or_none(row[2])
                loan.appraisal_due = util.to_date_or_none(row[3])
                loan.appraisal_amount = util.to_float_or_none(row[4])
                loan.appraisal_received = util.to_date_or_none(row[5])
                loan.title_requested = util.to_date_or_none(row[6])
                loan.title_commitment = util.to_date_or_none(row[7])
                loan.flood_details = util.to_date_or_none(row[8])
                loan.flood_ins_received = util.to_date_or_none(row[9])
                loan.loan_insurance = util.to_date_or_none(row[10])
                loan.title_company = util.to_upper_or_none(row[11])
                loan.attorney = util.to_upper_or_none(row[12])
                loan.closing_expected = util.to_date_or_none(row[13])
                loan.information_needed = util.to_upper_or_none(row[14])

                loan.save()

    except Exception as e:
        logging.error("{} {}".format(inspect.stack()[0][3], e))

    finally:
        if csvfile:
            csvfile.close()
