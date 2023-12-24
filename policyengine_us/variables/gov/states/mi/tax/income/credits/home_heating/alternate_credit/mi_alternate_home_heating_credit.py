## line_45 tax form
from policyengine_us.model_api import *


class mi_alternate_home_heating_credit(Variable):
    value_type = float
    entity = TaxUnit
    label = "Michigan alternate home heating credit amount"
    defined_for = "mi_alternate_heating_credit_eligible"
    unit = USD
    definition_period = YEAR

    reference = (
        "https://www.michigan.gov/-/media/Project/Websites/taxes/2022RM/IIT/MI-1040CR7.pdf?rev=84f72df3f8664b96903aa6b655dc34d2"
        "http://www.legislature.mi.gov/(S(keapvg1h2vndkn25rtmpyyse))/mileg.aspx?page=getObject&objectName=mcl-206-527a"
    )

    # Alternate Credit can not be claimed if claim is for less than 12 months
    def formula(tax_unit, period, parameters):
        p = parameters(
            period
        ).gov.states.mi.tax.income.credits.home_heating_credit

        household_resources = tax_unit("mi_household_resources", period)
        heating_costs = tax_unit("heating_costs", period)
        # Line 42
        capped_heating_costs = min_(heating_costs, p.alternate_credit.heating_costs.cap)
        # Line 43
        reduced_household_resources = household_resources * p.alternate_credit.household_resources.rate
        # Line 44
        reduced_capped_heating_costs = max_(capped_heating_costs - reduced_household_resources, 0)
        # Line 45
        return p.alternate_credit.heating_costs.rate * reduced_capped_heating_costs
