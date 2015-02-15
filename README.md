# bonviva-tracker
A set of scripts to mirror and parse the items in the Credit Suisse Bonviva Rewards Shop for further analysis

How To
======
1. Download this repository to a dedicated folder on your computer which is writeable for your user
1. Run `./mirror.sh`. A mirror of the rewards item pages is stored in `./cache/%ID%/%TODAY%.html`. This might take some time, depending on the speed of your Internet connection.
1. Run `./parse.py`

You now should find `./cache/YYYY-MM-DD.json` which contains a structured list all items for sale in the Credit Suisse Bonviva Rewards Shop. You can use this file to perform further analysis.

Example
=======
I was curious about which cash voucher offered in the shop gives you the most bang for the buck. I therefore wrote the script `find-vouchers.py` to find cash vouchers (as signalled by "CHF [0-9]+" in the description) and to calculate how much 1,000 Bonviva Reward Points are worth in CHF for any given voucher.

This is the result as of 2015-02-15:

    Hotelcard im Wert von CHF 95 ............................................... 7.62
    CeDe.ch Geschenkkarte im Wert von CHF 30 ................................... 7.50
    FLEUROP Geschenkkarte im Wert von CHF 50 ................................... 7.50
    FLEUROP Geschenkkarte im Wert von CHF 100 .................................. 7.50
    ATHLETICUM Geschenkkarte im Wert von CHF 50 ................................ 7.50
    ATHLETICUM Geschenkkarte im Wert von CHF 100 ............................... 7.50
    MrLens Gutschein im Wert von CHF 20 ........................................ 7.49
    FLEUROP Geschenkkarte im Wert von CHF 25 ................................... 7.49
    SHUI TANG Jahresabo im Wert von CHF 300 (Gutschein) ........................ 7.06
    VICTORIA-JUNGFRAU COLLECTION Wertgutschein von CHF 100 ..................... 7.06
    SHUI TANG Gutschein im Wert von CHF 100 .................................... 7.06
    NAVYBOOT Gutschein im Wert von CHF 100 ..................................... 7.06
    NAVYBOOT Gutschein im Wert von CHF 200 ..................................... 7.06
    SHUI TANG Gutschein im Wert von CHF 50 ..................................... 7.05
    NAVYBOOT Gutschein im Wert von CHF 50 ...................................... 7.05
    TheBungalow.ch Gutschein im Wert von CHF 100 ............................... 7.04
    JEANS.CH Gutschein im Wert von CHF 200 ..................................... 6.76
    SHIRTERY.CH Gutschein im Wert von CHF 200 .................................. 6.76
    TICKETCORNER Ski-Geschenkbox im Wert von CHF 100 ........................... 6.67
    TheBungalow.ch Gutschein im Wert von CHF 50 ................................ 6.67
    JEANS.CH Gutschein im Wert von CHF 100 ..................................... 6.58
    SHIRTERY.CH Gutschein im Wert von CHF 100 .................................. 6.58
    SWISS.HOLIDAYCARD Geschenkkarte im Wert von CHF 299 ........................ 6.38
    THE BODY SHOP Geschenkkarte im Wert von CHF 50 ............................. 6.38
    iTUNES Geschenkkarte im Wert von CHF 100 ................................... 6.35
    JELMOLI Geschenkkarte im Wert von CHF 50 ................................... 6.35
    LA REDOUTE Geschenkkarte im Wert von CHF 50 ................................ 6.35
    HOTELPLAN Geschenkkarte im Wert von CHF 50 ................................. 6.35
    BELDONA Geschenkkarte im Wert von CHF 50 ................................... 6.35
    STARBUCKS Geschenkkarte im Wert von CHF 50 ................................. 6.35
    BLACKOUT Geschenkkarte im Wert von CHF 50 .................................. 6.35
    iTUNES Geschenkkarte im Wert von CHF 50 .................................... 6.35
    GIDOR COIFFURE Geschenkkarte im Wert von CHF 100 ........................... 6.33
    ORELL FÜSSLI Geschenkkarte im Wert von CHF 50 .............................. 6.31
    ORELL FÜSSLI Geschenkkarte im Wert von CHF 20 .............................. 6.31
    JEANS.CH Gutschein im Wert von CHF 50 ...................................... 6.26
    SHIRTERY.CH Gutschein im Wert von CHF 50 ................................... 6.26
    TICKETCORNER Geschenkkarte im Wert von CHF 100 ............................. 6.18
    IKEA Geschenkkarte im Wert von CHF 50 ...................................... 6.18
    TICKETCORNER Geschenkkarte im Wert von CHF 50 .............................. 6.18
    TICKETCORNER Geschenkkarte im Wert von CHF 25 .............................. 6.17
    GIDOR COIFFURE Geschenkkarte im Wert von CHF 50 ............................ 6.02
    TICKETCORNER Ski-Geschenkbox im Wert von CHF 50 ............................ 6.00
    TheBungalow.ch Gutschein im Wert von CHF 20 ................................ 5.71
    GIDOR COIFFURE Geschenkkarte im Wert von CHF 20 ............................ 5.26

Troubleshooting
===============
The scripts verbosely log to `debug.txt` which is placed in the script directory.