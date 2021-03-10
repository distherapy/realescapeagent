port pandas as pd
import requests
import scrapy
import re
#pseudolayout
#
#ask user which county and state
#ask user the options --> commercial, residential, lot size, house size, price min-max, mls number, county, state)
#
#realtor, zillow, mls, landzero, landsofamerica, landflip, propertyshark, trulia, redfin, movoto, century21, homes.com
#
com = input("Type 'com' for commercial or 'res' for residential:")
res = com
county = input("Type the name of the county i.e. 'Essex':")
state = input("Type the initials for the state i.e. 'NJ':")
state_full = state.state(full)
pmin = input("Type the minimum price digits only i.e. '35000':")
pmax = input("Type the maximum price digits only i.e. '125000':")
lmin = input("Type the minimum acreage:")
lminsqf = lmin * 43560
lmax = input("Type the maximum acreage:")
lmaxsqf = lmax * 43560
def realtor(com, res, hmin, hmax, lmin, pmin, pmax, county, state):
	url = 'https://www.realtor.com/realestateandhomes-search/'+ county + '-' + 'County_' + state + '/price-' + pmin + '-' + pmax + '/lot-sqft-' + lmin
	r = requests.get(url)
	df_list = pd.read_html(r.text)
	df = df_list[0]
	df.head()
	print(df)

def mls(mls):
	url = 'https://www.mls.com/'+ mls
	r = requests.get(url)
	df_list = pd.read_html(r.text)
	df = df_list[0]
	df.head()
	print(df)

def zillow(hmin, hmax, lmin, pmin, pmax, county, state):
	url = 'https://www.zillow.com/realestateandhomes-search/'+ county + '-' + 'County_' + state + '/price-' + pmin + '-' + pmax + '/lot-sqft-' + lmin
	r = requests.get(url)
	df_list = pd.read_html(r.text)
	df = df_list[0]
	df.head()
	print(df)

def landzero(pmin, pmax, county, state):
	url = 'https://www.landzero.com/land-for-sale/' + pmin + '-to-' + pmax'
	r = requests.get(url)
	df_list = pd.read_html(r.text)
	df = df_list[0]
	df.head()
	print(df)
		
def landflip(county, state_full, pmin, pmax):
	url = 'https://www.landflip.com/land-for-sale/' + state + '/' + pmin +'-minprice/' + pmax +'-maxprice/
	r = requests.get(url)
	df_list = pd.read_html(r.text)
	df = df_list[0]
	df.head()
	print(df)

def propertyshark(county, state, pmin, pmax):
	url = 'https://www.propertyshark.com/homes/US/Real-Estate-Listings/' + state + '.html?location=' + state +'-minprice/' + pmax +'-maxprice/
	r = requests.get(url)
	df_list = pd.read_html(r.text)
	df = df_list[0]
	df.head()
	print(df)

	
def loa(county, state, pmin, pmax):
	url = 'https://www.landsofamerica.com/' + county + '-County-' + state +'all-land/under-' + pmax + '/over-' + lmin + '-acres'
	r = requests.get(url)
	df_list = pd.read_html(r.text)
	df = df_list[0]
	df.head()
	print(df)

'''
faceamount = response.xpath('faceValue')
print(faceamount)
