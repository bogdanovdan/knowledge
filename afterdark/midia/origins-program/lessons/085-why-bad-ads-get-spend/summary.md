# 85. Why bad ads get spend - Summary

> AI-generated summary of the course lesson (gemini-3.8-flash), written from [transcript.md](transcript.md) and [visual notes](visual_notes.md). It describes what the course teaches; it is not a transcript and not a decision for any business. Check timestamps in the transcript before relying on a claim.

## Overview
This lesson explains why Meta Ads Manager allocates the majority of campaign budget to ads that may appear to have lower ROAS, and how media buyers should properly evaluate ad performance rather than prematurely turning off high-spending creatives [00:00:00]. The instructor details how Meta optimizes for scale and purchase volume, how to identify top-of-funnel prospecting versus retargeting ads using frequency and CPC, and how to use a specific reallocation framework to decide whether an ad should be turned off [00:01:50, [00:07:17]]. The training is aimed at Shopify e-commerce founders and media buyers scaling their ad accounts up to and beyond $100k/month [00:27:13].

## Key teachings
- Meta's algorithm is designed to achieve the highest volume of conversions at the lowest possible cost based on account settings, prioritizing scale over isolated high-ROAS ads that lack volume [00:01:56].
- An ad with the highest spend in an account is often the account's best and most scalable ad because it carries the prospecting volume, even if its ROAS is lower than lower-spending ads [00:03:52, 00:04:24].
- Turning off high-spending prospecting ads often causes overall account ROAS to collapse days later because top-of-funnel traffic dries up, leaving downstream retargeting ads with no new audience to convert [00:09:36, 00:10:07].
- Frequency indicates an ad's position in the funnel: ads with low frequency (around 1.0 to 1.8) and low CPCs typically perform top-of-funnel prospecting, while ads with high frequency (e.g., 3.0+) and higher CPCs are functioning as retargeting [00:08:25, 00:09:12, 00:11:03].
- Do not sort Ads Manager by ROAS to determine winning creatives; tiny spends (e.g., $1 to $5) can produce misleadingly high ROAS numbers (50x–110x) off a single purchase that cannot sustain scale [00:11:23, 00:11:43].
- Always filter and evaluate ads by spend first, as spend is the primary indicator of creative scalability in a CBO structure [00:12:08, 00:12:31].
- When Meta gives $0 to $3 to a newly launched ad over multiple days, it is signaling that the ad has low potential; forcing spend onto it via minimum budgets is generally a waste of money [00:16:43, 00:17:54].
- Meta will rapidly direct spend toward new ads that exhibit strong engagement metrics (high hook rates, high CTRs, and low CPCs) to test for statistical significance [00:17:28, 00:21:35].
- Never make ad-killing decisions based on a single day of data; attribution delays can mask actual performance, and sales often occur several days after the initial click [00:18:36, 00:18:54].

## Frameworks and models
### The Budget Reallocation Decision Framework
Before turning off an ad that is spending budget but showing a lower-than-desired ROAS, follow this decision tree [00:04:42, 00:07:17, 00:22:33]:
1. **Identify the Spend & Metrics:** Check the ad's total spend, ROAS, and frequency relative to other active ads in the account [00:12:31].
2. **Ask the Reallocation Question:** *"If I turn off this ad and its budget is forced into the remaining active ads, will those remaining ads maintain an overall ROAS higher than this ad's current ROAS?"* [00:04:42, 00:24:23].
3. **Factor in Diminishing Returns:** Account for the rule that increasing an ad's spend typically lowers its ROAS efficiency [00:05:22].
4. **Take Action:**
   - **Leave the ad ON:** If the ad is the account's top-spending prospecting pillar and forcing its budget into secondary ads would drop their efficiency below the primary ad's ROAS [00:06:21, 00:24:35].
   - **Turn the ad OFF:** If the ad is not the primary prospecting titan (e.g., spending sub-optimally with sub-1.0 ROAS or low ROAS) and you have multiple proven winners that can absorb the extra budget at higher efficiency [00:06:36, 00:08:03, 00:23:20].

## Numbers, benchmarks and rules of thumb
- Scaling ad budget by 20% typically causes ROAS to drop by 5% to 25% [00:05:32].
- In 95% to 99% of cases, an account's top-spending ad is its primary growth driver and should not be turned off simply for having a lower ROAS than low-spending ads [00:04:24, 00:24:38].
- High-performing volume over vanity metrics: 100 purchases at a 2.0x ROAS is preferable to 5 purchases at a 5.0x ROAS [00:23:56].
- Evaluation timeline: Allow new ads that Meta tests heavily at least 2 to 3 days of multi-day tracking before optimizing or killing them to account for attribution lag [00:22:13, 00:24:16].

## Tools and resources mentioned
- **Meta Ads Manager:** Campaign Budget Optimization (CBO) and ad performance tracking [00:01:03, 00:11:49].
- **Origins Skool Community:** Training community for Shopify stores under $100k/month (`skool.com/origins`) [00:27:19].
- **Evolve:** Advanced growth program/agency for brands doing over $100k/month [00:27:32].

## Exercises and action items assigned
- Review active Meta ad accounts and verify default sorting is set by **Amount Spent (descending)** rather than ROAS or CPA [00:12:08].
- Inspect the frequency and CPC of all top-performing ROAS ads to identify which creatives are driving top-of-funnel discovery versus bottom-of-funnel retargeting [00:08:25, 00:11:03].
- Apply the Budget Reallocation Decision Framework before toggling off any high-spend ad [00:24:23].

## On-screen material worth reviewing
- **[00:02:30] Meta Ads Manager table (Spend vs. ROAS distribution):** Shows how the top-spending ad ($7,516 spend, 1.58 ROAS) drives 96 conversions while higher-ROAS ads have significantly less volume.
- **[00:09:25] & [00:11:25] Secondary Metrics Table:** Demonstrates frequency differences (1.89 on the top prospecting ad vs. 3.21 on the 2.97 ROAS retargeting ad) alongside CPM and CPC comparisons.
- **[00:11:50] Sorting by Lowest Spend Table:** Displays deceptive ROAS figures (e.g., 110.47x ROAS on $1.77 spend) from single purchases that do not represent scale.
- **[00:15:00] - [00:16:30] Daily Progression (Sep 1 to Sep 4):** Case study showing Meta shifting spend day-by-day from an old winner ($6,800/day) to a new super-winner reaching $3,000+/day.
- **[00:23:35] Two-Day Multi-Ad Breakdown:** Example of killing a secondary test ad that spent $3,287 at 1.51 ROAS where spend could be absorbed by two proven ads running at 2.62 and 2.29 ROAS.
