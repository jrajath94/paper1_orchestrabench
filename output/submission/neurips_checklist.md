# NeurIPS 2026 Paper Checklist

This checklist must be included in the submitted paper after the references section. Each item requires a Yes/No/NA response with justification. Papers submitted without this checklist will be desk-rejected.

---

## 1. Claims

**Do the main claims made in the abstract and introduction accurately reflect the paper's contributions and scope?**

Response: Yes

Justification: All claims in the abstract and introduction are directly supported by experimental evidence presented in [SECTION REF: Results] and theoretical analysis in [SECTION REF: Methods]. No claims extend beyond what the evidence demonstrates.

---

## 2. Limitations

**Does the paper discuss the limitations of the work performed by the authors?**

Response: Yes

Justification: Limitations are discussed in [SECTION REF: Limitations/Discussion]. The paper explicitly addresses scope boundaries, assumptions that may not generalize, and conditions under which the approach may underperform.

---

## 3. Theory Assumptions and Proofs

**For each theoretical result, does the paper provide the full set of assumptions and a complete (or correct) proof?**

Response: [Yes/NA -- depends on paper type]

Justification: [If theoretical results exist: "All assumptions are stated in [SECTION REF] and proofs are provided in Appendix [X]." If no theoretical results: "NA -- this is primarily an empirical contribution."]

---

## 4. Experimental Reproducibility

**Does the paper provide sufficient information for reproducing the experiments?**

Response: Yes

Justification: The companion codebase includes all experimental scripts with pinned random seeds, a single-command Makefile setup (`make reproduce`), hardware logging, and expected output checksums for result verification. Full experimental setup details are in [SECTION REF: Experiments] and Appendix [SECTION REF: Experimental Details].

---

## 5. Open Access to Data and Code

**Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results?**

Response: Yes

Justification: An anonymous repository is provided for review. The repository will be de-anonymized upon acceptance. All datasets used are publicly available with licenses cited. The reproducibility package includes installation instructions, dependency specifications, and verification checksums.

---

## 6. Experimental Setup and Details

**Does the paper specify all the training and test details (e.g., data splits, hyperparameters, how they were chosen, best validation results)?**

Response: Yes

Justification: Full experimental setup including hyperparameters, data splits, selection criteria, and configuration files are specified in [SECTION REF: Experiments] and Appendix [SECTION REF: Experimental Details]. Hyperparameter search ranges and selection methodology are documented.

---

## 7. Error Bars and Statistical Significance

**Does the paper report error bars suitably and correctly?**

Response: Yes

Justification: Statistical significance is assessed using Shapiro-Wilk normality test to select between paired t-test and Wilcoxon signed-rank test as appropriate. Error bars, confidence intervals, and p-values are reported in [SECTION REF: Results]. The number of experimental runs and variance sources are documented.

---

## 8. Compute Resources

**Does the paper report the computational resources required?**

Response: Yes

Justification: Hardware specifications are captured automatically via hardware logging and reported in Appendix [SECTION REF: Compute Resources]. Total compute time, GPU/CPU specifications, and memory requirements are documented.

---

## 9. Code of Ethics

**Does the research conducted in the paper conform to the NeurIPS Code of Ethics?**

Response: Yes

Justification: This research involves no human subjects, no personally identifiable information, and no dual-use concerns. The work conforms to the NeurIPS Code of Ethics. LLM usage is disclosed transparently in the paper appendix.

---

## 10. Broader Impacts

**Does the paper discuss both potential positive societal impacts and negative societal impacts of the work performed?**

Response: Yes

Justification: A Broader Impact section is included in the paper addressing both potential benefits (e.g., improved efficiency, accessibility of [DOMAIN] research) and risks (e.g., potential misuse, environmental cost of compute). [SECTION REF: Broader Impact]

---

## 11. Safeguards

**Does the paper describe safeguards that have been put in place for responsible release of data or models that have a high risk for misuse?**

Response: [Yes/NA]

Justification: [If applicable: "Safeguards are described in [SECTION REF]." If not: "NA -- the contribution does not present high-risk artifacts. The codebase is a research tool for [DOMAIN] experimentation, not a deployable system with direct misuse potential."]

---

## 12. Licenses for Existing Assets

**Are the creators of assets (e.g., code, data, models) used in the paper properly credited and are the license and terms of use explicitly mentioned and properly respected?**

Response: Yes

Justification: All datasets, libraries, and pre-trained models used are publicly available. Licenses are cited in the references and in the reproducibility package manifest. No proprietary or restricted assets were used without authorization.

---

## 13. New Assets

**Are new assets introduced in the paper well documented and is the documentation provided alongside the assets?**

Response: Yes

Justification: The companion codebase and experimental scripts are released with documentation including a README, installation guide, API documentation, and usage examples. The reproducibility package serves as the primary asset documentation.

---

## 14. Crowdsourcing and Human Subjects

**For crowdsourcing experiments and research with human subjects, does the paper include the full text of instructions given to participants and screenshots?**

Response: NA

Justification: This research does not involve crowdsourcing or human subjects experiments. All evaluations are computational.

---

## 15. IRB Approval

**Does the paper describe potential risks incurred by study participants, whether combensation was coverage of those risks, and whether Institutional Review Board (IRB) approvals were obtained?**

Response: NA

Justification: No human subjects research was conducted. IRB approval is not applicable.

---

## 16. Human Subjects -- Consent and Compensation

**If the study involves human subjects, was informed consent obtained and were participants adequately compensated?**

Response: NA

Justification: No human subjects were involved in this research. No consent or compensation considerations apply.

---

*Checklist completed for NeurIPS 2026 submission. Items with [SECTION REF] placeholders must be updated with actual section numbers before final submission.*
