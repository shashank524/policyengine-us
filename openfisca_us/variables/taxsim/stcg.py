from openfisca_us.model_api import *

class stcg(Variable):
    value_type = float
    entity = TaxUnit
    label = "Short-term capital gains"
    unit = "currency-USD"
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        return add(tax_unit, period, ["short_term_capital_gains"])