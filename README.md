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

This is the result as of 2015-10-24:

	[4019] Hotelcard im Wert von CHF 95 ........................... 7.62
	[1078] CeDe.ch Geschenkkarte im Wert von CHF 30 ............... 7.50
	[1269] FLEUROP Geschenkkarte im Wert von CHF 50 ............... 7.50
	[1270] FLEUROP Geschenkkarte im Wert von CHF 100 .............. 7.50
	[1507] ATHLETICUM Geschenkkarte im Wert von CHF 50 ............ 7.50
	[1508] ATHLETICUM Geschenkkarte im Wert von CHF 100 ........... 7.50
	[4255] MAGANDO.ch Geschenkkarte im Wert von CHF 50 ............ 7.50
	[4257] MAGANDO.ch Geschenkkarte im Wert von CHF 100 ........... 7.50
	[1163] MrLens Gutschein im Wert von CHF 20 .................... 7.49
	[4253] MAGANDO.ch Geschenkkarte im Wert von CHF 20 ............ 7.49
	[1268] FLEUROP Geschenkkarte im Wert von CHF 25 ............... 7.49
	[1308] SHUI TANG Jahresabo im Wert von CHF 300 (Gutschein) .... 7.06
	[1215] VICTORIA-JUNGFRAU COLLECTION Wertgutschein von CHF 100 . 7.06
	[1307] SHUI TANG Gutschein im Wert von CHF 100 ................ 7.06
	[1510] NAVYBOOT Gutschein im Wert von CHF 100 ................. 7.06
	[1511] NAVYBOOT Gutschein im Wert von CHF 200 ................. 7.06
	[1306] SHUI TANG Gutschein im Wert von CHF 50 ................. 7.05
	[1509] NAVYBOOT Gutschein im Wert von CHF 50 .................. 7.05
	[3555] TheBungalow.ch Gutschein im Wert von CHF 100 ........... 7.04
	[3561] JEANS.CH Gutschein im Wert von CHF 200 ................. 6.76
	[3567] SHIRTERY.CH Gutschein im Wert von CHF 200 .............. 6.76
	[1504] TICKETCORNER Ski-Geschenkbox im Wert von CHF 100 ....... 6.67
	[3553] TheBungalow.ch Gutschein im Wert von CHF 50 ............ 6.67
	[3559] JEANS.CH Gutschein im Wert von CHF 100 ................. 6.58
	[3565] SHIRTERY.CH Gutschein im Wert von CHF 100 .............. 6.58
	[1329] SWISS.HOLIDAYCARD Geschenkkarte im Wert von CHF 299 .... 6.38
	[1198] THE BODY SHOP Geschenkkarte im Wert von CHF 50 ......... 6.38
	[4931] GLOBUS Geschenkkarte im Wert von CHF 200 ............... 6.35
	[1516] iTUNES Geschenkkarte im Wert von CHF 100 ............... 6.35
	[4929] GLOBUS Geschenkkarte im Wert von CHF 100 ............... 6.35
	[4933] SWAROVSKI Geschenkkarte im Wert von CHF 100 ............ 6.35
	[1197] JELMOLI Geschenkkarte im Wert von CHF 50 ............... 6.35
	[1331] LA REDOUTE Geschenkkarte im Wert von CHF 50 ............ 6.35
	[1332] HOTELPLAN Geschenkkarte im Wert von CHF 50 ............. 6.35
	[1505] BELDONA Geschenkkarte im Wert von CHF 50 ............... 6.35
	[1512] STARBUCKS Geschenkkarte im Wert von CHF 50 ............. 6.35
	[1513] BLACKOUT Geschenkkarte im Wert von CHF 50 .............. 6.35
	[1515] iTUNES Geschenkkarte im Wert von CHF 50 ................ 6.35
	[4927] GLOBUS Geschenkkarte im Wert von CHF 50 ................ 6.35
	[4938] LÜTHY BALMER STOCKER Geschenkkarte im Wert von CHF 50 .. 6.35
	[4250] GIDOR COIFFURE Geschenkkarte im Wert von CHF 100 ....... 6.33
	[4936] LÜTHY BALMER STOCKER Geschenkkarte im Wert von CHF 20 .. 6.33
	[1093] ORELL FÜSSLI Geschenkkarte im Wert von CHF 50 .......... 6.31
	[1092] ORELL FÜSSLI Geschenkkarte im Wert von CHF 20 .......... 6.31
	[3557] JEANS.CH Gutschein im Wert von CHF 50 .................. 6.26
	[3563] SHIRTERY.CH Gutschein im Wert von CHF 50 ............... 6.26
	[1201] TICKETCORNER Geschenkkarte im Wert von CHF 100 ......... 6.18
	[1196] IKEA Geschenkkarte im Wert von CHF 50 .................. 6.18
	[1200] TICKETCORNER Geschenkkarte im Wert von CHF 50 .......... 6.18
	[1199] TICKETCORNER Geschenkkarte im Wert von CHF 25 .......... 6.17
	[4249] GIDOR COIFFURE Geschenkkarte im Wert von CHF 50 ........ 6.02
	[1503] TICKETCORNER Ski-Geschenkbox im Wert von CHF 50 ........ 6.00
	[3546] TheBungalow.ch Gutschein im Wert von CHF 20 ............ 5.71
	[4247] GIDOR COIFFURE Geschenkkarte im Wert von CHF 20 ........ 5.26

Troubleshooting
===============
The scripts verbosely log to `debug.txt` which is placed in the script directory.