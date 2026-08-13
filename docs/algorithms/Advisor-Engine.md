# Advisor Engine

**Project:** Enclosure Lab
**Document Version:** 0.1
**Last Updated:** 2026-08-12
**Status:** Draft

---

# Purpose

The Advisor Engine is the decision-making core of Enclosure Lab.

Its purpose is not simply to calculate enclosure alignments.

Its purpose is to evaluate a loudspeaker driver, understand the user's design goals, compare multiple enclosure types, and explain why one solution is recommended over another.

The Advisor Engine functions as an engineering expert rather than a calculator.

---

# Inputs

The Advisor Engine evaluates three categories of information.

## Driver Data

Examples include:

* Fs
* Qts
* Qes
* Qms
* Vas
* Sd
* Xmax
* Re
* Le
* BL
* Mms
* Cms
* Sensitivity
* Rated Power

---

## User Goals

Examples include:

* Deep bass
* Flat frequency response
* Small cabinet
* Maximum SPL
* Home theater
* Music listening
* Studio monitor
* Car audio
* PA
* Line array
* Subwoofer

---

## Design Constraints

Examples include:

* Maximum cabinet size
* Material thickness
* Budget
* Passive or active system
* Port limitations
* Driver orientation
* Manufacturing method
* Available materials

---

# Candidate Enclosure Types

Version 1 should evaluate:

* Sealed
* Ported
* Passive Radiator
* Transmission Line
* 4th Order Bandpass
* 6th Order Bandpass

Future versions may include:

* Horn
* Tapped Horn
* Quarter Wave
* Isobaric
* Open Baffle
* Infinite Baffle
* Hybrid Designs

---

# Evaluation Process

The Advisor Engine evaluates every enclosure independently.

Each enclosure receives scores based on engineering rules.

Example categories include:

* Bass Extension
* Efficiency
* Cabinet Size
* Transient Response
* SPL Capability
* Excursion Control
* Port Performance
* Complexity
* Build Difficulty
* Cost

These scores combine into an overall recommendation.

---

# Explainable Engineering

Every recommendation must include an explanation.

Example:

Recommended: Ported Enclosure

Reason:

* Driver Qts favors vented loading.
* Vas supports a practical cabinet volume.
* Target low-frequency extension can be achieved.
* Cone excursion remains within Xmax.
* Port velocity is acceptable.

Alternative options should also be explained.

---

# Confidence Score

Each recommendation receives a confidence score.

Example:

95%

Confidence is determined by how well the driver's characteristics align with the recommended enclosure.

Recommendations with lower confidence should clearly explain why.

---

# Guiding Principle

The Advisor Engine should always answer three questions.

1. What is the best enclosure?

2. Why is it the best enclosure?

3. What tradeoffs were made?

If those questions cannot be answered clearly, the recommendation is incomplete.

---

# Future Expansion

Future versions of the Advisor Engine may include:

* Rule weighting
* Machine learning assistance
* Measured driver validation
* Historical project learning
* User preference adaptation

The underlying philosophy remains unchanged:

Every recommendation must be understandable, reproducible, and supported by engineering principles.
