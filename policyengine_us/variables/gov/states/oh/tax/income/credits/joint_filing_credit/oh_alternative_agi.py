from policyengine_us.model_api import *


class oh_alternative_agi(Variable):
    value_type = float
    entity = Person
    label = (
        "Ohio alternative adjusted gross income for the joint filing credit"
    )
    unit = USD
    definition_period = YEAR
    reference = (
        "https://codes.ohio.gov/ohio-revised-code/section-5747.055",
        "https://tax.ohio.gov/static/forms/ohio_individual/individual/2021/pit-it1040-booklet.pdf#page=20",
    )
    defined_for = StateCode.OH

    adds = ["oh_agi"]

    subtracts = (
        "gov.states.oh.tax.income.credits.joint_filing.agi_subtractions"
    )
