import Scraper as sc
import pandas

path = "C:\Program Files (x86)\chromedriver.exe"    # Path to open in windows

df = sc.get_jobs('data-scientist', 30, False, path, 3)
