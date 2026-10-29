"""NETID/APSM NIC deterministic reference demo (2026 snapshot).

This is a *partial* proof of concept ported from APSM's Net Income Calculator.
It does NOT implement historical anchoring, external source verification,
text/numeric reconciliation, or the Systemic Fracture Matrix described in
NETID v0.2. It is NOT a validated universal NETID implementation.

The calculation reproduces the supplied APSM NIC JavaScript assumptions,
which are simplified educational scenarios, not personal tax advice.
No external dependencies; Python 3.9+.
"""

import argparse
import json
import math
from typing import Dict, List

SOURCE_ENGINE = "https://apostlesportsmedia.com/net-income-calculator/"
RESEARCH_DOI = "https://doi.org/10.5281/zenodo.23750015"
TAX_YEAR = 2026
MAX_GROSS = 1_000_000_000
STANDARD_DEDUCTION = 16_100.0
SOCIAL_SECURITY_WAGE_BASE = 184_500.0
FEDERAL_BRACKETS = [
    [0, .10], [12_400, .12], [50_400, .22], [105_700, .24],
    [201_775, .32], [256_225, .35], [640_600, .37],
]

# Exactly transcribed from the uploaded APSM NIC HTML/JS snapshot.
# These are the NIC's simplified 2026 state schedules, NOT an independently
# audited legal dataset. State-specific deductions and local taxes are omitted.
STATE_BRACKETS = {
    "Alabama": [[0,0.02],[500,0.04],[3000,0.05]],
    "Alaska": [[0,0]],
    "Arizona": [[0,0.025]],
    "Arkansas": [[0,0.02],[4600,0.039]],
    "California": [[0,0.01],[11079,0.02],[26264,0.04],[41452,0.06],[57542,0.08],[72724,0.093],[371479,0.103],[445771,0.113],[742953,0.123],[1000000,0.133]],
    "Colorado": [[0,0.044]],
    "Connecticut": [[0,0.02],[10000,0.045],[50000,0.055],[100000,0.06],[200000,0.065],[250000,0.069],[500000,0.0699]],
    "Delaware": [[0,0],[2000,0.022],[5000,0.039],[10000,0.048],[20000,0.052],[25000,0.0555],[60000,0.066]],
    "District of Columbia": [[0,0.04],[10000,0.06],[40000,0.065],[60000,0.085],[250000,0.0925],[500000,0.0975],[1000000,0.1075]],
    "Florida": [[0,0]],
    "Georgia": [[0,0.0519]],
    "Hawaii": [[0,0.014],[9600,0.032],[14400,0.055],[19200,0.064],[24000,0.068],[36000,0.072],[48000,0.076],[125000,0.079],[175000,0.0825],[225000,0.09],[275000,0.1],[325000,0.11]],
    "Idaho": [[0,0],[4811,0.053]],
    "Illinois": [[0,0.0495]],
    "Indiana": [[0,0.0295]],
    "Iowa": [[0,0.038]],
    "Kansas": [[0,0.052],[23000,0.0558]],
    "Kentucky": [[0,0.035]],
    "Louisiana": [[0,0.03]],
    "Maine": [[0,0.058],[27399,0.0675],[64849,0.0715]],
    "Maryland": [[0,0.02],[1000,0.03],[2000,0.04],[3000,0.0475],[100000,0.05],[125000,0.0525],[150000,0.055],[250000,0.0575],[500000,0.0625],[1000000,0.065]],
    "Massachusetts": [[0,0.05],[1083150,0.09]],
    "Michigan": [[0,0.0425]],
    "Minnesota": [[0,0.0535],[33310,0.068],[109430,0.0785],[203150,0.0985]],
    "Mississippi": [[0,0],[10000,0.04]],
    "Missouri": [[0,0],[1348,0.02],[2696,0.025],[4044,0.03],[5392,0.035],[6740,0.04],[8088,0.045],[9436,0.047]],
    "Montana": [[0,0.047],[47500,0.0565]],
    "Nebraska": [[0,0.0246],[4130,0.0351],[24760,0.0455]],
    "Nevada": [[0,0]],
    "New Hampshire": [[0,0]],
    "New Jersey": [[0,0.014],[20000,0.0175],[35000,0.035],[40000,0.0553],[75000,0.0637],[500000,0.0897],[1000000,0.1075]],
    "New Mexico": [[0,0.015],[5500,0.032],[16500,0.043],[33500,0.047],[66500,0.049],[210000,0.059]],
    "New York": [[0,0.039],[8500,0.044],[11700,0.0515],[13900,0.054],[80650,0.059],[215400,0.0685],[1077550,0.0965],[5000000,0.103],[25000000,0.109]],
    "North Carolina": [[0,0.0399]],
    "North Dakota": [[0,0],[48475,0.0195],[244825,0.025]],
    "Ohio": [[0,0],[26050,0.0275]],
    "Oklahoma": [[0,0],[3750,0.025],[4900,0.035],[7200,0.045]],
    "Oregon": [[0,0.0475],[4550,0.0675],[11400,0.0875],[125000,0.099]],
    "Pennsylvania": [[0,0.0307]],
    "Puerto Rico": [[0,0.33]],
    "Rhode Island": [[0,0.0375],[82050,0.0475],[186450,0.0599]],
    "South Carolina": [[0,0],[3640,0.03],[18230,0.06]],
    "South Dakota": [[0,0]],
    "Tennessee": [[0,0]],
    "Texas": [[0,0]],
    "Utah": [[0,0.045]],
    "Vermont": [[0,0.0335],[49400,0.066],[119700,0.076],[249700,0.0875]],
    "Virginia": [[0,0.02],[3000,0.03],[5000,0.05],[17000,0.0575]],
    "Washington": [[0,0]],
    "West Virginia": [[0,0.0222],[10000,0.0296],[25000,0.0333],[40000,0.0444],[60000,0.0482]],
    "Wisconsin": [[0,0.035],[15110,0.044],[51950,0.053],[332720,0.0765]],
    "Wyoming": [[0,0]],
}

def progressive_tax(income: float, brackets: List[List[float]]) -> float:
    """Return marginal-bracket tax. This matches the NIC's progressiveTax()."""
    tax = 0.0
    for index, (floor, rate) in enumerate(brackets):
        ceiling = brackets[index + 1][0] if index + 1 < len(brackets) else math.inf
        if income > floor:
            tax += (min(income, ceiling) - floor) * rate
    return tax


def nic_self_employment_tax(gross: float) -> Dict[str, float]:
    """Mirror NIC calcSETax, including its simplified treatment."""
    se_base = gross * 0.9235
    oasdi = min(se_base, SOCIAL_SECURITY_WAGE_BASE) * 0.124
    medicare = se_base * 0.029
    # Deliberately match NIC condition and base, not a separate tax-law model.
    additional = max(0.0, (se_base - 200_000.0) * 0.009) if gross > 200_000 else 0.0
    return {
        "base": se_base,
        "oasdi": oasdi,
        "medicare": medicare,
        "additional_medicare": additional,
        "total": oasdi + medicare + additional,
    }


def _nonnegative_finite(value: float, field: str) -> float:
    if not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
        raise ValueError(f"{field} must be a nonnegative finite number")
    return float(value)


class NETIDMiddleware:
    """Small domain-specific adapter: NIC numbers -> typed, auditable output.

    The name describes a proposed use as middleware, NOT the completed
    four-layer NETID research framework.
    """

    def __init__(self, target_state="Washington", agent_fee_pct=0.0, overhead_pct=0.0):
        if target_state not in STATE_BRACKETS:
            raise ValueError(f"Unknown jurisdiction {target_state!r}; use full NIC names")
        self.target_state = target_state
        self.agent_fee_pct = _nonnegative_finite(agent_fee_pct, "agent_fee_pct")
        self.overhead_pct = _nonnegative_finite(overhead_pct, "overhead_pct")
        if self.agent_fee_pct > 20 or self.overhead_pct > 20:
            raise ValueError("NIC fee sliders permit 0% to 20% for agent and overhead")

    def calculate_net_retention(self, gross: float) -> dict:
        gross = _nonnegative_finite(gross, "gross")
        if gross > MAX_GROSS:
            raise ValueError("Gross exceeds the NIC's $1,000,000,000 maximum")

        se = nic_self_employment_tax(gross)
        # The NIC deducts half of Schedule SE, excluding Additional Medicare.
        se_deductible = se["total"] - se["additional_medicare"]
        federal_taxable = max(0.0, gross - STANDARD_DEDUCTION - se_deductible / 2)
        federal_tax = progressive_tax(federal_taxable, FEDERAL_BRACKETS)
        state_tax = progressive_tax(gross, STATE_BRACKETS[self.target_state])
        agent_fee = gross * self.agent_fee_pct / 100.0
        overhead = gross * self.overhead_pct / 100.0
        total_out = federal_tax + se["total"] + state_tax + agent_fee + overhead
        net = gross - total_out
        score = max(0.0, min(100.0, net / gross * 100)) if gross > 0 else 0.0

        # Arithmetic integrity flags are NOT macroeconomic fracture detection.
        flags = []
        if net < 0:
            flags.append("NEGATIVE_MODELED_CASH_FLOW")
        if abs(gross - total_out - net) > 0.00001:
            flags.append("ACCOUNTING_IDENTITY_MISMATCH")

        # Keep numeric values machine-readable, with rounded display only at presentation.
        money = lambda n: round(n, 2)
        return {
            "status": "modeled_estimate",
            "measurement": "annual modeled net take-home (NIC educational assumptions)",
            "inputs": {
                "gross_usd": money(gross), "jurisdiction": self.target_state,
                "agent_fee_pct": self.agent_fee_pct,
                "overhead_pct": self.overhead_pct,
                "tax_year": TAX_YEAR,
            },
            "breakdown_usd": {
                "gross": money(gross),
                "federal_income_tax": money(federal_tax),
                "self_employment_and_fica": money(se["total"]),
                "state_income_tax": money(state_tax),
                "agent_fee": money(agent_fee),
                "career_overhead": money(overhead),
                "total_deductions": money(total_out),
                "estimated_net_take_home": money(net),
            },
            "retention_score_0_to_100": round(score, 4),
            "integrity_flags": flags,
            "provenance": {
                "source": "APSM Net Income Calculator (supplied HTML/JS snapshot)",
                "source_url": SOURCE_ENGINE,
                "research_proposal": RESEARCH_DOI,
                "source_verified_independently": False,
                "assumptions": [
                    "2026 NIC single-filer federal bracket and deduction constants",
                    "2026 NIC state brackets on gross without state-specific deductions",
                    "NIC simplified self-employment/FICA and half-SE deduction model",
                    "Local/jock taxes and income type differences not modeled",
                    "Fees/overhead deducted after NIC tax calculations (no fee deductibility model)",
                    "Not personalized financial or tax advice",
                ],
            },
            "netid_layer_coverage": {
                "historical_anchor": "NOT IMPLEMENTED; 2026 NIC schedule snapshot only",
                "contextual_drag_filter": "PARTIAL; NIC progressive taxes and scenario fees",
                "working_midpoint_operator": "PARTIAL; deterministic NIC result only, no inferred range",
                "systemic_fracture_matrix": "NOT IMPLEMENTED; arithmetic flags are not regime detection",
                "text_to_numeric_reconciliation": "NOT IMPLEMENTED",
            },
        }


def self_test() -> None:
    # Independently generated JS-matching expectations (see README).
    assert len(STATE_BRACKETS) == 52
    assert progressive_tax(12_400, FEDERAL_BRACKETS) == 1_240
    assert progressive_tax(0, FEDERAL_BRACKETS) == 0
    assert NETIDMiddleware("Washington", 0, 0).calculate_net_retention(0)["breakdown_usd"]["estimated_net_take_home"] == 0
    for state in ("California", "Washington", "Ohio", "Florida", "New York"):
        item = NETIDMiddleware(state, 7, 8).calculate_net_retention(1_000_000)
        bd = item["breakdown_usd"]
        assert abs(bd["gross"] - bd["total_deductions"] - bd["estimated_net_take_home"]) <= 0.02
        assert 0 <= item["retention_score_0_to_100"] <= 100
    assert NETIDMiddleware("Washington", 0, 0).calculate_net_retention(1_000_000)["breakdown_usd"]["state_income_tax"] == 0
    assert NETIDMiddleware("California", 0, 0).calculate_net_retention(1_000_000)["breakdown_usd"]["state_income_tax"] > 0
    try:
        NETIDMiddleware("Atlantis").calculate_net_retention(1_000_000)
        raise AssertionError("Unknown state accepted")
    except ValueError:
        pass
    print("Self-test passed: 52 jurisdictions, boundaries, accounting identity and input validity")


def main() -> None:
    parser = argparse.ArgumentParser(description="NETID partial demonstration using the APSM NIC 2026 tax engine")
    parser.add_argument("--gross", type=float, default=1_000_000, help="Annual gross income (NIC max $1B)")
    parser.add_argument("--state", default="Washington", choices=sorted(STATE_BRACKETS))
    parser.add_argument("--agent", type=float, default=0, help="Agent fee percentage, 0–20")
    parser.add_argument("--overhead", type=float, default=0, help="Overhead percentage, 0–20")
    parser.add_argument("--self-test", action="store_true", help="Run sanity tests instead of sample calculation")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    try:
        result = NETIDMiddleware(args.state, args.agent, args.overhead).calculate_net_retention(args.gross)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()