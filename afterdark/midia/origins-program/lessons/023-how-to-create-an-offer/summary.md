# 23. How to create an offer - Summary

> AI-generated summary of the course lesson (gemini-3.8-flash), written from [transcript.md](transcript.md) and [visual notes](visual_notes.md). It describes what the course teaches; it is not a transcript and not a decision for any business. Check timestamps in the transcript before relying on a claim.

## Overview
This lesson teaches e-commerce founders how to design, model, and split-test profitable offers using a structured margin spreadsheet and key economic metrics like Revenue Per Session (RPS) and Profit Per Session (PPS). The instructor walks through how to balance Average Order Value (AOV), conversion rate (CVR), and cost of goods sold (COGS) to find an optimal offer structure before testing it in Meta Ads. It is aimed at media buyers and store owners seeking to scale their ad accounts by improving the fundamentals of what customers buy.

## Key teachings
- A winning offer makes scaling on Meta much easier because better offers convert higher-intent traffic at higher rates, driving up ROAS through conversion rate and AOV improvements [00:00:11].
- Never rely on general store-wide Shopify conversion rates for evaluating offers; track custom Conversion Rate and custom AOV metrics inside Meta Ads Manager (calculated as `Purchases / Website Landing Page Views`) because Shopify numbers fluctuate wildly and lack ad-level attribution [00:10:16], [00:15:00], [00:37:17].
- Always verify true unit economics with suppliers (exact COGS, incremental pick-and-pack, shipping per unit) and overestimate costs rather than underestimate them [00:01:21], [00:06:30].
- Bundling generates superior margins primarily when incremental shipping costs remain flat or rise minimally while selling two or three units [00:03:36], [00:23:08].
- Profitability is not driven by AOV maxing or CVR maxing alone; the real driver is optimizing both together through Revenue Per Session and Profit Per Session [00:11:44], [00:17:53].
- A lower price or lower margin (such as a BOGO offer at ~53% margin) can yield substantially higher profit per session if it unlocks a massive conversion rate jump [00:19:39].
- Early-stage e-commerce brands should avoid forcing subscriptions before establishing basic product profitability and customer retention, as premature subscriptions require money to fund acquisition without an established lifetime value (LTV) [00:29:19].
- Take "big swings" initially when price testing (e.g., testing $59.99 vs. $69.99 rather than $1 variations), and refine to closer increments once the direction is validated [00:36:36].
- When testing a new offer, duplicate the landing page or product page in Shopify to isolate traffic to a separate URL, rather than overwriting existing site settings [00:12:44], [00:30:56].
- An offer test must run inside Meta Ads for a minimum of 7 days before evaluating performance [00:15:15], [00:37:13].

## Frameworks and models
### 1. Revenue & Profit Per Session Decision Framework
The instructor uses two core metrics to determine offer viability:
- `Revenue Per Session (RPS) = AOV x Conversion Rate` [00:08:27]
  - If RPS is below $1.00: The offer is broken. The price is likely too high (killing CVR) or pricing/AOV is far too low to survive US ad costs [00:26:04].
  - If RPS is between $1.00 and $2.00: Performance is approaching viability, but needs bundling or offer tweaks to reach safety [00:27:28].
  - Target RPS: $2.00 to $3.00+ for the US market (ensures profitability when CPC is $1.00–$2.40) [00:08:52], [00:27:35].
- `Profit Per Session (PPS) = RPS x Margin %` [00:16:59]
  - Used to verify whether higher revenue per session actually yields more bottom-line cash after factoring in product discounts and COGS [00:17:21].

### 2. Offer Strategy Types
- **Bundle & Save (Highest Recommendation):** Group commonly purchased items or multi-packs (e.g., 1, 2, 3 or 2, 4, 6 units). Always provide a logical reason and a unique name for the bundle [00:00:40], [00:14:25].
- **Buy X Get X Free (Highly Recommended):** BOGO (Buy 1 Get 1 Free), Buy 2 Get 1 Free, or Buy 2 Get 3 Free. Highly effective when volume allows supplier cost reductions [00:18:04], [00:20:30].
- **Buy X Get X% Off:** Recommended when margins are too tight to support straight free product discounts (e.g., Buy 2 get 20% off, Buy 3 get 30% off) [00:14:20], [00:20:54].
- **$X Amount Off:** Direct dollar discount leveraging the "law of large numbers" (e.g., "Save $20", "Save $80 sitewide") [00:00:45], [00:14:30].
- **Free Gift (Add-On Only):** Complimentary product, mystery gift, or dream-outcome eBook used as an order-value incentive rather than the core front-end hook [00:21:10].
- **Free Shipping (Add-On Only):** Threshold-based (e.g., free shipping over $95 or $120) or storewide incentive to raise basket size [00:04:22], [00:34:30].

### 3. Native Shopify Product Offer Duplication Process
For brands not using third-party landing page builders:
1. Navigate to Shopify Admin > Products and duplicate the hero product [00:31:02].
2. Set product details, new offer pricing, and draft status [00:31:10].
3. Go to Online Store > Themes > Customize [00:31:25].
4. Under the Products template dropdown, select "Create template" (e.g., named `eam-tester`) based on the default product template [00:31:35].
5. Customize the template blocks and copy to reflect the specific bundle or promo [00:31:40].
6. In the Shopify product admin, assign the newly created theme template to the duplicated product and publish [00:31:55].
7. Copy the published live URL (never the preview URL) and use it as the destination URL in Meta Ads [00:32:32].

## Numbers, benchmarks and rules of thumb
- **Margin Floor:** Never allow margins to drop below 50% under any circumstance; keep baseline margins above 60% whenever possible [00:04:45], [00:18:28], [00:19:10].
- **Revenue Per Session Targets (US Market):** Target $2.00+ minimum; $2.50 to $3.00 is ideal [00:08:52], [00:27:35].
- **Standard Gateway Fees Formula:** 3% of order value + $0.03 [00:04:18].
- **Testing Duration:** Test landing page and offer variations for a minimum of 7 days before turning them off or deciding winners [00:15:15], [00:37:13]. (Note: The visual notes mention a testing duration guideline of minimum 3 days, standard 7 days, maximum 14 days [00:13:20]).
- **Creative Testing Budget Formula:** Total ad sets = `Budget / Target CPA` (e.g., $100 budget / $20 TCPA = maximum 5 ad sets/concepts) [00:13:20].

## Tools and resources mentioned
- **The Offer Creation Sheet:** `https://docs.google.com/spreadsheets/d/16QG7kI0vYGvJm7w90-0dO40Ekt5aVzwrKtcSwpL_QsU/edit?usp=sharing` (alternative URL shown on screen: `https://docs.google.com/spreadsheets/d/1wWq4rkL29SkqajwNnbtB1kGgIUnYs_IgNNrhXfDuL1o/edit?usp=sharing` [00:12:55]).
- **PageDeck:** Landing page builder recommended by the course (`https://www.pagedeck.com/?via=easya`), using discount code `EASYA15` (or `EASY15`) for 15% off [00:12:55], [00:22:35].
- **Kaching Apps:** Bundle tool app recommended for standard Shopify stores (`https://www.kachingappz.com/`) [00:32:09].
- **GemPages:** Alternative landing page builder mentioned [00:35:00].
- **Claude:** AI tool suggested for generating offer ideas based on margin inputs [00:33:01].
- **Triple Whale / TrueProfit:** Profit-tracking apps mentioned as unreliable compared to bank reconciliation because they do not track true cash in/out [00:06:53].

## Exercises and action items assigned
1. Fill out the "Origins - NEW Margin & Offer Breakdown" sheet with current product COGS, exact supplier shipping costs, and gateway fees [00:04:07], [00:06:15].
2. Identify current baseline AOV and Conversion Rate in Meta Ads Manager to compute current Revenue Per Session [00:10:16].
3. Model at least three offer variations in the sheet: a tiered bundle (e.g., 1, 2, 3 units), a price test, and a value-add offer (e.g., BOGO or Buy 2 Get 1 Free) [00:12:22], [00:24:00], [00:27:58].
4. Verify that each proposed offer maintains at least a 60% margin and a viable Break-Even ROAS / Target CPA [00:04:45], [00:05:20].
5. Duplicate the product page in Shopify or build a duplicate landing page in PageDeck [00:31:02].
6. Set up a separate ad set targeting the new offer URL in Meta Ads and test for at least 7 days [00:13:01], [00:37:13].

## On-screen material worth reviewing
- **[00:00:40] Bundle & Save Framework:** Visual definitions, naming conventions, and pricing examples for bundle offers.
- **[00:00:50] & [00:05:25] Margin & Offer Breakdown Sheet:** The primary template layout displaying Gateway fees, Total Cost, Break-Even ROAS, and Target CPA formulas.
- **[00:08:35] Revenue Per Session Calculator:** The BEFORE vs. AFTER comparison table demonstrating how CVR and AOV combine to affect session value.
- **[00:10:45] Meta Ads Manager Custom Columns Preset:** Demonstration of the `EAM($)` column setup displaying purchases conversion value, ROAS, custom CVR, AOV, landing page views, link clicks, and CPC.
- **[00:13:20] Creative Testing Guidelines Doc:** Rules governing maximum ad sets (`Budget / TCPA`) and 7-day test evaluation timelines.
- **[00:17:55] & [00:25:20] Revenue & Profit Per Session Models:** The exact formulas and spreadsheet outputs showing how margin drops impact PPS.
- **[00:24:00] Tiered Bundle Calculations:** Live spreadsheet configuration of 1x, 2x (20% off), and 3x (30% off) multi-packs.
- **[00:31:35] - [00:32:30] Shopify Duplication & Template Workflow:** Step-by-step walkthrough of creating and assigning a new product template without disrupting the main live store.
