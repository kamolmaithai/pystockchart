from flask import Flask, Markup, render_template, request
import pandas as pd

# for pandas_datareader, otherwise it might have issues, sometimes there is some version mismatch
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import datetime
import time
import json

app = Flask(__name__)

@app.route('/volprofile')
def volprofile():
	# ___variables___
	ticker = request.args.get('ticker')
	#start_time = request.args.get('starttime')
	start_time = datetime.datetime(2019, 9, 1)
	#end_time = datetime.datetime(2019, 1, 20)
	end_time = datetime.datetime.now().date().isoformat()         # today
	# yahoo gives only daily historical data
	connected = False
	while not connected:
		try:
			df = web.get_data_yahoo(ticker, start=start_time, end=end_time)
			connected = True
			print('connected to yahoo')
		except Exception as e:
			print("type error: " + str(e))
			time.sleep( 5 )
			pass   
	df = df.reset_index()
	cols = ['Date', 'Close','Open' ,'Low', 'High','Volume', 'Adj Close']
	df.reindex(columns=cols)
	jsondatas = json.loads(df.to_json(orient='records'))
	#jsondatas = df.to_json(orient='records')

	return render_template('volprofileindex.html', jsondatas=jsondatas, ticker=ticker)
@app.route('/volprofile2')
def volprofile2():
	# ___variables___
	ticker = request.args.get('ticker')
	#start_time = request.args.get('starttime')
	start_time = datetime.datetime(2019, 9, 1)
	#end_time = datetime.datetime(2019, 1, 20)
	end_time = datetime.datetime.now().date().isoformat()         # today
	# yahoo gives only daily historical data
	connected = False
	while not connected:
		try:
			df = web.get_data_yahoo(ticker, start=start_time, end=end_time)
			connected = True
			print('connected to yahoo')
		except Exception as e:
			print("type error: " + str(e))
			time.sleep( 5 )
			pass   
	df = df.reset_index()
	cols = ['Date', 'Close','Open' ,'Low', 'Height','Volume', 'Adj Close']
	df.reindex(columns=cols)
	jsondatas = json.loads(df.to_json(orient='records'))
	#jsondatas = df.to_json(orient='records')

	return render_template('volprofileindex2.html', jsondatas=jsondatas, ticker=ticker)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)