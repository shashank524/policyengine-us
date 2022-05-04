from openfisca_us.model_api import *


class taxable_ui_agi(Variable):
    value_type = float
    entity = TaxUnit
    label = "Adjusted gross income (SS)"
    unit = USD
    documentation = "Income used to determine taxability of unemployment insurance."
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        irs = parameters(period).irs
        gross_income_sources = irs.gross_income.sources
        income_sources_without_ss = [income_source for income_source in gross_income_sources if income_source != "taxable_unemployment_insurance"]
        gross_income = add(tax_unit, period, income_sources_without_ss)
        above_the_line_deductions = irs.ald.deductions
        total_deductions = add(tax_unit, period, above_the_line_deductions)
        return max_(0, gross_income - total_deductions)