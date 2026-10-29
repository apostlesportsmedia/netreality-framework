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

## Licensing, attribution, and contributions

**Software and repository documentation:** The code and repository documentation provided here, including `netid_demo.py`, are licensed under the **[Apache License, Version 2.0](LICENSE)**, unless a file explicitly states otherwise. You may use, modify, redistribute, and commercially deploy the licensed code, including independently operated NETID-compatible services, subject to the Apache license terms. No license fee or exclusive APSM API gateway is required to use this repository's Apache-licensed materials.

**Founding research paper:** The white paper *NETID: A Four-Layer Architecture for Historically Grounded Numerical Data and AI Systems*, originally proposed by **Aidan Anderson (2026)**, has its own archival record and license terms at [Zenodo DOI 10.5281/zenodo.23750015](https://doi.org/10.5281/zenodo.23750015). Linking to it here does not change the paper's publication license. For scholarly attribution, please use GitHub's **Cite this repository** option, powered by [`CITATION.cff`](CITATION.cff), or cite the DOI directly. See [`NOTICE`](NOTICE) for the founding provenance notice.

**Separate APSM products:** This repository does **not** release the full APSM website, live Net Income Calculator source, proprietary reports, athlete datasets, trademarks, or future commercial hosted services. Those separate assets are not automatically covered by this repository's license. Anyone may independently build a commercial service using code released here, under Apache 2.0.

**Data rights:** No third-party government, publisher, athlete, or commercial dataset is automatically relicensed by this repository. Future contributors should provide original or appropriately licensed data, document its source and permissions, and avoid including sensitive personal records.

**Contributions:** The project welcomes issues and pull requests for reproducible methods and independent tests. Contributors retain credit for their own contributions, and contributions accepted under Apache 2.0 follow that license unless separately agreed. The original proposal is attributed to Aidan Anderson; this does not claim authorship of subsequent independent engineering or research. Evidence, provenance, and reproducibility take priority over authority.
