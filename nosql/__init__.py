import mongoengine


class Loan(mongoengine.Document):
    customer_name = mongoengine.StringField(required=True)
    approval_date = mongoengine.DateField(required=False)
    appraisal_ordered = mongoengine.DateField(required=False)
    appraisal_due = mongoengine.DateField(required=False)
    appraisal_amount = mongoengine.DecimalField(required=False)
    appraisal_received = mongoengine.DateField(required=False)
    title_requested = mongoengine.DateField(required=False)
    title_commitment = mongoengine.DateField(required=False)
    flood_details = mongoengine.DateField(required=False)
    flood_ins_received = mongoengine.DateField(required=False)
    loan_insurance = mongoengine.DateField(required=False)
    title_company = mongoengine.StringField(required=False)
    attorney = mongoengine.StringField(required=False)
    closing_expected = mongoengine.DateField(required=False)
    information_needed = mongoengine.StringField(required=False)

    meta = {
        'all_inheritance': True,
        "collection": "loans"
    }



