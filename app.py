__author__ = 'spowell'
import logging

import mongoengine
from flask import Flask
from flask import render_template
from flask import request
from flask_jsonpify import jsonpify as jsonify

from nosql import Loan

logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s",
                    filename="flask_autocomplete.log",
                    filemode="w",
                    level=logging.DEBUG,
                    datefmt="%m/%d/%Y %I:%M:%S %p")

app = Flask(__name__)
flask_setup = {"host": "192.168.1.170", "port": "5000", "debug": True}


@app.before_first_request
def startup():
    mongoengine.connect(name="bank", host="192.168.1.130", port=27017)


@app.route("/bank/loans", methods=["GET"])
def get_loans():
    name = request.args.get("name")

    if name:
        loans = Loan.objects(customer_name__contains=name.upper()).exclude("id")[:10]
    else:
        loans = Loan.objects().exclude("id")[:10]
    results = list()
    if loans:
        for loan in loans:
            results.append(loan.to_mongo())

        for loan in results:
            print(loan)
        return jsonify({"loans": results})
    else:
        return jsonify({"loans": results})


@app.route("/bank/loans/detail")
def eartag_details():
    try:
        name = request.args.get("name")
        found_loan = Loan.objects(customer_name=name).first()
        if found_loan:
            loan_list = list()
            loan_dict = dict()
            loan_dict["customer_name"] = str(found_loan.customer_name)
            loan_dict["approval_date"] = str(found_loan.approval_date)
            loan_dict["appraisal_ordered"] = str(found_loan.appraisal_ordered)
            loan_dict["appraisal_due"] = str(found_loan.appraisal_due)
            loan_dict["appraisal_amount"] = str(found_loan.appraisal_amount)
            loan_dict["appraisal_received"] =  str(found_loan.appraisal_received)
            loan_dict["title_requested"] = str(found_loan.title_requested)
            loan_dict["title_commitment"] = str(found_loan.title_commitment)
            loan_dict["flood_details"] = str(found_loan.flood_details)
            loan_dict["flood_ins_received"] = str(found_loan.flood_ins_received)
            loan_dict["loan_insurance"] = str(found_loan.loan_insurance)
            loan_dict["title_company"] = str(found_loan.title_company)
            loan_dict["attorney"] = str(found_loan.attorney)
            loan_dict["closing_expected"] = str(found_loan.closing_expected)
            loan_dict["information_needed"] = str(found_loan.information_needed)
            loan_list.append(loan_dict)

            return jsonify(loan_details=loan_dict)
        else:
            return jsonify(loan_details="none")
    except Exception as e:
        return str(e)


@app.route("/bank/")
def render_animal():
    try:
        return render_template("loans_mobile.html")
    except Exception as e:
        return str(e)


if '__main__' == __name__:
    app.run(**flask_setup)
