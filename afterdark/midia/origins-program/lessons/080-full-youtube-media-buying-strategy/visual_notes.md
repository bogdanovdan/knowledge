# 80. Full YouTube media buying strategy - Visual notes

- **Frames kept:** 160 of 516 visually distinct candidates (sampled from keyframes every ~5 s, de-duplicated)
- **Resolution:** 1280x720 (native), PNG frames in Google Drive as [080-full-youtube-media-buying-strategy-frames.zip](https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)
- **Described with:** gemini-3.8-flash (Gemini API), checked against [the transcript](transcript.md)

> **On screen** records what the frame shows. **Not in transcript** lists information that is visible but not said aloud nearby. AI-generated: verify important figures against the frame.

## [00:00:03] Meta Ads Manager dashboard showing ad spend and ROAS

frame: 080_00-00-03.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager interface:
- Date range: Last 30 days: Apr 20, 2025 – May 19, 2025
- Amount spent: $2,231,570.60 (hover tooltip shows Total spent: $2,231,570.56)
- ROAS: 2.69 [2]
- Tooltip note: '[2] To provide a more complete view of your performance, we may use statistical modeling where conversion data may be missing or partial, likely due to industry or regulatory changes. Learn more'

**Not in transcript:**

Date range: Apr 20, 2025 – May 19, 2025; Exact spend: $2,231,570.60; ROAS: 2.69; Meta statistical modeling disclaimer footnote.

## [00:00:29] Graphic displaying revenue figure

frame: 080_00-00-29.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*other*

**On screen:**

Glowing green button showing amount: $11,976,442 with cursor icon next to it.

**Not in transcript:**

$11,976,442

## [00:01:02] Topic overview cards

frame: 080_00-01-02.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*slide*

**On screen:**

Card topics displayed in motion:
- [Ho]w to [pro]perly [creati]ve test
- How to scale

## [00:02:16] Blank Meta Ads Manager Setup Interface

frame: 080_00-02-16.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager dashboard:
- Active tab: Campaigns (1 selected), Ad sets (1 selected), Ads (3 selected)
- Date range: Last 30 days: Apr 20, 2025 - May 19, 2025
- Selected campaign: 'New Sales Campaign' (Toggle: Off, status line with dashes for Purchases, Cost per purchase, Purchase ROAS, CVR)
- Columns configuration: 'EAM ($)'
- Table headers visible: Off / On, Campaign, Purchases, Cost per purchase, Purchases conversion..., Purchase ROAS (return on ad..., CVR, Average purchases..., Hook Rate

**Not in transcript:**

Date range set to 'Last 30 days: Apr 20, 2025 - May 19, 2025'; custom column preset name 'EAM ($)'; campaign name 'New Sales Campaign'.

## [00:04:10] Configuring customized reporting columns in Meta Ads Manager

frame: 080_00-04-10.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager custom column settings dialog titled 'EAM ($)':
- Search bar: 'Search for metrics or column settings'
- Tabs: All, Recently used, Custom
- Left side categories: Performance (7 selected), Ad relevance diagnostics, Cost (2 selected), Performance funnel, Engagement (Page post, Calling, Messaging, Media [1 selected])
- Right panel: '30 columns selected' (Drag and drop to arrange columns):
  - Reach
  - Impressions
  - CPM (cost per 1,000 impressions)
  - Link clicks
  - CPC (cost per link click)
  - CTR (link click-through rate)
  - Results
  - Cost per result
  - Purchases

**Not in transcript:**

Preset name 'EAM ($)'; category list on the left with selection counts; right panel showing exactly 30 columns selected and order of visible items (Reach, Impressions, CPM, Link clicks, CPC, CTR, Results, Cost per result, Purchases).

## [00:04:33] Custom metrics list and CVR metric definition in Ads Manager

frame: 080_00-04-33.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Custom column preset dialog under 'Custom' tab:
- Custom metrics checklist:
  - OBC>LP
  - AOV
  - Actual profit
  - Purchase CVR
  - Video Hook
  - LP>ATC
  - CVR (Unique Clicks)
  - AOV
  - CVR (Checked)
  - EPC
  - NC ROAS (Warroad)
- Tooltip for CVR:
  - Title: CVR (Created by Shaun Eng)
  - Formula: Purchases ÷ Landing page views
- Selected column list on the right (top items):
  - Campaign name
  - Ad Set Name
  - Attribution setting
  - Bid strategy
  - Budget
  - Amount spent
  - Reach
  - Impressions
  - CPM (cost per 1,000 impressions)
  - Link clicks

**Not in transcript:**

Metric creator name 'Shaun Eng'; specific custom metric names in list (OBC>LP, Actual profit, Video Hook, LP>ATC, EPC, NC ROAS (Warroad)); right column ordering starting with Campaign name, Ad Set Name, Attribution setting, Bid strategy, Budget, Amount spent.

## [00:04:58] Creating custom metric Purchase CVR formula setup

frame: 080_00-04-58.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Create custom metric modal:
- Formula editor: Purchases ÷ Landing page views
- Name: Purchase CVR (12/100)
- Format: Percentage (%)
- Description: Optional (0/350)
- Who can access this?: 'Only you' selected (options: 'Only you - You'll be able to see, edit and delete this custom metric...', 'Everyone with access to this Business')
- 'Try popular custom formulas' sidebar suggestions:
  - Impressions to 3-second video plays rate
  - Impressions to post engagements rate
  - Link clicks to landing page views rate
  - Video plays to link clicks rate
  - Link clicks to purchases rate

**Not in transcript:**

Character limit for Name (12/100); Description field (0/350); popular custom formula suggestions on the right side panel.

## [00:06:06] Renaming Ad Set inline in Meta Ads Manager

frame: 080_00-06-06.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager showing the 'Ad sets' tab with an inline rename pop-up:
- Original Name: 'New Sales Ad Set'
- Input Name: 'Broad Adset Women - 35+'
- Visible Columns: Video Hold, Video average play time, Excluded custom audiences, Included custom audiences, Audience gender (Ad set settings) ['All'], Audience location (Ad se...) ['CA'], Audience age (Ad set settings) ['18 - 65']

**Not in transcript:**

Location targeting is set to 'CA'. Buttons: 'Cancel', 'Save to draft'.

## [00:06:28] Ad Set editing view in Meta Ads Manager

frame: 080_00-06-28.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager editor panel:
- Left tree: New Sales Campaign > Broad Adset Women - 35+ > New Sales Ad, New Sales Ad - Copy, New Sales Ad - Copy 2
- Main panel fields:
  - Ad set name: 'Broad Adset Women - 35+'
  - Conversion
  - Dynamic creative: Off (Notice: 'Dynamic creative will be going away soon')
  - Budget & schedule
- Audience definition panel: 'Your audience is broad.'

**Not in transcript:**

Shows the campaign hierarchy tree on the left and dynamic creative deprecation warning notice.

## [00:07:33] Ads tab reporting columns in Meta Ads Manager

frame: 080_00-07-33.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager 'Ads' tab with 3 selected ads:
- Rows: 'New Sales Ad', 'New Sales Ad - Copy 2', 'New Sales Ad - Copy'
- Columns: Off / On, Ad, Bid strategy ('Highest volume / Conversions'), Budget ('Using campaign...'), Amount spent, Reach, Impressions, CPM (cost per 1,000...), Link clicks, CPC (cost per link click)
- Date range: 'Last 30 days: Apr 20, 2025 - May 19, 2025'

**Not in transcript:**

Column metrics setup for ad-level view including CPM and CPC columns.

## [00:07:52] Topic slide: Naming Schemes

frame: 080_00-07-52.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*title card*

**On screen:**

Stylized graphic card on pink background:
'Naming Schemes'

## [00:08:04] Custom report view showing account spend and ROAS

frame: 080_00-08-04.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager reporting table:
- Amount spent: $2,231,570.60 (Total spent: $2,231,570.56)
- ROAS: 2.69 [2]

**Not in transcript:**

Exact total spend ($2,231,570.60) and ROAS (2.69) visible in pivot table view.

## [00:09:44] Professor Charley T Twitter/X profile callout

frame: 080_00-09-44.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*social post*

**On screen:**

Twitter / X Profile overlay:
Professor Charley T | The Facebook Ads Guy (@CTTheDisrupter)
Bio: Facebook Top 100 Advertiser | Creator of the 3:2:2 Method, PSM and 4Pi - $1B+ in revenue - Godfather of Broad | Founder @DisrupterSchool & Disrupter Enterprises
Location: Atwater Village, CA | Website: DisrupterSchool.com
Joined July 2020 | 6,228 Following | 18.6K Followers

**Not in transcript:**

@CTTheDisrupter handle, bio text mentioning 'Creator of the 3:2:2 Method, PSM and 4Pi - $1B+ in revenue - Godfather of Broad', DisrupterSchool.com link, 18.6K followers count.

## [00:10:32] Meta Ads Manager campaign creation objective selection

frame: 080_00-10-32.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager interface showing campaign setup:
- Campaign details -> Buying type: Auction
- Campaign objective: Sales (selected)
Other options listed: Awareness, Traffic, Engagement, Leads, App promotion
- Left sidebar tree structure: New Sales Campaign -> Broad Adset Women - 35+ -> New Sales Ad, New Sales Ad - Copy, New Sales Ad - Copy 2

**Not in transcript:**

Left sidebar structure shows ad set named 'Broad Adset Women - 35+' and ads 'New Sales Ad - Copy', 'New Sales Ad - Copy 2'.

## [00:10:41] Choose a campaign setup modal in Meta Ads Manager

frame: 080_00-10-41.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Modal dialog 'Choose a campaign setup':
- Advantage+ shopping campaign (Streamlined, Tailored, Best practices)
- Manual sales campaign (Selected, highlighted in blue, 'Create a sales campaign from scratch using the standard setup.')
Buttons: 'Back', 'Continue'

**Not in transcript:**

Text for Advantage+ shopping campaign: 'Maximize performance and reach valuable audiences with a simplified setup. Preset settings include placements, age and more.'

## [00:10:48] New campaign level settings options in Meta Ads Manager

frame: 080_00-10-48.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager Campaign setup page:
- Campaign name: New Sales Campaign
- Campaign details: Buying type: Auction, Campaign objective: Sales
- Advantage+ catalog ads: Off toggle
- Advantage campaign budget: Off toggle
- A/B test: Off toggle
- Audience segment reporting

**Not in transcript:**

Explaining text under Advantage campaign budget: 'Distribute your budget across ad sets to get more results. You can control spending for each ad set.'

## [00:11:16] Renamed campaign settings overview in Meta Ads Manager

frame: 080_00-11-16.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager showing campaign header renamed to: EAM//Acquisition//US//CBO
Settings visible:
- Campaign spending limit: None added
- Advantage+ catalog ads: Off
- Advantage campaign budget: Off
- A/B test: Off
- Audience segment reporting (Engaged audience, Existing customers)
- Special Ad Categories

**Not in transcript:**

Exact campaign naming string shown: 'EAM//Acquisition//US//CBO'.

## [00:11:20] Enabling Advantage campaign budget (CBO) settings

frame: 080_00-11-20.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager Campaign settings:
- Advantage campaign budget: On toggle enabled
- Budget: Daily budget dropdown, value: $ 20.00 CAD
- Explanatory note: 'You'll spend an average of $20.00 per day. Your maximum daily spend is $35.00 and your maximum weekly spend is $140.00.'
- Campaign bid strategy: Highest volume or value
- Budget scheduling option (Schedule budget increases)

**Not in transcript:**

Daily budget default shown as $20.00 CAD, max daily spend $35.00, weekly max $140.00, Campaign bid strategy default 'Highest volume or value'.

## [00:11:25] Campaign testing rules and FAQ notes document

frame: 080_00-11-25.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*document*

**On screen:**

Notes document:
To Sum Up:
1 Campaign
1 Champions Ad set, Multiple Creative Test Ad Sets
3 creatives in each ad set (same concept), each with 2 headlines and 2 copies

WARNING DO NOT TURN OFF YOUR EXISTING ADS IF THEY ARE WORKING...

FAQ:
1. How many creative ad sets can you launch at a time?
- If you're only spending few hundred a day, I recommend keeping it to 5 ad sets...
- You can launch all 5 ad sets in the same day if you wish
- If you're spending a few thousand a day you can definitely have more ad sets
2. Do we set min/max spend limits for this campaign method?
- No, we tested it and it didn't help.
3. How long do you test creatives for?
- We recommend testing creatives for a minimum of 3 days...
4. How do you know if a creative ad set is a winner?

**Not in transcript:**

Structure details: '1 Champions Ad set, Multiple Creative Test Ad Sets; 3 creatives in each ad set (same concept), each with 2 headlines and 2 copies'. FAQ answers about running 5 ad sets, testing for 3-7 days.

## [00:11:26] Formula for max number of creatives to test per week

frame: 080_00-11-26.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*document*

**On screen:**

Google Doc:
**How to figure out the max number of creatives to test per week:**
Example #1 - Budget $100/day
Total Budget (example $100/day)
Target CPA (Example $20)

Total Tests = Budget/TCPA

$100/$20 = 5

So max amount of concepts is 5 considering 100% of your budget is testing.
this applies to all budgets below $1,000 per day.
If your budget is above $1,000/day, you are fine to test at will.

**Not in transcript:**

Formula text and full calculation: 'Total Tests = Budget/TCPA', '$100/$20 = 5', 'max amount of concepts is 5 considering 100% of your budget is testing. this applies to all budgets below $1,000 per day. If your budget is above $1,000/day, you are fine to test at will.'

## [00:11:36] Configuring Daily Budget in Meta Advantage Campaign Budget

frame: 080_00-11-36.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager showing campaign settings for 'EAM//Acquisition//US//CBO':
- Advantage campaign budget: On (toggled on)
- Budget: Daily budget selected, input value: $20.00 CAD
- Note: 'You'll spend an average of $20.00 per day. Your maximum daily spend is $35.00 and your maximum weekly spend is $140.00.'
- Campaign bid strategy: Highest volume or value
- Budget scheduling: (Hide options) - Schedule budget increases (unchecked)
- A/B test: Off
- Warning alert on right: 'Campaign may get zero Results' with recommendation to expand audiences or increase budget.

**Not in transcript:**

Budget value '$20.00 CAD', text stating maximum daily spend is $35.00 and weekly spend is $140.00, Campaign bid strategy set to 'Highest volume or value', warning box 'Campaign may get zero Results'.

## [00:16:00] Configuring Daily Budget and Campaign Bid Strategy in Meta Ads Manager

frame: 080_00-16-00.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager campaign creation UI:
- Advantage campaign budget +: On
- Budget: Daily budget, $200.00 CAD
- Note: 'You'll spend an average of $200.00 per day. Your maximum daily spend is $350.00 and your maximum weekly spend is $1,400.00.'
- Campaign bid strategy: Highest volume or value
- Budget scheduling: Increase your budget during specific days or times (Schedule budget increases unchecked)
- A/B test: Off
- Audience segment reporting: Define your ad account's audience segments in Advertiser settings... (Engaged audience: Not defined, Existing customers: Not defined)

**Not in transcript:**

CAD currency specification; Budget scheduling checkbox; A/B test set to Off; Audience segment reporting section details.

## [00:16:48] Campaign bid strategy dropdown selected in Meta Ads Manager

frame: 080_00-16-48.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager interface showing:
- Campaign bid strategy: 'How we'll bid in ad auctions.' with dropdown set to 'Highest volume or value'
- Advantage campaign budget +: On
- Budget: Daily budget $200.00 CAD (Max daily: $350.00, Max weekly: $1,400.00)

**Not in transcript:**

Text label below Campaign bid strategy: 'How we'll bid in ad auctions.'

## [00:19:16] Audience segment reporting and special ad categories in Meta Ads Manager

frame: 080_00-19-16.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager campaign settings showing:
- Budget scheduling: 'Schedule budget increases'
- A/B test: Off
- Audience segment reporting: 'Define your ad account's audience segments in Advertiser settings to receive reporting breakdowns between your new audience, engaged audience and existing customers.'
  - Engaged audience: Not defined
  - Existing customers: Not defined
- Special Ad Categories: 'Declare if your ads are related to financial products and services...'

**Not in transcript:**

Budget scheduling option, A/B test toggle setting (Off), Special Ad Categories section.

## [00:19:23] Navigating to Audiences from Ads Manager side menu

frame: 080_00-19-23.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager left sidebar navigation menu expanded:
- Account Overview
- Campaigns
- Ads Reporting
- Audiences (cursor hovering)
- Advertising settings
- Billing & payments
- Events Manager
- All tools

**Not in transcript:**

Account Overview, Ads Reporting, Advertising settings, Billing & payments, Events Manager menu items.

## [00:19:27] Choosing a custom audience source in Meta Audiences

frame: 080_00-19-27.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Modal popup: 'Choose a custom audience source'
Connect with people who have already shown an interest in your business or product.
Your sources:
- Website
- Customer list
- App activity
- Offline activity
- Catalog
Meta sources:
- Video
- Instagram account
- Lead form
- Events
- Instant Experience
- Facebook page
- Shopping
- On-Facebook listings
Buttons: Cancel, Next

**Not in transcript:**

Full list of sources including App activity, Offline activity, Catalog, Video, Instagram account, Lead form, Events, Instant Experience, Facebook page, Shopping, On-Facebook listings.

## [00:19:33] Create a website custom audience modal in Meta Ads

frame: 080_00-19-33.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Modal popup: 'Create a website custom audience'
Include Accounts Center accounts who meet Any of the following criteria:
- Buttons: 'Include more people', 'Exclude people'
- Audience Name (0/50)
- Description • Optional (0/100)
Buttons: Back, Create audience

**Not in transcript:**

Criteria dropdown ('Any'), character limits (0/50, 0/100), buttons 'Include more people', 'Exclude people'.

## [00:19:55] Prepare customer list guidelines table in Meta Ads

frame: 080_00-19-55.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Modal: 'Create audience from a list' > 'Prepare customer list'
Steps on left: Prepare list, Add list, Match columns, Upload, Confirmation
Action buttons: 'Download file template', 'Import from Mailchimp'
Main identifiers formatting table:
- Identifier: Email | Column header: email | Formatting guidelines: We accept email addresses in up to three separate columns... | Examples: Emily@example.com, John@example.com, Helena@example.com
- Identifier: Phone number | Column header: phone | Formatting guidelines: Phone numbers must include a country code...

**Not in transcript:**

Step tracker (Add list, Match columns, Upload, Confirmation), Import from Mailchimp button, Download file template button, exact formatting guidelines and examples for Email and Phone number.

## [00:21:02] Configuring ad level with existing post in Meta Ads Manager

frame: 080_00-21-02.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager ad edit screen for 'Champions Adset > Best Ads':
- Instagram account: easya_media
- Threads profile: Create profile
- Ad setup: Dropdown selected 'Use existing post'
- Multi-advertiser ads checkbox
- Ad sources: Catalog (Not connected), Source URL, Site Links
- Ad preview pane on the right

**Not in transcript:**

Instagram account handle easya_media, Threads profile option, Multi-advertiser ads checkbox, Catalog / Source URL input fields.

## [00:21:12] Finding Facebook Ads Post ID tutorial reference

frame: 080_00-21-12.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*social post* | legibility: partly legible

**On screen:**

Picture-in-picture overlay showing a YouTube video screenshot titled: 'How To Find a Facebook Ads Post ID In 90 Seconds' by Spencer Pawliw.
The screen displays an ad preview titled "EasyA's Post" with a highlighted date/timestamp link used to locate the post ID, along with ad copy starting: 'Your FB ads performance is stuck in 2019 While you're...'.

**Not in transcript:**

Channel name 'Spencer Pawliw', video title 'How To Find a Facebook Ads Post ID In 90 Seconds', visual indicator highlighting the timestamp link on EasyA's post.

## [00:21:33] Ad set conversion location and performance goal configuration

frame: 080_00-21-33.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager ad set configuration:
- Ad set name: 'Champions Adset'
- Conversion location: 'Website' (selected) - 'Drive sales and conversions on your website.'
- Other unselected conversion options: Website and shop, App, Website and app, Message destinations, Calls, Website and calls.
- Performance goal: 'Maximize number of conversions'
- Dataset: 'EAM-YOUTUBE'
- Left hierarchy sidebar shows: 'Champions Adset' with sub-item 'Best Ads'.

**Not in transcript:**

Dataset name: 'EAM-YOUTUBE'; campaign naming hierarchy: 'EAM//Acquisition//US//CBO > Champions Adset > 1 Ad'.

## [00:22:27] Standard attribution window settings in Meta Ads Manager

frame: 080_00-22-27.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager Attribution setting:
- Standard attribution (selected): 'Optimize delivery for a selected time window and interaction type.'
- Incremental attribution: 'Optimize delivery for incremental conversions using sophisticated models...'
- Note: '1-day engaged-view is now selected by default to help maximize your campaign performance.'
Standard attribution selections:
- Click-through: 7 days
- Engaged-view (For video only): 1 day
- View-through: 1 day
- Dynamic creative: Off ('Dynamic creative will be going away soon...')

**Not in transcript:**

View-through default setting visible as '1 day'. Notice stating dynamic creative will be going away soon.

## [00:23:09] Click-through attribution options dropdown in Meta Ads Manager

frame: 080_00-23-09.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager - Standard attribution selections:
- Click-through dropdown open displaying options:
  • 1 day (selected)
  • 7 days
- Engaged-view (For video only): [hidden / set below]
- View-through: 1 day

## [00:23:33] Meta Ads attribution settings and dynamic creative notice

frame: 080_00-23-33.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Standard attribution selections:
Click-through: 7 days
Engaged-view (For video only): 1 day
View-through: 1 day

Dynamic creative: Off
Notice: 'Dynamic creative will be going away soon. Until then, using dynamic creative will enable the Flexible ad format.'

**Not in transcript:**

Dynamic creative toggle status (Off), exact text of the warning that Dynamic creative will be going away soon and transitioning to Flexible ad format.

## [00:24:43] Ad set attribution settings with view-through set to None

frame: 080_00-24-43.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager ad set editor:
Attribution setting: Standard attribution (selected)
Standard attribution selections:
Click-through: 7 days
Engaged-view (For video only): 1 day
View-through: None
Audience definition: Your audience is broad.
Estimated daily results: Not available for this campaign since it has a budget optimized across ad sets.

**Not in transcript:**

Standard attribution vs Incremental attribution radio buttons visible, campaign name EAM//Acquisition//US//CBO, ad set Champions Adset.

## [00:26:17] Attribution setting with engaged-view and view-through disabled

frame: 080_00-26-17.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager ad set configuration:
Standard attribution selections:
Click-through: 7 days
Engaged-view (For video only): None
View-through: None
Dynamic creative: Off

**Not in transcript:**

Engaged-view dropdown set to 'None' alongside View-through set to 'None'.

## [00:28:07] Audience controls setup in Meta Ads Manager

frame: 080_00-28-07.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Audience controls:
'Adjust audience controls to reflect legal or practical constraints only.'
Locations: Included location: Canada
Minimum age: 18
Exclude these custom audiences: Search existing audiences
Languages: All languages
Advantage+ audience: 'Our AI finds audiences for your ads. If you add an audience suggestion, you'll guide our AI towards people you think are likely to respond.'

**Not in transcript:**

Excluded custom audiences input field, Minimum age default (18), Languages set to 'All languages', Advantage+ audience explanation box.

## [00:29:08] Exclude custom audiences section in Meta Ads Manager

frame: 080_00-29-08.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager ad set settings: 'Exclude these custom audiences' section with a search bar showing 'Search existing audiences' and the message 'No existing audience in this account. Create a new audience to use this targeting option'. Below, Placements section is visible.

**Not in transcript:**

Campaign name: EAM//Acquisition//US//CBO; Ad set: Champions Adset; Locations: Included location: Canada; Minimum age: 18.

## [00:29:13] Audiences overview screen in Meta Ads Manager

frame: 080_00-29-13.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Audiences page showing: 'Reach the Accounts Center accounts Who Matter to You' with options to 'Create a custom audience', 'Create a lookalike audience', and 'Create a Saved Audience'.

**Not in transcript:**

Account name: EAM-YouTube (17886493...). Description text explaining Custom audiences, Lookalike audiences, and Saved Audience.

## [00:30:06] Advantage+ audience expansion notice in Meta Ads Manager

frame: 080_00-30-06.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Advantage+ audience section showing 'Detailed targeting' with an informational tooltip: 'We may deliver ads beyond your audience for eligible ad objectives, if it's likely to improve performance.' Switch to original audience options link shown below. In Placements, 'Introducing ads in Threads' banner is displayed.

**Not in transcript:**

Age: 18 - 65+, Gender: All genders. Link: 'Switch to original audience options'. Threads feed placement banner text.

## [00:31:28] Meta Ads Manager custom audience exclusions setup

frame: 080_00-31-28.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Audience configuration in Meta Ads Manager showing: 'Audience controls for this ad account', 'Advantage+ audience' prompt ('You could get 7.2% lower cost per result'), and 'Custom audiences' section with Exclude list showing: 'Website PUR 180'. Also shows alert: 'You'll need to accept the Meta Business Tools Terms before you can edit this ad set.'

**Not in transcript:**

Terms warning pop-up: 'You'll need to accept the Meta Business Tools Terms before you can edit this ad set.' Button: 'Next'. Exclude field: 'Website PUR 180'.

## [00:31:35] Expanded audience exclusions list in Meta Ads Manager

frame: 080_00-31-35.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager audience settings with Exclude list showing: 'Website PUR 180', 'PUR 30', and 'Customer List'.

**Not in transcript:**

Additional exclusion rows visible: 'PUR 30' and 'Customer List'.

## [00:32:00] Placements settings in Meta Ads Manager

frame: 080_00-32-00.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager under campaign 'EAM//Acquisition//US/CBO' and ad set 'Champions Adset'. Displays 'Detailed targeting' (empty), 'Placements' section with 'Introducing ads in Threads' notice, and 'Advantage+ placements' selected ('Your budget will be allocated by Meta's delivery system across multiple placements based on where it's likely to perform best.').

**Not in transcript:**

Breadcrumbs: 'EAM//Acquisition//US/CBO > Champions Adset > 1 Ad'. Left sidebar showing 'Champions Adset' and 'Best Ads'. Button 'Switch to original audience options'.

## [00:32:06] Duplicate ad set modal dialog

frame: 080_00-32-06.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Modal window titled 'Duplicate your ad set' with options:
- 'Select a campaign for your ad set': 'Existing campaign' (radio selected) with search input 'Select a campaign', 'New campaign'.
- 'Number of copies': '1'
Buttons: 'Cancel', 'Duplicate'.

**Not in transcript:**

Radio buttons: 'Existing campaign', 'New campaign'. Number of copies input default: 1.

## [00:32:11] Topic title card: How to properly creative test

frame: 080_00-32-11.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*title card*

**On screen:**

Pink gradient title card with a glassmorphism media player window displaying text: 'How to properly creative test'.

## [00:33:51] Creative test ad set audience exclusion setup

frame: 080_00-33-51.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager showing ad set 'Creative Test Adset #1' under campaign 'EAM//Acquisition//US/CBO'. Left panel shows 'Creative Test Adset #1' with child ad 'New Ad #1', alongside existing 'Champions Adset'. Form fields display: Minimum age: 18, Exclude these custom audiences: search field, Languages: All languages, Advantage+ audience section.

**Not in transcript:**

Ad set renamed to 'Creative Test Adset #1' with nested 'New Ad #1' showing warning icons.

## [00:35:12] Ad level identity setup in Meta Ads Manager

frame: 080_00-35-12.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager at the ad level for 'New Ad #1' within 'Creative BATCH #1 Adset'. Sections include:
- 'Ad name': 'New Ad #1'
- 'Partnership ad': Off toggle
- 'Identity': Facebook Page set to 'EasyA', Instagram account set to 'easya_media', Threads profile 'Create profile'
- 'Ad setup': 'Use existing post', Multi-advertiser ads checkbox
- 'Ad preview' panel on the right.

**Not in transcript:**

Ad set name displayed as 'Creative BATCH #1 Adset'. Facebook Page: 'EasyA'. Instagram account: 'easya_media'. 'Use existing post' selected under Ad setup.

## [00:36:25] Meta Ads Manager branding setup tooltip

frame: 080_00-36-25.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Facebook Page: EasyA. Instagram account: easya_media. Tooltip: 'We can automatically source branding from URLs you've previously used, previous ads, information from your Facebook Page and your Shopify account. We'll match the fonts and colors we find to the most relevant available options. You can edit or turn this off at any time. About branding'. Branding: Inactive [Add branding]. Ad setup: Create ad. Media setup: Manual upload.

**Not in transcript:**

Branding button text: 'Add branding', status: 'Inactive'. Ad setup selector set to 'Create ad'.

## [00:36:38] Meta Ads Manager Branding settings modal

frame: 080_00-36-38.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo* | legibility: partly legible

**On screen:**

Modal: 'Branding'. Options: Apply this branding (toggle), Logo (+), Font (No preference), Colors (+ + +). Text tone: 'Describe a tone, like "warm, informed and conversational"' 0/300. Visual style: 'Describe your visual style, like "colorful and natural"' 0/300. [Done] button.

**Not in transcript:**

Character limit 0/300 for Text tone and Visual style. Font default: 'No preference'. Input fields for Logo and Colors.

## [00:37:02] Ad format selection options in Meta Ads Manager

frame: 080_00-37-02.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Format selection:
- Flexible: 'We'll show your ad in the format we predict may perform best'
- Single image or video: 'One image or video, or a slideshow with multiple images'
- Carousel: '2 or more scrollable images or videos'
- Collection: 'Group of items that opens into a fullscreen mobile experience'
Multi-advertiser ads checkbox checked.
Ad creative: Media (0 of 10), Primary text (0 of 5).

**Not in transcript:**

Options for Single image or video, Carousel, Collection with descriptions. Media limit: 0 of 10. Primary text limit: 0 of 5.

## [00:37:32] Flexible ad preview in Meta Ads Manager

frame: 080_00-37-32.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo* | legibility: partly legible

**On screen:**

Ad preview for account 'peekaboo_pillow'. Facebook Feed preview showing multi-card carousel format automatically created from uploaded media. Ad copy: 'Say hello to Peekaboo Pillow: the easiest, coziest, and safest way to bond with your baby.' Headline: 'Make Every Moment Count...' [Shop now].

**Not in transcript:**

Account name: 'peekaboo_pillow'. Exact preview card text: 'Say hello to Peekaboo Pillow: the easiest, coziest, and safest way to bond with your baby.' CTA button: 'Shop now'.

## [00:37:43] Recommended creative scaling video reference

frame: 080_00-37-43.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo* | legibility: partly legible

**On screen:**

YouTube video overlay titled: 'How I make Facebook ads that scale to $50k/day' by Spencer Pawliw. Showing Miro/Figma board categorized by 'Messaging (TXT)', 'Imagery (IMG)', 'Hook (HOOK)', 'Hold (HOLD)'.

**Not in transcript:**

The thumbnail/video says '$50k/day' (transcript says '40k per day'). Column categories on board: Messaging (TXT), Imagery (IMG), Hook (HOOK), Hold (HOLD).

## [00:38:11] Flexible ad breakdown missing image-level spend

frame: 080_00-38-11.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager reporting table:
Ad: DCT #2_Baby/Dad Static_IMG__PP_C_H_
Results: 2 Website purchases
Cost per result: $161.95 Per Purchase
Amount spent: $323.90 Total spent
CPM: $40.95
Purchases: 2 Total
Purchases conversion value: $352.58
Purchase ROAS: 1.09

**Not in transcript:**

Exact ad name 'DCT #2_Baby/Dad Static_IMG__PP_C_H_'. Cost per result: $161.95, Total spent: $323.90, CPM: $40.95, Purchases value: $352.58, ROAS: 1.09.

## [00:38:38] Destination and browser add-on settings in Meta Ads Manager

frame: 080_00-38-38.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Website URL: easyamedia.com [Preview URL]. Display link input field. Browser add-ons: None (selected), Call, Messenger, Instagram Direct, WhatsApp, Instant form, Instant Experience, Facebook event. Ad preview showing Instagram feed ad for EasyA.

**Not in transcript:**

Browser add-on options list: None, Call, Messenger, Instagram Direct, WhatsApp, Instant form, Instant Experience, Facebook event.

## [00:38:47] Media selection modal in Meta Ads Manager

frame: 080_00-38-47.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Modal: 'Set up your creative' -> Media: 'Select or upload the media you want to use for your ad. You can select one image or video.' Tabs: All, Account, Business, Instagram, Page. Upload button. EasyA page assets shown: 1000 x 1000, 1920 x 1080.

**Not in transcript:**

Steps on left: Creative setup, Media, Crop, Text, Image generation, Enhancements. Image dimensions: 1000x1000, 1920x1080.

## [00:38:49] Selecting ad media in Meta Ads Manager

frame: 080_00-38-49.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager popup 'Media: Select or upload the media your want to use for your ad.' Displays Instagram Images options with dimensions like 1080 x 1350 and 1290 x 2293, and EasyA account images (1000 x 1000, 1920 x 1080). Tabs: All, Account, Business, Instagram, Page.

**Not in transcript:**

Image pixel dimensions displayed beneath previews: 1080 x 1350, 1290 x 2293, 1000 x 1000, 1920 x 1080.

## [00:39:12] Media crop settings for placements in Meta Ads Manager

frame: 080_00-39-12.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Modal: 'Select media crop for placements'. Checkbox enabled: 'Turn on flexible media to show media you chose for a specific aspect ratio across all placements.' Placements shown: Square (Original, 1:1), Vertical (Original, 9:16), Horizontal (Original, 1.91:1), with preview thumbnails.

**Not in transcript:**

Exact options for aspect ratios: Square (Original, 1:1), Vertical (Original, 9:16), Horizontal (Original, 1.91:1); 'Replace' and 'Crop' buttons below each thumbnail.

## [00:39:23] Vertical 9:16 aspect ratio overlay diagram

frame: 080_00-39-23.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*diagram*

**On screen:**

Graphic overlay of a tall rectangle labeled '9:16' demonstrating the full vertical story/reel frame format.

**Not in transcript:**

Visual bounding box showing vertical proportions.

## [00:39:30] 4:5 safe area inside 9:16 video overlay

frame: 080_00-39-30.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*diagram*

**On screen:**

Graphic overlay showing '9:16' vertical frame containing an inner shaded box labeled '4:5' demonstrating safe zone formatting for video feeds.

**Not in transcript:**

Visual comparison showing where the 4:5 frame sits centered within the 9:16 vertical box.

## [00:39:39] 1:1 square safe area inside 9:16 creative overlay

frame: 080_00-39-39.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*diagram*

**On screen:**

Graphic overlay showing '9:16' vertical frame containing a center square region labeled '1:1', demonstrating safe framing for square feeds from vertical images.

**Not in transcript:**

Visual representation of how the 1:1 crop aligns within the taller 9:16 boundary.

## [00:42:21] Setting multiple text and headline options in Meta Ads Manager

frame: 080_00-42-21.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager 'Set up your creative' -> 'Text' screen:
- Primary text (2 of 5): 'Best Copy #1', 'Test Copy #2'
- Headline (2 of 5): 'Best Headline #1', 'Test Headline #2'
- Description: empty
- Call to action: dropdown open with options including Book now, Buy tickets, Contact us, Download, Get offer, Get quote, Get showtimes, Learn more

**Not in transcript:**

CTA dropdown menu list visible: Book now, Buy tickets, Contact us, Download, Get offer, Get quote, Get showtimes, Learn more.

## [00:42:36] Advantage+ creative AI image generation options in Meta Ads Manager

frame: 080_00-42-36.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager 'Advantage+ creative image generation':
- Banner note: 'In our experiment, campaigns with all ads adding AI-generated images saw 11% CTR lift and 8% CVR lift'
- Image variations grid (9 AI generated stock/business images)
- Generation setup sidebar:
  - Radio options: Backgrounds / Full images (selected)
  - Button: 'Generate new images'
- Text and logo overlays:
  - Add text AI toggle: On
  - Font dropdown: 'Playfair Display'
  - Add logo toggle: On

**Not in transcript:**

Toggle options: 'Add text AI' with font selector 'Playfair Display' and input fields 'Add a short text overlay'; 'Add logo' toggle switch.

## [00:42:48] Advantage+ creative enhancements review panel

frame: 080_00-42-48.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager 'Advantage+ creative enhancements' modal (For review tab - 5 items):
1. 'Translating primary text and headline into other languages.' (Customize button, Example 1 of 4)
2. 'We'll add product tiles under your media. Customize to turn on.' (Customize button, Example 1 of 3)
3. 'We'll add 3D motion and depth to your image when it may help...'
4. 'We'll pair key phrases with your CTA and optimize CTA text.' (Customize button)
- Bottom toggle: Image animation (AI)

**Not in transcript:**

Exact labels: 'For review (5)', 'Other active enhancements (5)', 'Translating primary text and headline into other languages', 'We'll add product tiles under your media', 'We'll add 3D motion and depth to your image', 'We'll pair key phrases with your CTA and optimize CTA text', 'Image animation'.

## [00:42:54] Configuring other active creative enhancements in Meta Ads Manager

frame: 080_00-42-54.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Modal window: 'Advantage+ creative enhancements'. Tabs: 'For review (5)', 'Other active enhancements (5)' selected. Visible cards under 'Other active enhancements': 'Add overlays' (toggled ON), 'Visual touch-ups' (toggled ON), 'Music' (toggled ON, cursor hovering), 'Text improvements' (toggled ON).

**Not in transcript:**

Toggle switch state for Add overlays, Visual touch-ups, Music, and Text improvements are all initially ON.

## [00:43:18] Advantage+ creative review enhancements toggled off

frame: 080_00-43-18.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Modal: 'Advantage+ creative enhancements' under tab 'For review (5)'. Cards shown: 'Translate text' (Early release AI, toggled OFF), 'Add catalog items' (toggled OFF), '3D animation' (toggled OFF), 'Enhance CTA' (toggled OFF). Below each card are previews and 'Customize' options.

**Not in transcript:**

Detailed cards shown: 'Translate text', 'Add catalog items', '3D animation', 'Enhance CTA' all toggled off.

## [00:43:31] Disabling music and text improvements in active enhancements

frame: 080_00-43-31.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Modal: 'Advantage+ creative enhancements' under 'Other active enhancements (5)'. Active enhancements visible: 'Add overlays' (ON), 'Visual touch-ups' (ON), 'Music' (toggled OFF), 'Text improvements' (toggled OFF).

**Not in transcript:**

Demonstrates specific configuration: Music and Text improvements switched off while Add overlays and Visual touch-ups remain on.

## [00:44:13] Advantage+ creative enhancements summary status

frame: 080_00-44-13.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Section 'Advantage+ creative enhancements (2/10)': 'Turned off: Translate text, Add catalog items, Music and 5 more', 'Turned on: Add overlays, Visual touch-ups'. Sections below: 'Event details - Optional', 'Languages' (Off), 'Tracking'.

**Not in transcript:**

Shows summary ratio (2/10 enhancements active) and exact status text.

## [00:44:21] Advantage+ creative advanced preview settings overview

frame: 080_00-44-21.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Modal: 'Advanced preview' > 'Advantage+ creative'. Shows enhancements: 'Text improvements' (OFF), 'Enhance CTA' (OFF), 'Add site links' (OFF), 'Image animation' (OFF with 'Your image isn't eligible for image animation').

**Not in transcript:**

'Image animation' status displays 'Your image isn't eligible for image animation'.

## [00:45:31] Ad setup overview and identity settings in Meta Ads Manager

frame: 080_00-45-31.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager interface showing:
- Campaign hierarchy: EAM//Acquisition//US/CBO > Creative BATCH #1 Adset > New Ad #1
- Ad name: New Ad #1 (with 'Create template' button)
- Partnership ad: Toggle set to Off
- Identity section:
  - Facebook Page: EasyA
  - Instagram account: easya_media
  - Threads profile: Create profile button
- Branding: Inactive, 'Add branding' button
- Ad preview panel on right side showing feed mockups with headline 'Best Headline #1' and CTA button 'Shop now'

**Not in transcript:**

Campaign hierarchy names ('EAM//Acquisition//US/CBO', 'Creative BATCH #1 Adset', 'Champions Adset', 'Best Ads'); Facebook Page 'EasyA'; Instagram account 'easya_media'; Partnership ad toggle Off.

## [00:45:33] Duplicate your ad modal settings in Meta Ads Manager

frame: 080_00-45-33.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Modal window titled 'Duplicate your ad':
- Select a campaign for your ad: Existing campaign (radio selected), 'Select a campaign' search input
- Select an ad set for your ad: Existing ad set (radio selected), 'Search ad sets' input, 'Add to all' button
- Number of copies: 1 (stepper input)
- Checkbox selected: 'Show existing reactions, comments and shares on new ads'
- Buttons: Cancel, Duplicate (blue button)

**Not in transcript:**

Default modal options: 'Existing campaign', 'Existing ad set', Number of copies set to 1, checked option 'Show existing reactions, comments and shares on new ads', Duplicate and Cancel buttons.

## [00:45:34] Ad contextual action menu in Meta Ads Manager

frame: 080_00-45-34.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager interface showing action menu for ad 'New Ad #1 - Copy': Duplicate (Ctrl+D), Copy (Ctrl+C), Paste (Ctrl+V), Delete (Ctrl+Del), Create rule, ID: 120226477810010332.

**Not in transcript:**

Action menu options and shortcut keys (Duplicate, Copy, Paste, Delete, Create rule), Ad ID 120226477810010332.

## [00:45:44] Ad format and destination settings for duplicated ad

frame: 080_00-45-44.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager showing 'New Ad #2' setup:
- Ad format: Single image or video (selected)
- Multi-advertiser ads checkbox
- Destination: Website (selected), Website URL: 'easymedia.com', Display link, Browser add-ons: None
- Ad preview on right panel showing Facebook and Instagram mockups.

**Not in transcript:**

Website URL easymedia.com, Browser add-ons set to None, ad preview columns.

## [00:45:58] Media selection dialog in Meta Ads Manager

frame: 080_00-45-58.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Modal 'Set up your creative -> Media':
- Tabs: All, Account, Business, Instagram, Page
- Search media input, Upload button
- Instagram Images gallery (showing first 8 images, 1080 x 1350, 1290 x 2293)
- EasyA gallery showing 2 images: 1000 x 1000 and 1920 x 1080.

**Not in transcript:**

Media gallery tab choices, dimensions of available assets (1000 x 1000, 1920 x 1080, 1080 x 1350, 1290 x 2293), Upload button.

## [00:46:04] Advantage+ creative image generation prompt

frame: 080_00-46-04.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Modal step 'Image generation':
- 'Advantage+ creative image generation AI'
- Notice: 'In our experiment, campaigns with all ads adding AI-generated images saw 11% CTR lift and 8% CVR lift'
- Status: 'Analyzing your image...'
- Headline: 'You could get 11% higher clickthrough rate. Add more creative diversity with AI-generated images.'

**Not in transcript:**

Exact lift percentages displayed (11% CTR lift, 8% CVR lift).

## [00:46:14] Disabling site links enhancement confirmation dialog

frame: 080_00-46-14.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Confirmation popup: 'Add site links may improve performance'
- Text: 'We recommend turning on as many Advantage+ creative enhancements as possible, which can help improve performance.'
- Dropdown: 'Why are you turning this enhancement off? Optional - Select a reason for turning off this enhancement'
- Buttons: 'Turn off', 'Keep using'.

**Not in transcript:**

Dropdown prompt 'Why are you turning this enhancement off? Optional', Buttons 'Turn off' and 'Keep using'.

## [00:46:23] Ad creative placements and copy overview for New Ad #2

frame: 080_00-46-23.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager ad setup for 'New Ad #2':
- Creative setup: Site links (Off), Catalog items (Off)
- Media (22 Placements): Feeds, In-stream ads for videos and reels; Stories and Reels, Search results, Apps and sites; Right column, Search results
- Flexible media: Enabled
- Advantage+ creative image generation prompt with thumbnails (+ 11 more)
- Primary text: 'Best Copy #1'
- Ad preview on right panel displaying EasyA ad with dark visual.

**Not in transcript:**

22 placements breakdown categories, Flexible media status: Enabled, Advantage+ image generation thumbnail preview count (+ 11 more).

## [00:46:45] Selecting media crop aspect ratios for New Ad #3

frame: 080_00-46-45.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager dialog: 'Select media crop for placements'. Shows three aspect ratio previews (Square: Original 1:1, Vertical: Original 9:16, Horizontal: Original 1.91:1) displaying a screenshot creative with headline 'Going from $5k/Day to $40k/Day Makes you feel some type of way'. Toggle: 'Turn on flexible media to show media you chose for a specific aspect ratio across all placements.'

**Not in transcript:**

Ad creative text visible: 'Going from $5k/Day to $40k/Day Makes you feel some type of way' with Discord/dashboard metrics screenshot. Placement options: Square (1:1), Vertical (9:16), Horizontal (1.91:1).

## [00:46:49] New Ad #3 preview with new creative image

frame: 080_00-46-49.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager ad editor for 'New Ad #3'. Left sidebar shows ads: 'New Ad #1', 'New Ad #3', 'New Ad #2'. Center pane details: 'Ad creative', placements (22 Placements: Feeds/In-stream, Stories/Reels, Right column), 'Flexible media: Enabled', 'Advantage+ creative image generation'. Right side shows Facebook and Instagram ad previews featuring the '$5k/Day to $40k/Day' creative image with headline 'Best Headline #1'.

**Not in transcript:**

22 Placements configured. Left tree hierarchy shows the 3 ads: New Ad #1, New Ad #3, New Ad #2.

## [00:47:08] Multi-ad selection across all 3 ads

frame: 080_00-47-08.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager bulk editing view. Top banner: 'You're editing 3 ads at once'. Sidebar shows all three ads selected: 'New Ad #1', 'New Ad #3', 'New Ad #2'. Center shows bulk 'Tracking for 3 ads' (Website events, Offline events). Warning: 'Your Meta Pixel is not active'. Right preview panel shows '1 of 3 ads'.

**Not in transcript:**

Status: 'You're editing 3 ads at once'. Meta Pixel warning: 'Website events cannot be tracked without an active Meta Pixel. Please check your account's data sources in Events Manager...'.

## [00:47:10] Duplicate your ads dialog for bulk duplication

frame: 080_00-47-10.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager modal: 'Duplicate your ads'. Options: 'Select a campaign for your ads' (Existing campaign / New campaign), 'Select an ad set for your ads' (Existing ad set / New ad set), 'Number of copies: 1', checkbox: 'Show existing reactions, comments and shares on new ads' (checked). Cancel and Duplicate buttons.

**Not in transcript:**

Modal title indicates plural 'Duplicate your ads'. Checkbox setting: 'Show existing reactions, comments and shares on new ads' is checked by default.

## [00:47:13] Meta Ads Manager showing duplicated ad batch and tracking settings

frame: 080_00-47-13.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager: In Creative BATCH #1 Adset, 3 duplicated ads are selected ('New Ad #3 - Copy', 'New Ad #1 - Copy', 'New Ad #2 - Copy'). Top notification: 'You're editing 3 ads at once'. Tracking section shows 'Tracking for 3 ads', Website events with Pixel 'EAM-YOUTUBE' (Pixel ID: 1602392147111447) with warning 'Your Meta Pixel is not active'. App events and Offline events visible.

**Not in transcript:**

Pixel ID: 1602392147111447, Warning: 'Your Meta Pixel is not active', Offline Event Set ID: 458380732878449 AUTO.

## [00:47:20] Ad editing screen for duplicated ad copy variations

frame: 080_00-47-20.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager ad editor for 'New Ad #1 - Copy'. Headline input: 'Best Headline #1', 'Test Headline #2'. Description input field. 'Optimize text per person: Enabled'. 'Call to action: Shop now'. Info labels section with '11 info labels selected'. Ad preview on the right.

**Not in transcript:**

Optimize text per person is Enabled; Call to action is 'Shop now'; '11 info labels selected'.

## [00:47:39] Destination website URL configuration for duplicated ad batch

frame: 080_00-47-39.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager Destination settings: 'Website' radio selected. Website URL input: 'easymedia.com/profit-calcula' with 'Preview URL' button. Display link field. Browser add-ons options: None, Call, Messenger, Instagram Direct, WhatsApp.

**Not in transcript:**

Website URL entered: easymedia.com/profit-calcula; Browser add-ons options visible.

## [00:47:41] Profit and ROAS calculator landing page

frame: 080_00-47-41.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*webpage*

**On screen:**

Calculator webpage: Top nav: EVOLVE NEW, CR8TIVE, Follow, Join our team, Work with us. Form fields on left: Average (Gross) Profit Margin: 0.6; Breakeven ROAS value: 1.67; Service Fee: $2,000 /pm; Performance Fee: 5% Profit; Commission: $2,500. Form fields on right: Recommended Ad Spend: $20,000 per month (20000); ROAS Value Multiplier: 6.00 times returns (6.00); Revenue From Ad Spend (ROAS): $120,000 per month; Profit After Margin: $72,000 per month; Profit After Ad Spend: $52,000 per month; Profit After All Spend: $50,000 per month; True Profit: $45,000 per month. Large button: 'ROI: 2240%'.

**Not in transcript:**

All specific numbers and calculations shown: Breakeven ROAS 1.67, Service fee $2,000, Performance fee 5%, Commission $2,500, Recommended ad spend $20,000, Multiplier 6.00, Revenue $120,000, Margin profit $72,000, True profit $45,000, ROI 2240%.

## [00:48:53] Meta Ads Manager ad URL configuration for New Ad #1 - Copy

frame: 080_00-48-53.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager editing 'New Ad #1 - Copy' under 'Creative BATCH #1 Adset'. Destination settings show: Website URL set to 'easyamedia.com/profit-calcula' [partially visible], Preview URL button, Display link field, Browser add-ons option set to 'None'. Ad preview on the right shows Twitter-style post creative with revenue graph.

**Not in transcript:**

Ad hierarchy shows: EAM//Acquisition//US/CBO > Creative BATCH #1 Adset > New Ad #1 - Copy. Browser add-ons list: None, Call, Messenger, Instagram Direct, WhatsApp.

## [00:48:58] Meta Ads Manager ad URL configuration for New Ad #2 - Copy

frame: 080_00-48-58.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager editing 'New Ad #2 - Copy'. Website URL shows 'syamedia.com/profit-calculator' [partially truncated]. Ad preview displays black background creative with white logo mark.

**Not in transcript:**

Selection moved to New Ad #2 - Copy in the left sidebar hierarchy.

## [00:49:00] Editing Website URL on New Ad #3 - Copy

frame: 080_00-49-00.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager editing 'New Ad #3 - Copy'. Website URL field contains 'easyamedia.com'. Destination set to Website.

**Not in transcript:**

Cursor hovering over 'Build a URL Parameter' link below Website URL field.

## [00:49:03] Ad setup and format settings for New Ad #3 - Copy

frame: 080_00-49-03.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager showing Ad setup for New Ad #3 - Copy: Create ad selected. Media setup: Manual upload selected. Format: Single image or video selected. Ad preview shows image with overlay text: '$5k/Day to $40k/Day Makes you feel some type of way 🥲'.

**Not in transcript:**

Options under Media setup include Advantage+ catalog ads; options under Format include Flexible, Carousel, Collection; Multi-advertiser ads checkbox shown below.

## [00:49:22] Renaming ad to reflect landing page test name

frame: 080_00-49-22.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager editing ad name: 'New Ad #3_LP_Profit'. In the ad tree list on the left, ads are listed: New Ad #3_LP_Profit, New Ad #1, New Ad #1 - Copy, New Ad #2 - Copy, New Ad #3, New Ad #2.

**Not in transcript:**

Facebook Page selected: 'EasyA'; Instagram account: 'easya_media'. Identity section visible.

## [00:49:27] Updating ad name for New Ad #2 - Copy

frame: 080_00-49-27.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager editing 'New Ad #2 - Copy'. Left sidebar shows 'New Ad #1_LP_Profit' and 'New Ad #3_LP_Profit' already renamed. Ad name field highlighted showing 'New Ad #2 - Copy' ready to be updated.

**Not in transcript:**

Sidebar reflects updated names for ads #1 and #3: 'New Ad #1_LP_Profit' and 'New Ad #3_LP_Profit'.

## [00:49:29] Renaming ad New Ad #2_LP_Profit in Meta Ads Manager

frame: 080_00-49-29.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager interface showing campaign hierarchy: EAM//Acquisition//US//CBO > Creative BATCH #1 Adset > New Ad #2_LP_Profit. Left sidebar lists: New Ad #3_LP_Profit, New Ad #1, New Ad #1_LP_Profit, New Ad #2_LP_Profit, New Ad #3, New Ad #2.

**Not in transcript:**

Breadcrumb path: EAM//Acquisition//US//CBO > Creative BATCH #1 Adset; ad preview card with EasyA page identity and 'Best Headline #1', 'Best Copy #1'.

## [00:49:40] Renaming ad to New Ad #3_LP_Home in Meta Ads Manager

frame: 080_00-49-40.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager ad configuration pane: Ad name input box contains 'New Ad #3_LP_Home'. Left sidebar hierarchy lists ads: New Ad #3_LP_Profit, New Ad #1_LP_Home, New Ad #1_LP_Profit, New Ad #2_LP_Profit, New Ad #3, New Ad #2.

**Not in transcript:**

Ad name typed: 'New Ad #3_LP_Home'. Visible list of renamed and pending ads in the ad set.

## [00:51:22] Completed list of 6 ads in Creative BATCH #1 Adset

frame: 080_00-51-22.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager left sidebar displaying 6 ads in 'Creative BATCH #1 Adset':
- New Ad #3_LP_Profit
- New Ad #1_LP_Home
- New Ad #1_LP_Profit
- New Ad #2_LP_Profit
- New Ad #3_LP_Home
- New Ad #2_LP_Profit

Also shows 'Champions Adset' with 'Best Ads'. Currently selected: 'New Ad #3_LP_Profit'.

**Not in transcript:**

Shows the exact naming and order of the 6 creative batch ads pairing creative variations with landing page variations.

## [00:51:54] Creative BATCH #1 Adset conversion configuration

frame: 080_00-51-54.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager editing 'Creative BATCH #1 Adset' (6 Ads):
- Conversion location: 'Website' (selected: 'Drive sales and conversions on your website')
- Other options: Website and shop, App, Website and app, Message destinations, Calls, Website and calls
- Performance goal: Maximize number of conversions
- Dataset: EAM-YOUTUBE
- Audience definition: 'Your audience is broad.'

**Not in transcript:**

Dataset selected: 'EAM-YOUTUBE'; Performance goal set to 'Maximize number of conversions'; Audience broad indicator.

## [00:51:56] Duplicating Champions Adset modal

frame: 080_00-51-56.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager modal 'Duplicate your ad set':
- 'Select a campaign for your ad set': Existing campaign (Original campaign)
- 'Number of copies': 1
- Buttons: Cancel, Duplicate

**Not in transcript:**

Modal interface options for duplicating ad set into original campaign.

## [00:52:17] Page Test #1 Adset creation in campaign hierarchy

frame: 080_00-52-17.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager showing three ad sets in sidebar hierarchy under EAM//Acquisition//US/CBO:
1. Creative BATCH #1 Adset (6 ads)
2. Page Test #1 Adset (with Best Ads)
3. Champions Adset (with Best Ads)
Selected: 'Best Ads' under 'Page Test #1 Adset'.

**Not in transcript:**

Naming of the newly duplicated ad set as 'Page Test #1 Adset'.

## [00:52:33] Ad preview for New Ad #1_LP_Home

frame: 080_00-52-33.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager displaying 'New Ad #1_LP_Home':
- Identity: Facebook Page: EasyA, Instagram account: easya_media
- Ad setup: Create ad, Manual upload
- Ad preview showing Instagram post with screenshot of Shopify dashboard showing '$703,420.02' total sales on November 25th, headline 'Best Headline #1', button 'Shop now'.

**Not in transcript:**

Shows exact creative preview (Shopify revenue dashboard screenshot ad creative) and setup settings.

## [00:52:38] Ad action menu options in Meta Ads Manager

frame: 080_00-52-38.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager dropdown context menu 'Actions for this ad':
- Duplicate (Ctrl+D)
- Copy (Ctrl+C)
- Paste (grayed out)
- Delete (Ctrl+Del)
- Create rule
- ID: 120226477215610332

**Not in transcript:**

Visible context menu with keyboard shortcuts: Duplicate (Ctrl+D), Copy (Ctrl+C), Delete (Ctrl+Del), and ad ID '120226477215610332'.

## [00:52:44] Pasting duplicated ad into Page Test #1 Adset

frame: 080_00-52-44.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager interface showing ad set hierarchy on the left with 'New Ad #1_LP_Home - Copy' pasted under 'Page Test #1 Adset'. The main pane shows ad settings: Ad name 'New Ad #1_LP_Home - Copy', Identity with Facebook Page 'EasyA', Instagram account 'easya_media', and an ad preview pane on the right.

**Not in transcript:**

Ad name input box text 'New Ad #1_LP_Home - Copy', Facebook Page 'EasyA', Instagram account 'easya_media'.

## [00:52:59] Duplicate your ad dialog modal

frame: 080_00-52-59.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager popup dialog 'Duplicate your ad': Select a campaign for your ad ('Existing campaign' selected), Select an ad set for your ad ('Existing ad set' selected), 'Number of copies' set to '1'. Buttons 'Cancel' and 'Duplicate'.

**Not in transcript:**

Default settings in Duplicate your ad modal: Existing campaign selected, Existing ad set selected, Number of copies set to 1.

## [00:53:15] Multiple duplicated ads in Page Test #1 Adset

frame: 080_00-53-15.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Sidebar showing Page Test #1 Adset containing: 'New Ad #1_LP_Home - Copy', 'Best Ads #2', and 'Best Ads #3'. Ad setup panel for the selected ad with Ad name, Identity, and Ad preview displayed.

**Not in transcript:**

The naming 'Best Ads #2' and 'Best Ads #3' appearing in the sidebar hierarchy under Page Test #1 Adset.

## [00:54:02] Renamed ads to LP_Advertorial in Page Test #1 Adset

frame: 080_00-54-02.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Sidebar hierarchy showing renamed ads under Page Test #1 Adset: 'Best Ad #1_LP_Advertorial_#1', 'Best Ads #2_LP_Advertorial...', and 'Best Ads #3_LP_Advertorial...'. The main panel displays Ad set name 'Page Test #1 Adset' and Conversion settings (Website selected, Maximize number of conversions, Dataset: EAM-YOUTUBE).

**Not in transcript:**

Exact naming structure of ads: 'Best Ad #1_LP_Advertorial_#1', 'Best Ads #2_LP_Advertorial...', 'Best Ads #3_LP_Advertorial...'. Dataset 'EAM-YOUTUBE'.

## [00:54:16] Viewing original New Ad #3_LP_Home preview

frame: 080_00-54-16.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager showing ad settings for 'New Ad #3_LP_Home' under 'Creative BATCH #1 Adset'. The preview on the right shows Instagram/Facebook post with copy header '$5k/Day to $40k/Day Makes you feel some type of way' with line graph screenshots.

**Not in transcript:**

Specific ad creative graphic text: '$5k/Day to $40k/Day Makes you feel some type of way'.

## [00:54:27] Entering destination URL for landing page test ad

frame: 080_00-54-27.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Destination section of ad configuration: 'Website' radio button selected. 'Website URL' set to 'easyamedia.com/adv'. 'Display link' input field. 'Browser add-ons' set to 'None'.

**Not in transcript:**

Exact input field value 'easyamedia.com/adv' in Website URL; Browser add-ons options: None, Call, Messenger, Instagram Direct, WhatsApp.

## [00:56:08] Ad setup under Offer Test ad set in Meta Ads Manager

frame: 080_00-56-08.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager showing breadcrumb: EAM//Acquisition//US/CBO > Offer Test #1 Adset > Best Ad #1_LP_Advertorial_#1. In left sidebar under Offer Test #1 Adset: 'Best Ad #1_LP_Advertorial_#1', 'Best Ads #2_LP_Advertorial...', 'Best Ads #3_LP_Advertorial...'. Form fields show Ad name, Partnership ad toggle (Off), Identity (Facebook Page: EasyA, Instagram account: easya_media).

**Not in transcript:**

Ad naming Best Ad #1_LP_Advertorial_#1, Facebook Page 'EasyA', Instagram account 'easya_media', Campaign 'EAM//Acquisition//US/CBO'.

## [00:56:33] Publish draft items dialog in Meta Ads Manager

frame: 080_00-56-33.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Modal dialog 'Publish draft items?': 'Your changes to Offer Ad #1_LP_Offer have been saved as drafts automatically, but they aren't running yet. Click "Publish" to apply these changes and start running your ads.' Buttons: 'Close' and 'Publish'. Left sidebar shows Offer Test #1 Adset with 'Offer Ad #1_LP_Offer'.

**Not in transcript:**

Dialog text and buttons 'Don't show this again', 'Close', 'Publish'. Ad named 'Offer Ad #1_LP_Offer'.

## [00:56:40] Ad sets table view inside Acquisition CBO campaign

frame: 080_00-56-40.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager Ad sets tab showing rows: 'Champions Adset', 'Broad Adset Women - 35+', 'Offer Test #1 Adset' (selected), 'Creative BATCH #1 Adset'. Columns include Off / On, Ad set, Average purchases..., Hook Rate, Video Hold, Video average play time, Excluded custom audiences, Included custom audiences, Audience gender.

**Not in transcript:**

Specific ad sets visible: 'Broad Adset Women - 35+' which is about to be deleted.

## [00:56:56] Clean campaign structure with three core ad sets

frame: 080_00-56-56.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager showing 'Ad sets for 1 Campaign' inside 'Acquisition//US/CBO'. Three remaining ad sets:
1. 'Offer Test #1 Adset' (Bid strategy: Highest volume Conversions, Budget: Using campaign...)
2. 'Creative BATCH #1 Adset' (Bid strategy: Highest volume Conversions, Budget: Using campaign...)
3. 'Champions Adset' (Bid strategy: Highest volume Conversions, Budget: Using campaign...)
Footer shows 'Results from 3 ad sets'.

**Not in transcript:**

Bid strategy 'Highest volume Conversions', Budget setting 'Using campaign...', Campaign name '//Acquisition//US/CBO'.

## [00:58:24] Configuring ad set spending limits in Meta Ads Manager

frame: 080_00-58-24.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager ad set edit interface for 'Creative BATCH #1 Adset':
- Budget: 'You set a daily Advantage campaign budget of $200.00.'
- Start date: May 21, 2025, 12:00 AM PDT
- End date: Set an end date (unchecked)
- Ad set spending limits: Checkbox checked
- Daily minimum: $20.00 CAD ('We'll aim to spend at least this amount.')
- Daily maximum: blank CAD ('We won't spend more than this amount.')
- Left sidebar lists campaigns, ad sets, and ads hierarchy: EAM//Acquisition//US//CBO > Creative BATCH #1 Adset (6 ads), Offer Test #1 Adset, Champions Adset.

**Not in transcript:**

Currency is set to CAD (Canadian Dollars). Start date specified as May 21, 2025 at 12:00 AM PDT. Exact phrasing of the prompt: 'We'll aim to spend at least this amount.' and 'We won't spend more than this amount.'

## [00:58:50] Ad set spending limits fields in Meta Ads Manager

frame: 080_00-58-50.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager editing 'Creative BATCH #1 Adset':
- 'Ad set spending limits' checked
- Daily minimum: '$20.00 CAD' ('We'll aim to spend at least this amount.')
- Daily maximum: input field ('We won't spend more than this amount.')
- Budget: 'daily Advantage campaign budget of $200.00.'
- Start date: 'May 21, 2025 12:00 AM PDT'

**Not in transcript:**

Currency CAD; Start date 'May 21, 2025 12:00 AM PDT'.

## [01:00:12] Renaming new campaign to EAM//ASC//US//

frame: 080_01-00-12.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager Campaigns table:
- Existing campaign: 'EAM//Acquisition//US/CBO' ($200.00 Daily)
- New Sales Campaign being renamed inline: 'EAM//ASC//US//'
- Action button: 'Save to draft'

**Not in transcript:**

Text being typed into the campaign name field: 'EAM//ASC//US//'; button 'Save to draft'.

## [01:00:19] Choose a campaign setup modal in Meta Ads Manager

frame: 080_01-00-19.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Dialog 'Choose a campaign setup':
- 'Advantage+ shopping campaign' (Streamlined, Tailored, Best practices): 'Maximize performance and reach valuable audiences with a simplified setup. Preset settings include placements, age and more.'
- 'Manual sales campaign' (Manual setup): 'Create a sales campaign from scratch using the standard setup.' (selected)
- Annotative overlay box on left: 'ASC is actually ABO but it functions the same as an CBO. Spencer just loves his CBOs.'

**Not in transcript:**

On-screen note: 'ASC is actually ABO but it functions the same as an CBO. Spencer just loves his CBOs.'

## [01:00:22] Selecting Advantage+ shopping campaign setup

frame: 080_01-00-22.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Dialog 'Choose a campaign setup':
- Option 'Advantage+ shopping campaign' is selected (radio active)
- Subtitle tags: 'Streamlined', 'Tailored', 'Best practices'
- Description: 'Maximize performance and reach valuable audiences with a simplified setup. Preset settings include placements, age and more.'
- Buttons: 'Back', 'Continue' (loading)

**Not in transcript:**

Tags on Advantage+ shopping campaign: Streamlined, Tailored, Best practices.

## [01:00:32] Preset campaign settings for Advantage+ shopping campaign

frame: 080_01-00-32.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Modal 'Preset campaign settings' ('This campaign includes the following preset settings.'):
- Campaign objective: Sales
- Dynamic creative: Off
- Placements: Advantage+ placements
- Age: 18 and over
- 'Close' button
Background settings:
- Special Ad Categories: None declared
- Conversion location: 'Website' (Drive sales and conversions on your website.)

**Not in transcript:**

Close button; 'This campaign includes the following preset settings.' heading text; Conversion location set to Website in the background.

## [01:01:34] Configuring ad level settings for Advantage+ shopping campaign

frame: 080_01-01-34.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager interface showing ad settings for Advantage+ shopping campaign:
- Campaign: EAM//ASC//US//CBO Campaign
- Ad name: Advantage+ shopping campaign 05/20
- Partnership ad: Off
- Identity:
  - Facebook Page: EasyA
  - Instagram account: easya_media
  - Threads profile: Create profile
- Ad preview panel with toggle enabled and 'Advanced preview' button

**Not in transcript:**

Ad name input 'Advantage+ shopping campaign 05/20', Facebook Page 'EasyA', Instagram account 'easya_media'.

## [01:02:03] Ad sets overview table with Offer Test, Creative BATCH, and Champions

frame: 080_01-02-03.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager table under Campaigns > Ad sets for 1 Campaign:
- Campaign name: EAM//Acquisition//US//CBO
- Columns: Off / On, Ad set, Delivery, Campaign name, Attribution setting, Bid strategy, Budget, Amount spent, Reach, Impress...
- Row 1: Offer Test #1 Adset | In draft | EAM//Acquisition//US//CBO | Highest volume | Using campaign...
- Row 2: Creative BATCH #1 Adset | In draft | EAM//Acquisition//US//CBO | Highest volume | Using campaign...
- Row 3: Champions Adset | In draft | EAM//Acquisition//US//CBO | Highest volume | Using campaign...

**Not in transcript:**

Exact campaign naming string 'EAM//Acquisition//US//CBO', bid strategy 'Highest volume Conversions', Total spent: $0.00.

## [01:03:14] Formula for calculating max creatives to test per week

frame: 080_01-03-14.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*document*

**On screen:**

Google Doc notes:
"**How to figure out the max number of creatives to test per week:**

Example #1 - Budget $100/day

Total Budget (example $100/day)
Target CPA (Example $20)

Total Ads = Budget/TCPA

$100/$20 = 5

So max amount of concepts is 5 considering 100% of your budget is testing.

this applies to all budgets below $1,000 per day.

If your budget is above $1,000/day, you are fine to test at will."

**Not in transcript:**

"Total Ads = Budget/TCPA", "considering 100% of your budget is testing."

## [01:05:05] Performance table reviewing ad sets after 7 days

frame: 080_01-05-05.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager ad sets table (Date range: May 13, 2025 - May 19, 2025):
- Columns: Off/On, Ad set, Date created, Delivery, Att. set, Campaign name, Budget, Reach, Impressions, Frequency, CPM, Results
- Row BATCH#15: May 16, 2025 | Learning | Reach: 595 | Imp: 795 | Freq: 1.34 | CPM: $16.10
- Row BATCH#10 (selected, turned off): May 7, 2025 | Off | Reach: 413 | Imp: 517 | Freq: 1.25 | CPM: $15.69 | Results: -
- Row BATCH#10: May 7, 2025 | Learning limited | Reach: 9,646 | Imp: 14,017 | Freq: 1.45 | CPM: $21.81 | Results: 6
- Row EDIT#1 - Br...: May 4, 2025 | Learning limited | Reach: 2,976 | Imp: 4,838 | Freq: 1.63 | CPM: $16.55 | Results: 1
- Row BATCH#7: Apr 29, 2025 | Active | Reach: 32,380 | Imp: 60,170 | Freq: 1.86 | CPM: $16.55 | Results: 15
- Row BATCH#7: Apr 29, 2025 | Active | Reach: 32,104 | Imp: 54,815 | Freq: 1.71 | CPM: $18.03 | Results: 28
- Row PAGE #10: Apr 25, 2025 | Learning limited | Reach: 12,999 | Imp: 26,499 | Freq: 2.04 | CPM: $10.19 | Results: 4
- Row PAGE #10: Apr 24, 2025 | Active | Reach: 54,748 | Imp: 75,677 | Freq: 1.38 | CPM: $17.01 | Results: 23

**Not in transcript:**

Exact metric values for BATCH#10, Reach 413, Impressions 517, Frequency 1.25, CPM $15.69.

## [01:07:25] Evaluating ad performance metrics across ad sets

frame: 080_01-07-25.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager report table (Date range: Mar 9, 2025 - Mar 15, 2025):
- Columns: Ad set, Amount spent, Results, Cost per result, Purchases, Cost per purchase, Purchases conversion value, Purchase ROAS, AOV, CVR, Reach
- MASHUP #...: Spent: $8,853.95 | Purchases: 227 | Cost/purch: $39.00 | Value: $13,310.12 | ROAS: 1.50 | AOV: $58.63 | CVR: 5.46% | Reach: 538,758
- MASHUP #...: Spent: $7,430.07 | Purchases: 169 | Cost/purch: $43.96 | Value: $10,225.45 | ROAS: 1.38 | AOV: $60.51 | CVR: 6.27% | Reach: 379,306
- LP (selected): Spent: $6,331.09 | Purchases: 190 | Cost/purch: $33.32 | Value: $11,260.78 | ROAS: 1.78 | AOV: $59.27 | CVR: 7.66% | Reach: 452,610
- Static Ads...: Spent: $4,800.67 | Purchases: 186 | Cost/purch: $25.81 | Value: $9,387.84 | ROAS: 1.96 | AOV: $50.47 | CVR: 16.49% | Reach: 121,246
- DCT#2//Hit...: Spent: $3,937.82 | Purchases: 120 | Cost/purch: $32.82 | Value: $7,124.64 | ROAS: 1.81 | AOV: $59.37 | CVR: 8.96% | Reach: 184,466
- Founder M...: Spent: $3,719.87 | Purchases: 97 | Cost/purch: $38.35 | Value: $5,442.07 | ROAS: 1.46 | AOV: $56.10 | CVR: 6.78% | Reach: 169,278
- B-Roll Vide...: Spent: $2,882.98 | Purchases: 81 | Cost/purch: $35.59 | Value: $4,812.15 | ROAS: 1.67 | AOV: $59.41 | CVR: 6.69% | Reach: 139,314
- Total spent: $42,011.80 | Total purchases: 1,215 | Total value: $70,154.27 | Avg ROAS: 1.67

**Not in transcript:**

Full conversion value, AOV, CVR, and Reach numbers across all listed ad sets.

## [01:08:17] Ad set spending limits settings with daily minimum and maximum

frame: 080_01-08-17.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager Ad Set editing screen for Creative BATCH #1 Adset:
- Schedule:
  - Start date: May 21, 2025, 12:00 AM PDT
  - End date: Set an end date (unchecked)
- Ad set spending limits:
  - Ad set spending limits (checked)
  - Daily minimum: $20.00 CAD
  - Daily maximum: [empty input field] CAD
- Budget scheduling: Add entries in campaign setup
- Audience controls:
  - Locations: Included location: Canada

**Not in transcript:**

Daily minimum '$20.00 CAD', Start date 'May 21, 2025 12:00 AM PDT', Included location 'Canada'.

## [01:08:36] Meta Ads Manager campaigns list showing active CBO campaigns

frame: 080_01-08-36.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager Campaigns table:
- Campaigns listed:
  1. EAM//ASC//US//CBO Campaign
  2. EAM//Acquisition//US//CBO (Bid strategy: Highest volume, Budget: $200.00 Daily)
  3. EAM//ASC//US//CBO (Bid strategy: Highest volume, Budget: $200.00 Daily)
Popup notification at bottom left: 'Updates - Add payment method'.

**Not in transcript:**

Campaign names and daily budgets ($200.00 Daily) shown in the table.

## [01:08:39] Duplicating existing CBO acquisition campaign modal

frame: 080_01-08-39.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Modal dialog 'Duplicate your campaign':
- Number of copies: 1
- Checkbox selected: 'Show existing reactions, comments and shares on new ads'
- Buttons: 'Cancel', 'Duplicate'

**Not in transcript:**

Setting checkbox 'Show existing reactions, comments and shares on new ads' is checked.

## [01:08:47] Renaming duplicated campaign to Raw-Content CBO campaign

frame: 080_01-08-47.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager Campaign editor:
- Campaign name field input: 'EAM//Raw-Content//US/CBO - Copy'
- Buying type: Auction
- Campaign objective: Sales (selected)
Left sidebar shows duplicated structure: Offer Test #1 Adset (3 ads) and Creative BATCH #1 Adset (6 ads).

**Not in transcript:**

Naming convention: 'EAM//Raw-Content//US/CBO - Copy'; Campaign objective set to Sales.

## [01:08:56] Deleting Offer Test ad set from duplicated raw content campaign

frame: 080_01-08-56.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Confirmation dialog: 'Do you want to delete the ad set? If you delete this ad set, you won't be able to recover it later.' Buttons: Cancel, Delete.
In background ad sets list, 'Offer Test #1 Adset' is checked for deletion while 'Creative BATCH #1 Adset' remains.

**Not in transcript:**

User selects 'Offer Test #1 Adset' to delete it completely from the raw content campaign.

## [01:09:01] Ad level view in Creative BATCH #1 Adset

frame: 080_01-09-01.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Ads list under Creative BATCH #1 Adset:
- New Ad #3_LP_Profit
- New Ad #1_LP_Home
- New Ad #3_LP_Home
- New Ad #2_LP_Profit
- New Ad #2_LP_Profit
- New Ad #1_LP_Profit
Results from 6 ads.

**Not in transcript:**

Shows the 6 ads split between LP_Home and LP_Profit before pruning.

## [01:09:05] Deleting duplicate LP test ads to keep single landing page

frame: 080_01-09-05.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Confirmation dialog: 'Do you want to delete 3 ads? If you delete these ads, you won't be able to recover them later.' Buttons: Cancel, Delete.
Three ads selected for deletion (the duplicate landing page variants: New Ad #2_LP_Profit, New Ad #2_LP_Profit, New Ad #1_LP_Profit).

**Not in transcript:**

Selecting 3 ads to remove the secondary landing page variation.

## [01:09:10] Configuring ad set settings in raw content testing campaign

frame: 080_01-09-10.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Ad Set editor:
- Ad set name: Creative BATCH #1 Adset
- Conversion location: Website (selected)
- Performance goal: Maximize number of conversions
- Dataset: EAM-YOUTUBE
Left sidebar shows 3 remaining ads: New Ad #3_LP_Home, New Ad #1_LP_Home, New Ad #3_LP_Profit.

**Not in transcript:**

Audience definition shows 'Your audience is broad'; performance goal is 'Maximize number of conversions'.

## [01:09:27] Ad sets overview for raw content testing campaign

frame: 080_01-09-27.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager showing 'Ad sets' tab with 1 selected:
- Ad set: Raw Content - BATCH #1 Adset
- Campaign name: EAM//Raw-Content//US/CBO
- Bid strategy: Highest volume Conversions
- Budget: Using campaign...

**Not in transcript:**

Ad set name 'Raw Content - BATCH #1 Adset', Campaign name 'EAM//Raw-Content//US/CBO', Bid strategy details.

## [01:09:43] Rule formula for maximum creatives to test per week

frame: 080_01-09-43.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*document*

**On screen:**

**How to figure out the max number of creatives to test per week:**

Example #1 - Budget $100/day

Total Budget (example $100/day)
Target CPA (Example $20)

Total Tests = Budget/TCPA

$100/$20 = 5

So max amount of concepts is 5 considering 100% of your budget is testing.

this applies to all budgets below $1,000 per day.

If your budget is above $1,000/day, you are fine to test at will.

**Not in transcript:**

Text on document stating 'this applies to all budgets below $1,000 per day. If your budget is above $1,000/day, you are fine to test at will.'

## [01:10:21] Meta Ads Manager campaigns list with 4 draft campaigns

frame: 080_01-10-21.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager Campaigns table listing:
- EAM//Raw-Content//US/CBO (In draft, Highest volume, $200.00 Daily)
- EAM/ASC/US/CBO Campaign (In draft, Using ad set bid..., Using ad set bu...)
- EAM//Acquisition//US/CBO (In draft, Highest volume, $200.00 Daily)
- EAM//ASC//US//CBO (In draft, Highest volume, $200.00 Daily)

**Not in transcript:**

Campaign budgets ($200.00 Daily) and exact campaign list entries.

## [01:10:34] Duplicating acquisition campaign for whitelisting

frame: 080_01-10-34.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Modal dialog 'Duplicate your campaign':
- Number of copies: 1
- Checkbox selected: 'Show existing reactions, comments and shares on new ads'
Buttons: [Cancel], [Duplicate]

**Not in transcript:**

Checkbox option: 'Show existing reactions, comments and shares on new ads'

## [01:10:37] Editing duplicated campaign settings for whitelisting

frame: 080_01-10-37.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Campaign edit screen for 'EAM//Acquisition//US/CBO - Copy':
Left sidebar tree:
- EAM//Acquisition//US/CBO - Copy
  - Creative BATCH #1 Adset (6 ads)
  - Offer Test #1 Adset (3 ads)
Main panel:
- Campaign name: EAM//Acquisition//US/CBO - Copy
- Buying type: Auction
- Campaign objective: Sales (selected)
- Advantage+ catalog ads: Off

**Not in transcript:**

Sidebar ad set breakdown (Creative BATCH #1 Adset with 6 ads, Offer Test #1 Adset with 3 ads).

## [01:10:46] Ads view under Whitelisting campaign in Ads Manager

frame: 080_01-10-46.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager showing Ads tab (9 selected):
- Campaign name: EAM//Whitelisting//US/CBO
- Ad Set Names: Creative BATCH #1 Adset, Offer Test #1 Adset
- Ad names listed: New Ad #1_LP_Profit, New Ad #2_LP_Profit, New Ad #1_LP_Home, New Ad #3_LP_Profit, New Ad #3_LP_Home, Offer Ad #1_LP_Offer

**Not in transcript:**

Renamed campaign 'EAM//Whitelisting//US/CBO' and list of duplicated ads.

## [01:10:52] Ad configuration view showing identity settings in Meta Ads

frame: 080_01-10-52.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager showing ad editing under campaign EAM//Whitelisting//US/CBO > Creative BATCH #1 Adset > New Ad #1_LP_Profit. Navigation sidebar on left shows ad sets: 'Creative BATCH #1 Adset' and 'Offer Test #1 Adset'. Sections visible: 'Ad name', 'Partnership ad' (Off), 'Identity' (Facebook Page: EasyA, Instagram account, Threads profile, Branding), 'Ad setup', and 'Ad preview'.

**Not in transcript:**

Ad set names 'Offer Test #1 Adset', 'Creative BATCH #1 Adset'; ad names 'New Ad #3_LP_Home', 'New Ad #3_LP_Profit', 'New Ad #1_LP_Home', 'New Ad #2_LP_Profit'.

## [01:11:02] Editing Whitelisting Ad identity fields in Meta Ads

frame: 080_01-11-02.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager ad setup for 'Whitelisting Ad #1_LP_Offer' under 'Whitelisting Champions' ad set. Identity section shows: Facebook Page dropdown (EasyA), Instagram account dropdown (easya_media), Threads profile ('Create profile'), Branding ('Inactive', 'Add branding').

**Not in transcript:**

Ad name 'Whitelisting Ad #1_LP_Offer', ad set name 'Whitelisting Champions', Instagram handle 'easya_media'.

## [01:11:31] Destination and Ad creative settings in Meta Ads Manager

frame: 080_01-11-31.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager ad editing pane scrolled down: 'Destination' options: 'Website' (Send people to your website), 'Instant Experience', 'Facebook event'. 'Ad creative' section with 'Set up creative' button and warning message: 'One of the following is required: image, video, website URL, template link, text or offer.' 'Event details - Optional'.

**Not in transcript:**

Destination options and validation error text displayed on screen.

## [01:11:40] Whitelisting ad setup using creator page and preview

frame: 080_01-11-40.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager showing Identity section switched to creator: Facebook Page: 'Find Your Fit With Karissa', Instagram account: 'findyourfit.withkarissa', Threads profile: 'findyourfit.withkarissa'. Ad preview pane shows mobile Facebook feed and Instagram feed previews displaying creator handle 'Find Your Fit With Karissa' and 'findyourfit.withkarissa'.

**Not in transcript:**

Exact page name 'Find Your Fit With Karissa' and handle 'findyourfit.withkarissa'.

## [01:12:08] Ad sets table with Whitelisting Champions ad set

frame: 080_01-12-08.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager table under 'Ad sets for 1 Campaign': Row 1: 'Whitelisting Champions' (Delivery: In draft, Campaign name: EAM//Whitelisting//US/CBO, Bid strategy: Highest volume Conversions, Budget: Using campaign...). Row 2: 'Raw Content - BATCH #1 Adset' (Delivery: In draft, Campaign name: EAM//Raw-Content//US/CBO). Notification popup at bottom left: 'Add payment method'.

**Not in transcript:**

Row details, bid strategy 'Highest volume Conversions', and 'Add payment method' alert.

## [01:12:45] Campaigns list with four core draft campaigns

frame: 080_01-12-45.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager Campaigns list showing 4 campaigns:
1. EAM//Whitelisting//US/CBO (In draft, Highest volume, Budget $200.00 Daily)
2. EAM//Raw-Content//US/CBO (In draft, Highest volume, Budget $200.00 Daily)
3. EAM/ASC/US/CBO Campaign (In draft, Using ad set bid..., Using ad set bu...)
4. EAM//Acquisition//US/CBO (In draft, Highest volume, Budget $200.00 Daily, selected with checkmark).

**Not in transcript:**

Budget $200.00 Daily visible across campaigns; exact naming of all 4 campaigns.

## [01:12:58] Duplicate campaign modal in Ads Manager

frame: 080_01-12-58.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Modal dialog 'Duplicate your campaign': 'Number of copies' input (set to 1), checkbox checked: 'Show existing reactions, comments and shares on new ads'. Buttons: 'Cancel', 'Duplicate'. In background: table showing EAM//Acquisition//US/CBO.

**Not in transcript:**

Checkbox label 'Show existing reactions, comments and shares on new ads'.

## [01:13:08] Renaming duplicated campaign to CAAUUK CBO

frame: 080_01-13-08.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager campaign editor. Campaign name field set to: 'EAM//Acquisition//CAAUUK/CBO - Copy'. Buying type: Auction. Campaign objective: Sales selected. Left hierarchy shows 'Offer Test #1 Adset' (with 3 ads) and 'Creative BATCH #1 Adset' (with 6 ads).

**Not in transcript:**

Left sidebar tree structure showing ad sets and ad names: 'Offer Ad #1_LP_Offer', 'New Ad #3_LP_Profit', 'New Ad #2_LP_Profit', 'New Ad #1_LP_Home'.

## [01:13:13] Campaigns list including international acquisition CBO

frame: 080_01-13-13.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager Campaigns table. Visible campaigns:
- EAM//Acquisition//CAAUUK/CBO (In draft, Highest volume, Budget: $200.00 Daily)
- EAM//Whitelisting//US/CBO (In draft, Highest volume, $200.00 Daily)
- EAM//Raw-Content//US/CBO (In draft, Highest volume, $200.00 Daily)
- EAM//ASC/US/CBO Campaign (In draft, Using ad set bid...)
- EAM//Acquisition//US/CBO (In draft, Highest volume, $200.00 Daily)

**Not in transcript:**

Daily budget value of $200.00 across campaigns; status 'In draft'.

## [01:13:39] Ad sets view across multiple acquisition campaigns

frame: 080_01-13-39.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager Ad sets table showing 4 ad sets in draft:
- Creative BATCH #1 Adset (Campaign: EAM//Acquisition//Europe/C...)
- Creative BATCH #1 Adset (Campaign: EAM//Acquisition//CAAUUK/...)
- Offer Test #1 Adset (Campaign: EAM//Acquisition//CAAUUK/...)
- Offer Test #1 Adset (Campaign: EAM//Acquisition//Europe/C...)
All set to Highest volume Conversions, Using campaign budget.

**Not in transcript:**

Shows both 'Creative BATCH #1 Adset' and 'Offer Test #1 Adset' duplicated across CAAUUK and Europe campaigns.

## [01:14:16] Campaigns table showing Europe and CAAUUK campaigns

frame: 080_01-14-16.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager Campaigns table showing 6 campaigns in draft:
- EAM//Acquisition//Europe/CBO ($200.00 Daily)
- EAM//Acquisition//CAAUUK/CBO ($200.00 Daily)
- EAM//Whitelisting//US/CBO ($200.00 Daily)
- EAM//Raw-Content//US/CBO ($200.00 Daily)
- EAM//ASC/US/CBO Campaign
- EAM//Acquisition//US/CBO ($200.00 Daily)

**Not in transcript:**

Daily budget of $200.00 on Europe campaign; total results showing 6 campaigns.

## [01:14:29] Editing ad set locations setting

frame: 080_01-14-29.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager Ad Set settings for Offer Test #1 Adset. Sections: Audience controls, Locations (Included location: Canada with Edit button highlighted), Advantage+ audience, Placements. Right panel displays Audience definition (Broad).

**Not in transcript:**

Included location currently set to Canada before editing.

## [01:14:43] Configuring Worldwide location targeting with US excluded

frame: 080_01-14-43.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Locations settings in Meta Ads Manager:
- Included: Worldwide (checkmark icon)
- Excluded: United States (red cross icon)
Map view displaying blue highlight for worldwide selection. Notification: 'We are unable to highlight the border of Worldwide on the map, but it has been successfully added.'

**Not in transcript:**

Exact UI showing Worldwide included and United States excluded; verification notice banner on top right.

## [01:14:59] Ad set conversion location and performance goal

frame: 080_01-14-59.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Ad set editor for Offer Test #1 Adset under EAM//Acquisition//WW/CBO. Conversion location: Website selected ('Drive sales and conversions on your website.'). Performance goal: Maximize number of conversions. Dataset: EAM-YOUTUBE.

**Not in transcript:**

Dataset selected as 'EAM-YOUTUBE'; campaign named updated in header to 'EAM//Acquisition//WW/CBO'.

## [01:15:15] Breakdown menu in Meta Ads Manager

frame: 080_01-15-15.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager reporting interface with 'Breakdown' dropdown open. Options visible under Recently used: Image, video and slideshow, Platform, Text. Options under Popular: Day, Age, Placement, Country, Platform.

**Not in transcript:**

Dropdown list items under Breakdown: Day, Age, Placement, Country, Platform, Image, video and slideshow.

## [01:15:37] Ad sets view showing draft Offer Test #1 Adset

frame: 080_01-15-37.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager ad sets table displaying selected item:
- Ad set: Offer Test #1 Adset
- Delivery: In draft
- Campaign name: EAM//Acquisition//WW/CBO
- Attribution setting: -
- Bid strategy: Highest volume Conversions
- Budget: Using campaign...

**Not in transcript:**

Ad set status 'In draft', bid strategy 'Highest volume Conversions', date range 'Last 30 days: Apr 20, 2025 - May 19, 2025'

## [01:16:53] Campaigns dashboard listing six structured campaigns

frame: 080_01-16-53.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager Campaigns table listing:
1. EAM//Acquisition//WW/CBO | Delivery: In draft | Bid strategy: Highest volume | Budget: $200.00 Daily
2. EAM//Acquisition//CAAUUK/CBO | In draft | Highest volume | $200.00 Daily
3. EAM//Whitelisting//US/CBO | In draft | Highest volume | $200.00 Daily
4. EAM//Raw-Content//US/CBO | In draft | Highest volume | $200.00 Daily
5. EAM//ASC/US/CBO Campaign | In draft | Using ad set bid... | Using ad set bu...
6. EAM//Acquisition//US/CBO | In draft | Highest volume | $200.00 Daily
Results from 6 campaigns

**Not in transcript:**

Daily budget set at $200.00 for WW, CAAUUK, Whitelisting, Raw-Content, and US campaigns; prompt: 'Add payment method' for 'EAM-YouTube'.

## [01:17:00] Section card: How to properly creative test

frame: 080_01-17-00.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*title card*

**On screen:**

How to properly creative test

## [01:17:42] Campaign budget scaled to $300 daily

frame: 080_01-17-42.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Meta Ads Manager Campaigns view with single campaign selected:
- Campaign: EAM//Acquisition//US/CBO
- Delivery: -
- Attribution setting: -
- Bid strategy: Highest volume
- Budget: $300.00 Daily

**Not in transcript:**

Campaign budget set to $300.00 Daily on EAM//Acquisition//US/CBO

## [01:17:56] Spotlight calculator calculating budget bump

frame: 080_01-17-56.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

MacOS Spotlight search bar calculation overlay:
200*1.2 = 240

## [01:20:00] Evolve creative testing rules and FAQ

frame: 080_01-20-00.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*document*

**On screen:**

To Sum Up:
1 Campaign
1 Champions Ad set, Multiple Creative Test Ad Sets
3 creatives in each ad set (same concept), each with 2 headlines and 2 copies

WARNING DO NOT TURN OFF YOUR EXISTING ADS IF THEY ARE WORKING. THE DUMBEST THING YOU CAN DO IS TURN OFF ADS THAT ARE WORKING. IF YOUR OTHER CAMPAIGNS ARE WORKING - LEAVE THEM ON - IF YOU TURN THEM OFF AND YOU LOSE MONEY... THAT IS ON YOU.

FAQ:
1. How many creative ad sets can you launch at a time?
- If you're only spending few hundred a day, I recommend keeping it to 5 ad sets (including champions ad set, if it has ads inside) at a time so budget can be distributed efficiently. Focus more on intent of the ads instead of throwing things at the wall.
- You can launch all 5 ad sets in the same day if you wish
- If you're spending a few thousand a day you can definitely have more ad sets

2. Do we set min/max spend limits for this campaign method?
- No, we tested it and it didn't help.

3. How long do you test creatives for?
- We recommend testing creatives for a minimum of 3 days. However, [we recommend] testing 7 days. If they don't do well after 7 days (not much spend... missing KPI), we will then turn them off. If you want to test ads longer... we usually don't recommend leaving ads on for longer than 14 days.

4. How do you know if a creative ad set is a winner (Covered in "When To Le... Running" video below)?
- If it gets majority of spend at KPI like shown in the video. Besides that... not sure, the question you should ask is "Did my overall campaign per... improve?". If your overall campaign ROAS didn't improve, it's not a winner.

**Not in transcript:**

Exact structure rules (3 creatives in each ad set with 2 headlines and 2 copies), 14-day upper testing limit, capitalized warning statement.

## [01:20:03] Creative testing formula based on budget and target CPA

frame: 080_01-20-03.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*document*

**On screen:**

**How to figure out the max number of creatives to test per week:**
Example #1 - Budget $100/day
Total Budget (example $100/day)
Target CPA (Example $20)
Total Tests = Budget/TCPA
$100/$20 = 5
So max amount of concepts is 5 considering 100% of your budget is testing.
this applies to all budgets below $1,000 per day.
If your budget is above $1,000/day, you are fine to test at will.

**Not in transcript:**

Formula and worked example: "Target CPA (Example $20)", "Total Tests = Budget/TCPA", "$100/$20 = 5", note that rule applies to all budgets below $1,000 per day.

## [01:20:10] FAQ on ad set limits, duration, and shut-off rules

frame: 080_01-20-10.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*document*

**On screen:**

• If you're spending a few thousand a day you can definitely have more ad sets
2. Do we set min/max spend limits for this campaign method?
• No, we tested it and it didn't help.
3. How long do you test creatives for?
• We recommend testing creatives for a minimum of 3 days. However, we now leave them testing 7 days. If they don't do well after 7 days (not much spending or missing KPI), we will then turn them off. If you want to test ads longer, you can. But we usually don't recommend leaving ads on for longer than 14 days.
4. How do you know if a creative ad set is a winner (Covered in "When To Leave a 3:2:2 Running" video below)?
• If it gets majority of spend at KPI like shown in the video. Besides that if you're still not sure, the question you should ask is 'Did my overall campaign performance improve?'. If your overall campaign ROAS didn't improve, it's not a winner.
5. When do you turn off creatives/ad sets (Covered in "When To Turn Off A 3:2:2" video below)?
• With this method we are only turning off at the ad set level not ad level.
• If the ad set is not getting any spend at all the first 3 days we will turn off
• If the ad set is still not getting much spend after 7 days, and ROAS is not good we will turn off. If ROAS is good you may leave it running if you have no other creatives in queue.
• If the ad set took majority of spend within the first 3 days, performance... and overall campaign performance went down, we will turn off. But w... learnings on the ad because something about it got a lot of engagem... it more conversion driven. Try to give it 2-3 days to test, it may not co... 1st day but 2nd or 3rd day pick up.
6. What's the minimum budget to launch this?
• Minimum I would start this campaign at is $100/day
7. What if I don't have any past winners to put in the champions ad set or it's...

**Not in transcript:**

Detailed bullet points for FAQ items 2 through 7 (e.g. testing minimum 3 days vs 7 days up to 14 days; turning off at ad set level; specifics on ROAS/spend rules).

## [01:21:56] Ad account overview showing $2.2M monthly spend

frame: 080_01-21-56.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*software demo*

**On screen:**

Date range: Last 30 days: Apr 20, 2025 - May 19, 2025
Pivot table:
- Amount spent: $2,231,570.60
- ROAS: 2.69
- Total spent: $2,231,570.56
- Overall ROAS: 2.69

**Not in transcript:**

Date range: Last 30 days: Apr 20, 2025 - May 19, 2025; Amount spent: $2,231,570.60; ROAS: 2.69

## [01:22:41] Evolve Skool Community Page and Membership Overview

frame: 080_01-22-41.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*webpage*

**On screen:**

Skool page for 'Evolve' (skool.com/evolve-8484):
- Community header: 'EVOLVE GET RICH QUICK FOR SURE'
- Status: Private | 264 members | $999 /month | By Spencer Pawliw
- Button: 'JOIN $999/month'
- Stats: 264 Members, 5 Online, 5 Admins
- Description: 'Welcome to EVOLVE growth... This is a community made to help Shopify brands find success with Facebook Ads and Conversion Rate Optimization to scale their stores to multiple 7-and 8-figures.'
- 'The #1 eCommerce Community On Skool'
- 'NOTE: This is NOT for beginners.'
- 'What's Included:
  • Direct Communication and Access to Spencer & Shaun via Discord
  • 1-On-1 Call with Spencer or Shaun
  • Private Community of 200+ 6-8 Figure Brand Owners
  • Full EVOLVE Program - 70+ Ads & Creative Training Modules
  • Full EVOLVE CRO Program - 60+ CRO Training Modules (NEW)
  • Exclusive Resources Such As Meta Insiders, Fulfillment Partners, Accountants & More.'

**Not in transcript:**

URL slug 'evolve-8484', member count 264, price '$999/month', list of included items (Discord access, 1-on-1 call with Spencer or Shaun, 70+ creative training modules, 60+ CRO modules, partner resources).

## [01:23:02] Evolve Live Webinar Video on Vimeo

frame: 080_01-23-02.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*webpage*

**On screen:**

Vimeo video player page:
- Video title: 'Evolve Live Webinar $0-$100k'
- Video slide text: 'But before we scaled brands to $100k/day'
- Presenter webcam overlay in upper right corner
- Uploader: Shaun Eng

**Not in transcript:**

Vimeo platform, video title 'Evolve Live Webinar $0-$100k', exact slide text 'But before we scaled brands to $100k/day', uploader 'Shaun Eng'.

## [01:23:12] Evolve Free Skool community overview and program preview

frame: 080_01-23-12.png (Drive: https://drive.google.com/file/d/1b64j1NVjtIToPCMrAB5H9J2E4G-B9Nma/view?usp=drivesdk)

*webpage* | legibility: partly legible

**On screen:**

Inset graphic showing Skool page:
- Evolve (Free)
- Learn the Facebook ad strategies that scale Shopify brands to $100k+ per day in sales, one step at a time.
- Join The Full Program
- Book An Evolve Intro Call
- Work With Our Agency
- Stats: 5.2k Members, 22 Online, 3 Admins
- Button: JOIN GROUP
- Footer info: Private | 5.2k members | Free | By Spencer Pawliw

**Not in transcript:**

Member count (5.2k members), online users count (22), admins count (3), specific bullet links ('Book An Evolve Intro Call', 'Work With Our Agency'), and creator name 'Spencer Pawliw'.
