from bokeh.plotting import Figure, show
from bokeh.io import output_notebook, show, vform
from bokeh.models import CustomJS, ColumnDataSource, MultiSelect
import pandas as pd

'''
def readcsv(csvfile):
	data = pd.read_csv(csvfile)
	return data
'''

def timeplot(data):
	#input data is a DataFrame
	time = pd.DatetimeIndex(data['ltime'])
	#String list to store column names from the third column of the dataframe
	columns = []
	for x in data.columns[2:]:
		columns.append(x)
	#change string to float in the data 
	for x in columns:
		if (type(data[x][0]) is str):
			for i in range(len(data[x])):
				data[x][i] = float(data[x][i].replace(',',''))
	output_notebook()
	y = data[columns[1]]
	x = time
	p = Figure(x_axis_type = 'datetime')
	
	source = ColumnDataSource(data=dict(x=x, y=y, d=data))
	#create a new columndatasoure to pass column name to CustomJS
	source2 = ColumnDataSource(data = dict(columns = columns))

	p.line('x', 'y', source = source)
	
	callback = CustomJS(args = dict(source = source, columns=source2), code="""
				var data = source.get('data');
				var columns = columns.get('data')['columns'];
				var f = cb_obj.get('value');
				y = data['y'];
				console.log('y');
				console.log(y);
				var d = data['d'];
				//get the index of the chosen column from the widget

				for(i = 0; i<columns.length;i++){
					if(f[0]==columns[i]){
					index = i;
					}
				}
				//make the column transpose since the CustomJS
				//takes dataframe as an array of arrays which is 
				//a row of the DataFrame
				for (i = 0; i < d.length; i++) {
					y[i] = d[i][index+2];
				}
				console.log('y');
				console.log(y.length);
				source.trigger('change');
				""")
	
	select = MultiSelect(title="Y_Option:", value=[columns[0]],
							options=columns, callback=callback)
	layout = vform(select, p)
	show(layout)