# 70. FB Asset Structure to Prevent Getting Rekt - Summary

> AI-generated summary of the course lesson (gemini-3.8-flash), written from [transcript.md](transcript.md) and [visual notes](visual_notes.md). It describes what the course teaches; it is not a transcript and not a decision for any business. Check timestamps in the transcript before relying on a claim.

## Overview
This lesson outlines an asset isolation architecture for Facebook Business Managers to protect advertising assets (pixels, ad accounts, and pages) from platform ban waves. It teaches advertisers how to distribute permissions and asset ownership across either two or three Business Managers using real personal profiles. The guidance is targeted at new advertisers, dropshippers, and brand founders looking to avoid catastrophic loss of ad spend, pixels, or account access.

## Key teachings
- Facebook account bans are extremely common regardless of whether an advertiser runs dropshipping or a new brand [00:00:04].
- Avoid purchasing aged Facebook assets from third-party sellers due to high risks of bans, account hacking, and ad budget theft [00:00:46].
- Use genuine personal profiles belonging to yourself, friends, or family members (e.g., parents, siblings) to secure legitimate asset ownership [00:00:52].
- Maintain at least three real user profiles as full admins across all Business Managers (BMs) so that if one profile gets banned, administrative access is not permanently lost [00:00:34], [00:04:16].
- Host all pixels inside a dedicated "Pixel Only" Business Manager, regardless of how many stores are being run [00:01:40].
- Facebook pixels do not need to be warmed up before use (lesson page text).
- Facebook pages should not be created at the Business Manager level; they must be created at the individual profile level [00:03:52].
- Isolating assets prevents total operational shutdown: if an ad account or holding BM gets banned, the primary pixel data remains intact [00:02:54].

## Frameworks and models
### Facebook Asset Structure Architecture
The instructor presents two variations depending on company incorporation status [00:01:35], [00:02:00]:

#### Variation A: 3-BM Setup (Unincorporated Businesses)
- **BM 1 (Pixel BM):** Houses the pixels only. No ads are run directly from this BM [00:01:40].
- **BM 2 (Holding BM):** Contains no original assets. Pixels from BM 1 and ad accounts from BM 3 are shared into BM 2, where all ads are actively run [00:02:35].
- **BM 3 (Ad Account BM):** Hosts the ad accounts and shares them into the Holding BM [00:02:43].
- **Profile Layer:** 3+ real personal profiles added as admins across all three BMs [00:01:34].

#### Variation B: 2-BM Setup (Verified / Incorporated Businesses)
Used if the business has an incorporated entity (e.g., LLC or LTD) to verify the Business Manager [00:02:07]:
- **BM 1 (Pixel BM):** Houses all pixels exclusively [00:03:40].
- **BM 2 (Verified Ad Account BM):** Verified via company documents. Hosts the ad accounts and runs the ads directly; holding BM is eliminated [00:02:14], [00:03:25].
- **Profile Layer:** 3+ real personal profiles added as admins across both BMs [00:04:07].

## Numbers, benchmarks and rules of thumb
- **3+ Real Profiles:** The minimum number of personal administrator profiles required across every Business Manager [00:00:34], [00:01:35].
- **2 to 3 Business Managers:** The standard setup required to safeguard assets (3 BMs if unverified, 2 BMs if verified with an incorporated entity) [00:00:27], [00:02:00].

## Tools and resources mentioned
- **Facebook Business Manager (BM):** Infrastructure tool for managing pages, pixels, and ad accounts [00:00:27].
- **Legal Business Entities (LLC / LTD):** Used to complete Business Manager verification, which unlocks higher ad account limits and higher daily spend limits [00:02:07].

## Exercises and action items assigned
- Gather at least three real Facebook profiles from personal contacts (self, family, or friends) to serve as administrators [00:01:19].
- Set up a dedicated "Pixel Only" Business Manager and create the tracking pixels inside it [00:01:40].
- Determine whether to use a 2-BM or 3-BM model based on whether an LLC/LTD is available for business verification [00:02:00].
- Create the business Facebook Page at the profile level rather than inside a Business Manager [00:03:52].

## On-screen material worth reviewing
- **[00:01:35] FB Asset Structure Diagram:** Visual diagram illustrating the three-BM configuration showing BM 1 ("Pixel Only"), BM 2 ("Holding BM (Optional)"), and BM 3 ("Ad Account BM"), each managed by "3+ Real Profiles".
