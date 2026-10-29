# NETID — Net Reality Framework

**A four-layer research proposal for historically grounded numerical data and AI systems.**  
**Originating author and proponent:** Aidan Anderson · **Originating application:** [Apostle Sports Media (APSM)](https://apostlesportsmedia.com/)

**White paper:** [NETID v0.2 (Zenodo DOI: 10.5281/zenodo.23750015)](https://doi.org/10.5281/zenodo.23750015) · **ORCID:** [0009-0007-7874-0980](https://orcid.org/0009-0007-7874-0980)

## Purpose

NETID proposes a shared numerical-grounding architecture in which top-down discovery of textual claims is checked against bottom-up observations, defined numerical identities, reproducible transformations, and documented uncertainty. It is an **open research proposal, not a validated universal data layer**. Its four proposed layers are:

1. **Historical Anchor:** traceable observations and chronology (a historical record system is proposed but not built here).
2. **Contextual Drag Filter:** applicable, explicit adjustments rather than one-size-fits-all rates.
3. **Working Midpoint Operator:** correctly classified calculations, estimated ranges, or unresolved outputs—not forced averages between conflicting claims.
4. **Systemic Fracture Matrix:** proposed structural-break/regime-change handling; not implemented in this repository.

A cross-cutting **Numerical Identity and Provenance Principle** preserves what each value means, the assumptions behind it, and how it was derived. The long-term public research proposal welcomes independent evaluation and implementation. See the white paper for the complete hypotheses and limitations.

## Runnable partial proof of concept — APSM NIC Python port

[`netid_demo.py`](netid_demo.py) is a **working deterministic financial calculation example**, translated from the JavaScript in the [APSM Net Income Calculator](https://apostlesportsmedia.com/net-income-calculator/). It uses the supplied NIC's **2026 single-filer federal brackets, standard deduction, self-employment/FICA calculation, and 52 state/D.C./Puerto Rico jurisdiction schedules**. It can apply scenario-specific agent and overhead percentages and returns machine-readable JSON with a calculation breakdown and source/assumption metadata.

This demo is **not** a universal NETID engine, historical grounding database, or AI retrieval middleware deployed in production. It implements parts of the financial **Contextual Drag Filter** and a deterministic-output portion of the **Working Midpoint Operator**. The 1959/1960 historical anchor, actual uncertainty-range estimation, external source verification, top-down/bottom-up claim reconciliation, and **Systemic Fracture Matrix** remain to be developed and tested. Simple arithmetic/integrity flags are **not** evidence of regime-change detection.

### Run locally

Requires **Python 3.9+**; no third-party packages.

```bash
python netid_demo.py --self-test
python netid_demo.py --gross 1000000 --state Washington --agent 0 --overhead 0
python netid_demo.py --gross 1000000 --state California --agent 7 --overhead 8
python netid_demo.py --gross 5000000 --state Ohio --agent 6 --overhead 0
```

Use full jurisdiction names, including `District of Columbia` and `Puerto Rico`. Fees use the same 0–20% bounds as the NIC. Output is JSON with values in USD. The Python code is meant to **preserve** the inputs and calculations, not to state that those inputs have been independently verified.

### NIC parity checks

The Python port was compared with the supplied NIC JavaScript for seven example scenarios, including zero income, WA/CA/OH/NY/FL, and $1 million, $5 million, and $100 million gross cases. Those scenarios matched **within $0.01** for federal, self-employment, state, agent, overhead, and net outputs. `--self-test` also checks jurisdiction coverage, input validity, and accounting relationships. These checks confirm *code parity with the provided snapshot*, not tax-law accuracy or scientific validation of NETID's broader proposal.

### Important limitations

The NIC is an **educational modeled scenario**, not an individualized tax return or financial advice. For reproducibility, the port deliberately preserves the supplied NIC's simplified assumptions (including state taxes calculated on gross, omission of local and duty-day jock taxes, and a single simplified self-employment treatment). Tax status, NIL income characterization, qualified deductions, and actual liability can differ materially. No code in this repository should be described as independently verified tax-law accuracy without further review.

## Research roadmap

**Phase A:** founding proposal and versioned research record.  
**Phase B:** independently sourced and rights-cleared pilot observations, starting with a narrow Washington financial/economic use case.  
**Phase C:** numerical identity rules, evidence reconciliation, uncertainty intervals, and candidate structural-break operators.  
**Phase D:** independent evaluation against credible retrieval and statistical baselines, including accuracy, calibration, source integrity, and cost.  
**Phase E:** interoperable implementations and independently operated services *if* supported by evidence.

APSM remains the operating sports-finance publisher and origin of the financial methodology. The broader public NETID research proposal is separate from any eventual APSM NETID data products or commercial implementations.

## Authorship, rights, and contributions

**Founding proposal:** Aidan Anderson, 2026. Subsequent contributors should receive credit for their own implementations, data stewardship, experiments, and methodological improvements. The archived white paper is the canonical research citation.

**License notice:** This repository currently includes a [`LICENSE`](LICENSE) identified as **Business Source License 1.1 with restrictions until October 27, 2030**. That file is preserved without changes. Its use restrictions are different from an ordinary open-source license; do **not** describe the repository's code as unrestricted open source. The white paper's public-research intent, its copyright terms, the repository license, and permissions for third-party data are distinct questions that should be resolved before asserting unrestricted reuse or starting external contributions. Adding a demonstration does not automatically license other people's data or code.

For proposed improvements, use GitHub issues or pull requests. Technical claims should be testable, cite underlying sources, and keep estimates distinct from observations.