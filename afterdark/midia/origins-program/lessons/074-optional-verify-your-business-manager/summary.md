# 74. (Optional) Verify your Business Manager - Summary

> AI-generated summary of the course lesson (gemini-3.8-flash), written from [transcript.md](transcript.md) and [visual notes](visual_notes.md). It describes what the course teaches; it is not a transcript and not a decision for any business. Check timestamps in the transcript before relying on a claim.

## Overview
This lesson explains a workaround method to unlock and trigger Meta Business Manager verification when the "Start verification" button is grayed out or missing in the Security Center [00:00:00]. It guides media buyers and agency operators through creating a dummy app in Meta for Developers to force verification eligibility, instructing clients to submit their details, and cleaning up the app afterward [00:00:30, 00:03:30, 00:04:13].

## Key teachings
- If the option to start verification is not visible under `business.facebook.com/settings` > Security Center, creating a dummy developer app acts as a workaround to enable the button [00:00:10, 00:00:30].
- When creating the dummy app, choose the "Instant Games" type and fill out dummy text for the display name, tagline, description, and category [00:00:45, 00:01:20].
- Under the app's Basic Settings, entering a placeholder URL (such as `www.google.com`) for both the Privacy Policy and Terms of Service satisfies the system requirements [00:02:00].
- The app icon requires an image sized exactly 1024x1024 pixels (or between 512x512 and 1024x1024 pixels) before changes can be saved to unlock verification [00:02:16, 00:02:40].
- Once the app settings are saved, the "Start verification" button activates in both Meta for Developers and the Business Manager Security Center [00:03:04, 00:03:18].
- Clients must fill in all legal details in the Business Info section and complete the verification prompt with their organization's documentation [00:03:45].
- Only delete/remove the dummy app after the Business Manager status displays as fully verified; deleting it prematurely can cause issues [00:04:20, 00:04:34].

## Frameworks and models
### Developer App Verification Workaround
1. **Navigate to Apps:** In Business Settings (`business.facebook.com/settings`), go to *Accounts* > *Apps* [00:00:30].
2. **Create New App:** Click *Add* > *Create a New App ID*, select *Instant Games*, and name the app (e.g., "For Verif") [00:00:38, 00:00:53].
3. **Configure Product Details:** Set up Instant Games, agree to terms, and fill out basic placeholder text (tagline, description, category) [00:01:05, 00:01:25].
4. **Fill App Basic Settings:** 
   - Navigate to *Settings* > *Basic* [00:01:53].
   - Enter `www.google.com` as the Privacy Policy URL and Terms of Service URL [00:02:00].
   - Upload a square icon sized 1024x1024 pixels [00:02:16, 00:02:40].
   - Click *Save Changes* [00:03:04].
5. **Direct the Client to Verify:**
   - Confirm "Start verification" is active in *Security Center* [00:03:18].
   - Instruct the client to complete all fields in *Business Info* and run through the verification flow [00:03:45].
6. **Clean Up:**
   - Wait until Business Info shows the status as officially "Verified" [00:04:13, 00:04:45].
   - Return to *Accounts* > *Apps* and click *Remove* on the dummy app [00:04:20].

## Numbers, benchmarks and rules of thumb
- **Image dimensions:** App icon must be 1024x1024 pixels (acceptable range between 512x512 and 1024x1024 pixels; 1080x1080 will fail) [00:02:16, 00:02:40].

## Tools and resources mentioned
- **Meta Business Settings:** Specifically the *Security Center*, *Accounts > Apps*, and *Business info* sections [00:00:10, 00:00:35, 00:03:45].
- **Meta for Developers:** App creation tool used to trigger the verification workflow [00:00:38].
- **Monday.com:** Mentioned as the internal platform where the instructor uploads a pre-sized 1024x1024 blue square image for students [00:02:49].
- **Google Search:** Used to grab placeholder URLs (`www.google.com`) and generic placeholder images [00:02:00, 00:02:24].

## Exercises and action items assigned
- Check the client's Meta Business Manager Security Center to see if business verification is already enabled or completed [00:00:16].
- If verification is locked, run the dummy "Instant Games" app creation process to unlock the "Start verification" button [00:00:30].
- Take screenshots of the newly enabled verification button and any blank fields in the Business Info section, then send them to the client with the Security Center link to complete [00:03:33, 00:03:50].
- Verify that the Business Manager displays "Verified" before going to *Accounts > Apps* and removing the dummy app [00:04:20, 00:04:45].

## On-screen material worth reviewing
- **[00:02:15]** Meta for Developers - App Basic Settings: View of the required fields (Privacy Policy URL, Terms of Service URL, category) before saving.
- **[00:03:10]** Meta for Developers - Verification Section: Shows the "Start Verification" button becoming active once app details are saved.
- **[00:03:25]** Meta Business Settings Security Center: Shows the unlocked "Eligible for verification" status and "Start verification" button.
- **[00:04:50]** Meta Business Info - Verified Business Details: Example screen displaying a fully verified account with completed legal business name, address, tax ID, and verified status date.
