Convert Google Sheets charts to SVG files

1. `git clone ...`, `mkvirtualenv sheets2svg`, `pip install -r requirements.txt`
1. get link to Google Sheets chart, make sure it's published. Should look like: https://docs.google.com/spreadsheets/d/1codr6C_jxrXkcRmCIb2ao6XVG5qzdu_vYw3ObTWh2mo/pubchart?oid=1723669337&format=interactive
1. run `python convert.py`
1. input chart URL, input desired file name
1. open SVG in AI and style accordingly

### Additional requirement

If you've never used Selinium before you will also need to install a driver for your default browser. If you try to run the script without this driver it will give you a nice error message with a link to the driver for your default browers.

After you download the driver, unzip it and move it somewhere at the system level. By default, the script looks for `/Applications/chromedriver` but this can easily be changed in the script.



