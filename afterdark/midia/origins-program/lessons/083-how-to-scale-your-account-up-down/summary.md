# 83. How to scale your account (up & down) - Summary

> AI-generated summary of the course lesson (gemini-3.8-flash), written from [transcript.md](transcript.md) and [visual notes](visual_notes.md). It describes what the course teaches; it is not a transcript and not a decision for any business. Check timestamps in the transcript before relying on a claim.

## Overview
This lesson provides a complete operating protocol for scaling Meta (Facebook) ad spend up and down without collapsing Return on Ad Spend (ROAS) [00:00:00]. The instructor presents a flowchart-driven daily decision tree alongside a four-tier framework that dictates ad account structure as daily budgets grow from $0 to over $100,000 per day [00:00:20, 00:01:24]. It is aimed at e-commerce brand owners and media buyers seeking a systematic approach to ad budget management and account structure simplification [00:00:47, 00:01:17].

---

## Key teachings
- Ad account scaling must follow a systematic Standard Operating Procedure (SOP) evaluated on 24-hour cycles, rather than arbitrary budget spikes [00:00:47, 00:02:40].
- When ROAS drops after scaling up, the failure is usually not the account structure; it occurs because Meta must serve ads to colder audiences, and existing creatives are not compelling enough to convert cold prospects [00:10:11, 00:10:41].
- Never adjust budgets upward based purely on blended view-through attribution; scaling decisions require verifying that the majority of purchases are click-based [00:05:46, 00:06:40].
- When scaling down or hitting a minimum spend plateau, the solutions lie outside the ad account (creative testing, offer creation, audience research, and funnel maintenance), not in constant technical tweaking [00:12:52, 00:14:44].
- Simplified account structures scale farther than complex ones; brands should not adopt multi-campaign, highly segmented structures until spend volume genuinely requires it [00:17:53, 00:25:30].

---

## Frameworks and models

### EAM Scaling Process (Daily Decision Tree)

```
                            [Hitting Target KPI?]
                               /             \
                             YES              NO
                             /                 \
             [In Scaling Protocol (24h)?]    [Below Breakeven KPI for 24-48h?]
             OR [Limited Promo Campaign?]         /                      \
                    /            \              YES                       NO
                  YES             NO             |                         |
                   |               \             |       [Consistently below Target KPI
                   |     [48-72h consistently    |        for 48-72h on 7-day click?]
                   |      above Target KPI?]     |                 /             \
                   |      OR [New Reason to      |               YES              NO
                   |          scale?]            |                |                |
                   |          /        \         |                |         Wait 24 Hours
                   |        YES         NO       |                |
                   |         |           |       |                |
                   |         |     Wait 24 Hours |                |
                   \         /                   \                /
             [>60% Click-Based Data?             [At Minimum Daily Spend?]
              OR Click-Data meets KPI?]                    /            \
                     /          \                        YES             NO
                   YES           NO                       |               |
                    |             \                Do Not Decrease  Decrease Budget 20%
                    |       Wait 24 Hours            Spend Actions         Actions
                    |                                     |                   |
            Increase Budget 20%                   [Launch new DCTs in queue]
            (Or +50-100% if performance           [Audit funnel for bugs & errors]
             is 50-100% above KPI)                [Analyze winning ad data loops]
                                                  [Deep research: avatars/mechanisms]
                                                  [Test new offers]
```

- **Top Decision**: Is the campaign (or entire account) hitting target KPI? [00:02:11]
- **Yes Branch (Scaling Up)**:
  1. Determine if the account is in *Scaling Protocol* (already scaling every 24 hours) or running a time-limited promotional campaign [00:02:30].
  2. If not, check if performance has stayed consistently above target KPI for 48–72 hours, or if there is a "New Reason to Scale" (a newly validated winning ad, offer, or landing page that spikes efficiency) [00:03:32, 00:04:37].
  3. If false, wait 24 hours [00:04:07]. If true, verify attribution: check whether 60% or more of purchases are 7-day click-based (or whether 7-day click data alone hits the KPI target) [00:04:25, 00:06:57].
  4. If attribution check fails, wait 24 hours [00:09:40]. If it passes, increase budget by 20% (or by 50–100% if performance is 50–100% above target) [00:07:14, 00:08:04].
- **No Branch (Scaling Down)**:
  1. Check if performance is below breakeven KPI for 24–48 hours [00:09:56].
  2. If yes, check if the account is at its defined Minimum Daily Spend. If not at minimum, decrease budget by 20% [00:10:55, 00:12:40].
  3. If performance is not below breakeven, check if performance has been consistently below target KPI for 48–72 hours on 7-day click data [00:11:32].
  4. If false, wait 24 hours [00:11:46]. If true, evaluate against Minimum Daily Spend [00:11:51].
  5. If spend is at Minimum Daily Spend, do not decrease spend; trigger parallel non-ad actions [00:12:45].

---

### Four Levels of Ad Account Scaling

| Level | Daily Spend Range | Recommended Account Setup | Key Structural Focus |
| :--- | :--- | :--- | :--- |
| **Level 1** | $0 to $50,000/day [00:17:49] | 1 Campaign (CBO or ASC) [00:17:53, 00:19:50] | Single campaign with dynamic creative testing (DCT) and champion ad sets; keep it unified [00:18:20, 00:22:50]. |
| **Level 2** | $3,000 to $10,000+/day [00:19:32] | Main CBO + Raw Content Campaign [00:19:35, 00:20:05] | Introduce a low-intent testing campaign for raw UGC/TikTok Shop assets alongside the high-intent main CBO [00:20:05, 00:21:18]. |
| **Level 3** | $10,000 to $50,000+/day [00:21:39] | CBOs + Raw Content + ASCs + Whitelisting [00:21:42] | Add Advantage+ Shopping Campaigns (ASC) for scale using proven champions, creator whitelisting campaigns, and regional CBOs [00:22:30, 00:24:10]. |
| **Level 4** | $50,000 to $100,000+/day [00:25:20] | Segmented CBOs + Raw Content + ASCs + Whitelisting [00:25:25] | High segmentation across product collections, discrete customer avatars, and international territories [00:25:40, 00:28:08]. |

---

## Numbers, benchmarks and rules of thumb
- **Scaling protocol qualifying period**: 48 to 72 hours of consistent performance above target KPI [00:03:32].
- **Click-based attribution threshold**: 60% or more of purchases must be click-based (7-day click) before approving a budget increase [00:06:57].
- **Standard scaling increase**: 20% budget increase per 24 hours [00:07:14].
- **Aggressive scaling increase**: 50% to 100% budget increase if ROAS is 50% to 100% above target KPI (e.g., target is 2.5x ROAS and active performance is 3.75x ROAS) [00:08:12, 00:08:25].
- **Standard scaling reduction**: 20% budget reduction; reducing by only 10% is rarely recommended [00:11:06].
- **Breakeven intervention threshold**: 24 to 48 hours below breakeven KPI triggers scaling down [00:09:56].
- **Target underperformance timeline**: 48 to 72 hours of performance below target KPI (on 7-day click) before scaling down [00:11:32].
- **Typical minimum daily spend ranges**: $50 to $200/day for beginner/intermediate brands; $10,000/day floor for brands spending around $20,000/day [00:12:08, 00:12:21].
- **Large budget scaling safety adjustment**: At $10,000/day to $100,000/day spend levels, reduce scaling increments from 20% down to 5%, 10%, or 15% to limit financial risk [00:07:33, 00:07:43].

---

## Tools and resources mentioned
- **Meta Ads Manager**: Used for attribution comparison (7-day click vs. 1-day view/engaged-view) and budget adjustments [00:05:46, 00:06:05].
- **DCT (Dynamic Creative Testing)**: Method for testing 3:2:2 modular creative sets [00:13:08, 00:22:50].
- **ASC (Advantage+ Shopping Campaigns)**: Meta campaign type used for scaling winning creative champions and raw content [00:20:35, 00:22:30].
- **TikTok Shop / Product Seeding**: Sourcing mechanisms for UGC fed into Level 2 Raw Content campaigns [00:20:15, 00:21:10].
- **Whitelisting**: Running Meta ads directly through creator social handles rather than the brand's handle [00:24:05].
- **Evolve Community Winning Ads Document**: Internal resource containing top-spending reference creatives [00:15:31].

---

## Exercises and action items assigned
- **Calculate your brand's Minimum Daily Spend**: Determine the hard dollar baseline you will sustain for 30 days regardless of immediate results, based on current cash flow and reserves [00:12:00, 00:12:30].
- **Run the Click-Attribution Audit**: Open Meta Ads Manager, select "Compare attribution settings," and verify if 7-day click conversions equal 60%+ of total reported purchases before applying a budget increase [00:05:46, 00:06:57].
- **Execute the Non-Ad Protocol on Spend Drops**: Whenever budget cannot be scaled up or hits the minimum spend floor, complete the five-step diagnostic checklist [00:12:45]:
  1. Queue and launch new Dynamic Creative Tests (DCTs) [00:13:06].
  2. Audit the entire website funnel (cart code, checkout flows, inventory status, mobile layout) [00:13:08, 00:13:30].
  3. Perform ad data analysis to close learnings/feedback loops on winning hooks and visual angles [00:13:53].
  4. Conduct research into fresh customer avatars and new product mechanisms [00:14:30].
  5. Design and test fresh seasonal offers, bundles, or pricing structures [00:16:04, 00:17:15].

---

## On-screen material worth reviewing
- **[00:01:55] & [00:29:35] EAM Scaling Process Flowchart**: Complete visual representation of the decision hierarchy for daily budget management.
- **[00:05:50] Meta Ads Manager Compare Attribution Settings Modal**: Configuration showing how to isolate 7-day click data from view-through metrics.
- **[00:06:30] Click-Based Attribution Metrics Comparison Table**: Real ad account columns demonstrating the comparison between blended purchases and 7-day click purchases.
- **[00:19:15] Single Campaign $50k/Day Spend Metric View**: Proof of account structure simplicity with $50,429.55 spent on a single campaign at a 2.11 ROAS.
- **[00:20:35] Level 2 Campaign Architecture Table**: Multi-campaign setup showing a primary high-intent CBO campaign running alongside low-spend Raw Content ASC and testing campaigns.
- **[00:27:35] & [00:27:45] Pre-BFCM Promo Structure Breakdown**: Ad set setup showing Hot-90, Warm-60, and Broad targeting within a single promo campaign scaling to $50,000–$100,000/day.
