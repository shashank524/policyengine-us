from policyengine_us.model_api import *


class tax_unit_medicaid_income_level(Variable):
    value_type = float
    entity = TaxUnit
    label = (
        "Medicaid/CHIP/ACA-related modified adjusted gross income (MAGI) level"
    )
    unit = "/1"
    documentation = (
        "Medicaid/CHIP/ACA-related MAGI as fraction of federal poverty line."
        "Documentation in the following reference:"
        "  title: 2022 IRS Form 8962 (ACA PTC) instructions for line 4"
        "  href: https://www.irs.gov/pub/irs-pdf/i8962.pdf#page=7"
    )
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        income = tax_unit("medicaid_income", period)
        fpg = tax_unit("tax_unit_fpg", period.last_year)
        return income / fpg
