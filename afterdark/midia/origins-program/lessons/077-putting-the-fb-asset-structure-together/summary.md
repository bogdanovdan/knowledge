# 77. Putting The FB Asset Structure Together - Summary

> AI-generated summary of the course lesson (gemini-3.8-flash), written from [transcript.md](transcript.md) and [visual notes](visual_notes.md). It describes what the course teaches; it is not a transcript and not a decision for any business. Check timestamps in the transcript before relying on a claim.

## Overview
This lesson demonstrates how to connect and cross-share Facebook advertising assets across a 3-Business Manager (BM) structure designed to prevent loss of ad access due to account bans. The instructor guides viewers through sharing a dataset/pixel from BM 1 and an ad account from BM 3 into BM 2 (the main holding/operating BM), connecting the assets internally, and verifying asset availability inside Ads Manager. This tutorial is aimed at e-commerce store operators setting up Facebook advertising infrastructure.

## Key teachings
- Every Business Manager requires at least 3 real Facebook profiles with full admin control so that if one personal profile is banned, access to the Business Manager, ad accounts, and running campaigns is not lost [00:00:20], [00:01:05].
- The Business Manager ID can be quickly identified and copied directly from the URL query string (`?business_id=`) in Meta Business Suite [00:01:51].
- Datasets/pixels should be shared from BM 1 to BM 2 via partner sharing with full control ("Manage events dataset") [00:02:26].
- Ad accounts created in BM 3 must be shared with BM 2 via partner sharing with full "Manage ad account" permissions [00:03:07].
- Inside the holding BM (BM 2), the newly received dataset must be explicitly linked to the shared ad account under **Connected Assets** [00:03:39].
- Profiles inside BM 2 must have assets (the shared ad account and dataset) manually assigned to them under **Users > People** before they can run campaigns [00:03:57].
- The Facebook Page does not need to be attached directly to the Business Manager; having it connected to the operating Facebook profile is sufficient to run ads from it [00:04:33], [00:05:34].
- Running ads does not strictly require a separate Instagram account; Meta can display ads on Instagram using the identity and name of the linked Facebook Page [00:05:48].
- The conversion event selected at the ad set level for e-commerce testing campaigns is always "Purchase" [00:05:22].

## Frameworks and models
### 3-BM Asset Architecture ("FB Asset Structure to Prevent Getting Rekt")
- **BM 1 (Pixel BM):** Houses the Facebook dataset/pixel only. Administered by 3+ real profiles. Shares dataset access to BM 2 [00:00:17], [00:02:14].
- **BM 2 (Holding / Operating BM):** Holds partner assets and runs ads. Administered by 3+ real profiles. Receives the dataset from BM 1 and the ad account from BM 3, links them via Connected Assets, and assigns asset permissions to user profiles [00:01:48], [00:03:39].
- **BM 3 (Ad Account BM):** Used to create and host ad accounts. Administered by 3+ real profiles. Shares ad account access with BM 2 [00:02:59], [00:03:11].

### Step-by-Step Asset Linking Workflow
1. **Retrieve BM 2 ID:** Copy the numeric string from `business_id=` in the BM 2 browser URL [00:01:51].
2. **Share Dataset from BM 1:** Go to BM 1 > *Data Sources* > *Datasets & pixels* > *Partners* > *Assign partner* > paste BM 2 ID > enable full control ("Manage events dataset") > *Assign* [00:02:14].
3. **Accept in BM 2:** Open BM 2 > *Datasets & pixels* > accept pending request and refresh [00:02:41].
4. **Share Ad Account from BM 3:** Go to BM 3 > *Accounts* > *Ad accounts* > *Partners* > *Assign partner* > paste BM 2 ID > enable "Manage ad account" > *Assign* [00:03:07].
5. **Connect Assets in BM 2:** Go to BM 2 > *Data Sources* > *Datasets & pixels* > *Connected Assets* > attach the shared ad account to the dataset [00:03:39].
6. **Assign People in BM 2:** Go to BM 2 > *Users* > *People* > select profile > *Assign assets* > grant full control of the ad account and dataset [00:03:57].

## Numbers, benchmarks and rules of thumb
- Always maintain at least 3 real Facebook profiles on every Business Manager [00:00:20], [00:01:33].

## Tools and resources mentioned
- **Meta Business Suite / Business Manager:** Platform used for managing business assets, user permissions, and partner sharing [00:00:25].
- **Meta Ads Manager:** Tool used for creating campaigns and configuring ad sets [00:04:45].
- **Shopify:** Mentioned for native setup and synchronization of the Facebook pixel [00:01:38], [00:05:27].

## Exercises and action items assigned
- Invite 3 or more real Facebook profiles into your Business Manager and assign them full admin access [00:00:26].
- Copy your Business Manager ID from BM 2 and assign it as a partner to your dataset in BM 1 and your ad account in BM 3 [00:01:51], [00:03:11].
- In BM 2, link the dataset to the shared ad account under *Connected Assets* [00:03:43].
- Assign the shared dataset and ad account to your user profile under BM 2 *People* settings [00:04:03].

## On-screen material worth reviewing
- **[00:00:10] & [00:06:15] FB Asset Structure diagram overview:** Shows the three-BM layout (BM 1 Pixel Only, BM 2, BM 3 Ad Account BM, each with 3+ Real Profiles) and notes on warming assets.
- **[00:02:05] Copying business ID from URL:** Illustrates extracting the exact Business Manager ID directly from the browser address bar.
- **[00:02:35] Share dataset with partner modal:** Displays partner ID entry and toggle selection for full "Manage events dataset" control.
- **[00:04:25] Select assets and assign permissions modal:** Details assigning both the shared ad account and the dataset to the internal profile.
