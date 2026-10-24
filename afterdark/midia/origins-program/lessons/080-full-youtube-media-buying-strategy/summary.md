# 80. Full YouTube media buying strategy - Summary

> AI-generated summary of the course lesson (gemini-3.8-flash), written from [transcript.md](transcript.md) and [visual notes](visual_notes.md). It describes what the course teaches; it is not a transcript and not a decision for any business. Check timestamps in the transcript before relying on a claim.

## Overview

This lesson details the agency’s full Meta Ads media buying structure, centering on the "3:2:2:2" setup (three creatives, two primary texts, two headlines, and two landing pages) managed within an Advantage Campaign Budget (CBO) structure. It is aimed at e-commerce brand owners and media buyers seeking a systematic framework to test creative assets, landing pages, and offers simultaneously while scaling spend sustainably. The instructor emphasizes that account structure only supports performance and cannot compensate for weak offers, creative, or landing pages.

---

## Key teachings

- **Never disable winning campaigns:** Do not turn off existing campaigns that are producing results just to switch to a new structure; implement the new structure alongside existing winners [00:02:25].
- **Data tracking requires customized reporting columns:** Columns must be set up intentionally, including audience indicators (age, gender, exclusions) to catch setup errors early [00:03:26], [00:06:06].
- **Consolidate ad spend in CBO:** Brands spending under $1,000/day should operate with only one (or at most two) campaigns to prevent spreading budget too thin across the algorithm [00:09:55].
- **Let the algorithm allocate spend rather than forcing ABO:** Meta’s AI functions like an organic recommendation engine; if an ad fails to receive spend in CBO, it is usually because the algorithm identified it as less competitive in the auction [00:12:21], [00:14:18].
- **Avoid flexible ad formats for creative testing:** Flexible ad formats obscure spend and performance at the individual asset level and group creatives into unwanted carousels; build manual single image/video ads instead [00:36:55], [00:37:50].
- **Produce 9:16 vertical creatives with safe zones:** Build video creative in 9:16 format with core elements within a 4:5 safe area [00:39:24], and images in 9:16 framed to fit 1:1 feeds [00:39:35].
- **Pair proven copy with new copy in testing:** Every creative test should include the best-performing existing primary text and headline alongside one new test copy and headline [00:40:48], [00:42:06].
- **Test landing pages simultaneously:** Testing two URLs (e.g., homepage vs. advertorial or product page vs. listicle) across creative variations forces message congruency and lets Meta send traffic to the highest-converting destination [00:47:08], [00:49:42].
- **Turn off underperforming tests at the ad set level:** Never toggle off individual ads within a dynamic concept batch; shut off the entire ad set if it fails to spend or misses KPI targets [01:05:05], [01:20:10].
- **Attribution window adjustments by spend scale:** Use the standard 7-day click / 1-day view attribution at lower spend; remove 1-day view-through once monthly spend reaches six figures or returning customer rates exceed 15–20% to prevent claiming low-hanging fruit [00:24:20], [00:26:40].

---

## Frameworks and models

### The 3:2:2:2 Ad Set Structure
Adapted from Charley T's 3:2:2 framework, expanded to test landing pages directly:
- **3 Creatives:** Variations of the same creative concept (e.g., 3 video cuts or 3 image iterations) [00:40:26].
- **2 Primary Texts:** Best-performing copy #1 + Test copy #2 [00:40:34].
- **2 Headlines:** Best-performing headline #1 + Test headline #2 [00:42:06].
- **2 Landing Pages:** 3 ads pointed to Landing Page A, duplicated into 3 identical ads pointed to Landing Page B (6 ads total per concept batch ad set) [00:47:08], [00:51:14].

### Ad Set Types Within the Acquisition Campaign
The core Acquisition CBO campaign houses three functional ad sets [00:20:37], [00:56:56]:
1. **Champions Ad Set:** Houses proven winner ads using their original Post IDs (no URL edits) [00:20:46].
2. **Creative Batch Ad Sets:** Dedicated ad sets for testing new concepts using the 3:2:2:2 format (6 ads per batch) [00:35:05], [00:51:14].
3. **Page / Offer Test Ad Sets:** Replicates top-performing creatives to test a new landing page (e.g., listicle, advertorial) or a new front-end offer [00:51:58], [00:55:53].

### The 4 Campaign Types Architecture
As brand spend scales, accounts expand up to four campaigns [01:12:25], [01:16:26]:
1. **Acquisition CBO:** Primary scaling and testing campaign (US first; duplicated into separate campaigns for CA/AU/UK, Europe, or Worldwide) [00:11:00], [01:13:02].
2. **Advantage+ Shopping Campaign (ASC):** Dedicated purely to top-performing winning Post IDs (acts as a secondary champions bucket, no testing) [01:00:22], [01:01:39].
3. **Raw Content CBO:** Unfiltered volume testing bucket for raw UGC and product-seeding videos using single landing pages (used primarily at >$1,000–$2,000/day spend) [01:08:41], [01:09:09].
4. **Whitelisting CBO:** Campaigns running winning UGC creatives directly through creator pages/profiles instead of brand identity [01:10:39], [01:11:40].

---

## Numbers, benchmarks and rules of thumb

- **Minimum Campaign Launch Budget:** $100/day [01:20:49].
- **Max Testing Ad Sets Formula (Spend < $1,000/day):**
  - `Total Tests = Daily Budget / Target CPA` (e.g., $100 budget / $20 tCPA = 5 ad sets maximum per week) [01:03:33], [01:20:03].
  - For budgets > $1,000/day, test volume is unrestricted [01:03:56].
- **Creative Testing Window:**
  - Minimum testing time: 3 days [01:20:10].
  - Standard evaluation window: 7 days [01:04:46], [01:20:10].
  - Maximum test duration: 14 days before turning off non-spenders [01:05:34], [01:20:10].
- **Custom Metrics Formulas:**
  - `Purchase CVR = Purchases / Landing page views` [00:04:33].
  - `Video Hold = ThruPlays / Impressions` [00:05:08].
  - `Video Hook Rate = 3-second video plays / Impressions` [00:05:29].
- **Scaling Budget Bumps (Evaluated over 48–72 hours above target KPI):**
  - Moderate stability: Scale budget by 20% (`Budget x 1.2`) [01:17:18], [01:17:53].
  - Strong performance (e.g., target 2x ROAS achieving 3x–3.5x): Scale by 50% (`Budget x 1.5`) [01:17:33], [01:17:45].
  - Outlier performance (e.g., target 2x ROAS achieving 5x on new winning creative): Scale by 100% (double budget) [01:18:04], [01:18:21].
- **Launch Scheduling Rule:** Always set new campaigns or budget increases to launch at 12:00 AM (midnight) the following day to prevent accelerated intra-day pacing [00:27:11], [01:01:20].

---

## Tools and resources mentioned

- **Meta Ads Manager:** Primary ad buying interface.
- **Shopify & Klaviyo:** Used to export customer email and phone lists to construct 180-day purchaser exclusion custom audiences [00:19:57], [00:29:25].
- **Triple Whale:** External tracking platform requiring universal UTM parameters applied at the ad level [00:44:35].
- **Evolve Skool Community:** Private community platform for training modules and community support [01:22:41].

---

## Exercises and action items assigned

- Set up custom columns in Meta Ads Manager including Purchase CVR, Video Hold, Hook Rate, Excluded Audiences, Age, and Gender [00:04:10], [00:06:18].
- Build a custom audience of 180-day purchasers (plus a customer list from Shopify/Klaviyo) and apply them as exclusions to all acquisition ad sets [00:19:33], [00:29:25].
- Disable automated Advantage+ enhancements on new ads, specifically turning off AI Image Generation, Music, 3D Animation, and Text Improvements, while keeping Overlays and Visual Touch-ups on [00:42:48], [00:43:31].
- Set up a standard UTM tracking parameter across all ad-level configurations [00:45:00].
- Review active ad sets at 7 days; toggle off any ad sets that failed to spend or did not generate conversions [01:04:46].

---

## On-screen material worth reviewing

- **[00:04:33]** Custom columns configuration showing the exact metric list and formula setup for CVR.
- **[00:11:26] & [01:03:14]** Calculation notes showing the maximum number of creative tests per week formula (`Total Tests = Budget / Target CPA`).
- **[00:39:30]** Diagram demonstrating visual framing of a 4:5 safe area centered within a 9:16 vertical canvas.
- **[00:43:31]** Interface checklist of active vs. disabled Advantage+ creative enhancements.
- **[00:56:56]** Clean acquisition campaign architecture display showing the three concurrent ad sets (`Champions`, `Creative BATCH`, `Offer Test`).
- **[01:14:43]** Location setup demonstrating Worldwide inclusion with United States exclusion targeting.
