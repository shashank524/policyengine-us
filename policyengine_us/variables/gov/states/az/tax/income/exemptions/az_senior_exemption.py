from policyengine_us.model_api import *


class az_senior_exemption(Variable):
    value_type = float
    entity = TaxUnit
    label = "Arizona senior exemption"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.AZ

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.az.tax.income.exemptions.senior
        person = tax_unit.members

        # need to check for person age
        age = person("age", period)
        age_eligible = age > p.min_age

        care_and_support_payment = person("care_and_support_payment", period)
        care_and_support_costs = person("care_and_support_costs", period)
        payment_eligible = np.zeros_like(care_and_support_payment)
        mask = care_and_support_costs > 0
        payment_eligible[mask] = (
            (care_and_support_payment[mask] / care_and_support_costs[mask])
            > p.cost_rate
        ) | (care_and_support_payment > p.min_payment)
        eligible_seniors = tax_unit.sum(age_eligible * payment_eligible)
        return p.amount * eligible_seniors
