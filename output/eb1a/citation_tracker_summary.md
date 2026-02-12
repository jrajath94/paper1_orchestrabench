# Citation Impact Tracking Summary

**Prepared for:** EB1A Extraordinary Ability Petition -- Citation Evidence
**Companion file:** `citation_tracker.json` (programmatic tracking data)
**Last updated:** Pre-publication (no citation data yet)

---

## Paper Metadata

| Field | Value |
|-------|-------|
| Title | [FROM paper_state.json] |
| Authors | [Sole Author Name] |
| Venue | NeurIPS 2026 |
| Year | 2026 |
| DOI | Pending (assigned post-publication) |
| arXiv ID | Pending |
| Semantic Scholar ID | Pending |
| OpenAlex ID | Pending |
| Publication Date | Pending |

---

## Tracking Sources

Citation data is collected from three independent academic databases to ensure comprehensive coverage and cross-validation:

| Source | URL | Update Frequency | Coverage |
|--------|-----|------------------|----------|
| Google Scholar | https://scholar.google.com/ | Monthly | Broadest coverage including preprints, theses, and informal citations |
| Semantic Scholar | https://api.semanticscholar.org/ | Monthly | AI/ML focused, provides citation context and intent classification |
| OpenAlex | https://api.openalex.org/ | Monthly | Open scholarly metadata, institution and country-level citation data |

---

## Current Metrics

All metrics are zero at pre-publication. These will be updated monthly after the paper is published and indexed.

| Metric | Value | EB1A Relevance |
|--------|-------|----------------|
| Total Citations | 0 | Demonstrates the work is being referenced by others in the field |
| Independent Citations | 0 | Citations from research groups with no co-authorship relationship (strongest USCIS evidence) |
| International Citations | 0 | Citations from researchers outside the petitioner's country (demonstrates global impact) |
| Industry Citations | 0 | Citations from industry labs and companies (demonstrates practical significance) |
| Self-Citations | 0 | Citations by the author in their own subsequent work (excluded from independent count) |
| h-index Contribution | 0 | Contribution of this paper to the author's h-index |
| Field-Weighted Citation Impact | N/A | Citation count normalized against the field average (available post-publication) |

---

## Citation Milestones

Track these milestones for EB1A evidence strength assessment:

| Milestone | Citations | Significance |
|-----------|-----------|--------------|
| Initial traction | 10 | Paper is being noticed and cited in the field |
| Established impact | 25 | Paper has meaningful influence on subsequent research |
| Strong impact | 50 | Paper is a significant reference point in its subfield |
| High impact | 100 | Paper is widely influential and frequently cited |

### Notable Venue Citations

Citations from these venues carry extra weight for demonstrating field significance:
- **NeurIPS** -- Top-tier ML conference
- **ICML** -- Top-tier ML conference
- **ICLR** -- Top-tier ML conference
- **AAAI** -- Major AI conference
- **Nature** -- Premier scientific journal
- **Science** -- Premier scientific journal

---

## Update Instructions

### Monthly Update Cadence

After the paper is published and indexed (typically 2-4 weeks post-publication), perform the following monthly update:

1. **Query Semantic Scholar API:**
   ```
   GET https://api.semanticscholar.org/graph/v1/paper/{semantic_scholar_id}
   ?fields=citationCount,citations.title,citations.authors,citations.venue,citations.year
   ```

2. **Query OpenAlex API:**
   ```
   GET https://api.openalex.org/works/{openalex_id}
   ?select=cited_by_count,cited_by_api_url
   ```

3. **Check Google Scholar** (manual -- no official API):
   - Search for the paper title on Google Scholar
   - Record the "Cited by N" count
   - Note any new citing papers not found in Semantic Scholar or OpenAlex

4. **Update citation_tracker.json:**
   - Add a new snapshot to the `snapshots` array with the current date and citation counts from each source
   - Add any new citing papers to the `citing_papers` array with full metadata
   - Update `eb1a_metrics` with recalculated totals (independent, international, industry breakdowns)
   - Set `last_updated` to the current ISO date

5. **Classify new citations:**
   - **Independent:** No shared co-authors with the petitioner
   - **International:** Citing authors affiliated with institutions outside the petitioner's country
   - **Industry:** Citing authors affiliated with companies or industry research labs
   - **Self:** Petitioner is an author on the citing paper

### Snapshot Format

Each monthly snapshot should follow this structure in `citation_tracker.json`:
```json
{
  "date": "2026-MM-DD",
  "google_scholar": N,
  "semantic_scholar": N,
  "openalex": N,
  "notes": "Any notable citations or trends"
}
```

---

## EB1A Relevance

Citation metrics are critical evidence for USCIS Criterion 5 (original contributions of major significance). Specifically:

- **Independent citations** from other research groups demonstrate that the contribution has been recognized and built upon by others in the field, independent of any personal or professional relationship with the petitioner. This is the strongest form of citation evidence for USCIS purposes.

- **International citations** demonstrate global impact -- that the work is relevant and valuable to researchers worldwide, not just within a single institution or country.

- **Industry citations** demonstrate practical significance -- that the contribution has implications beyond academic research and is being applied or referenced in commercial or applied settings.

- **Citation velocity** (rate of citation accumulation) can demonstrate growing impact and sustained relevance in the field.

- **Citations from top venues** (NeurIPS, ICML, ICLR, Nature, Science) demonstrate that the citing work itself meets high quality standards, lending additional weight to the citation as evidence of significance.

USCIS adjudicators evaluate citation evidence as part of the "totality of evidence" under the two-step Kazarian framework. Strong citation metrics, combined with venue quality and expert testimony, build a compelling case for extraordinary ability.

---

*Document version: 1.0*
*Template created: 2026-03-15*
*Note: This summary reflects pre-publication status. Update monthly after publication using the instructions above.*
