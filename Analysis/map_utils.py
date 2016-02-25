
# This code currently doesn't work because the ee.mapclient dependency is broken
import ee
import ee.mapclient
import datetime
from geopandas import GeoDataFrame
from shapely.geometry import shape



# Authenticate your user credentials so you can access the API
ee.Initialize()

# Center the map on the study area.
ee.mapclient.centerMap(-93, 40, 4)


"""
In this step, you will select rows from a fusion table. 
This will allow you to display on a map feature data. 
The feature data is sort of like a mappable array composed of 
thousands of points, each with a lat/long 
and many associated variables. 
"""


# Select the 'Sonoran desert' feature from the TNC Ecoregions fusion table.
fc1 = (ee.FeatureCollection('ft:1Ec8IWsP8asxN-ywSqgXWMuBaxI6pPaeh6hC64lA')
      .filter(ee.Filter().eq('ECO_NAME', 'Sonoran desert')))

# Select the USGS feature collection of sampling data from Summer 2015
fc2 = ee.FeatureCollection("ft:1KLL3aOt7-mavHuL_uyLLPXOf7vUVk6v08XbzIepq");

# Paint it into a blank image.
image1 = ee.Image(0).mask(0)
ee.mapclient.addToMap(image1.paint(fc, 0, 5))

image2 = ee.Image(0).mask(0)
ee.mapclient.addToMap(image2.paint(fc, 0, 5))



""" 
In this step you are going to create a background map using Landsat imagery
by filtering an image collection by date to make a median composite. The composite
is composed of the stack of all the individual Landsat images from the entire date range.
Each image also has many bands and each band represents different kinds of spectral information 
collected by the instrument. 
"""


# Import Landsat 8 satellite imagery
var L8 = ee.ImageCollection("LANDSAT/LC8_L1T")   

# Filter to only include images within the watershed boundaries.
polygon = ee.Feature.Polygon([[
    [-109.05, 37.0], [-102.05, 37.0], [-102.05, 41.0],   
    [-109.05, 41.0], [-111.05, 41.0], [-111.05, 42.0],   
    [-114.05, 42.0], [-114.05, 37.0], [-109.05, 37.0]]])

# Create a Landsat 8 composition for the Summer of 2015 and filter
# by the bounds of the feature collection 
var collection = ee.Algorithms.Landsat.simpleComposite({
  collection: L8.filterDate('2015-7-1', '2015-8-16'),
  asFloat: true});

# Select the median pixel.
image1 = collection.median()

# Select the red, green and blue bands.
image = image1.select('B3', 'B2', 'B1')
ee.mapclient.addToMap(image, {'gain': [1.4, 1.4, 1.1]})



def fc2df(fc):

	""" Now we will write an automated function to convert a 
	feature collection into a pandas Datafram so we can maninpulate
	the data using geopandas
	"""

    # Features is a list of dict with the output
    # this calls the attributes of the feature coll
    features = fc.getInfo()['features']

    dictarr = []
      
    for f in features:
        # Store all attributes in a dict
        attr = f['properties']
        # and treat geometry separately
        attr['geometry'] = f['geometry']  # GeoJSON Feature!b
        # attr['geometrytype'] = f['geometry']['type']
        dictarr.append(attr)
       
    df = GeoDataFrame(dictarr)
    # Convert GeoJSON features to shape
    df['geometry'] = map(lambda s: shape(s), df.geometry)    
    return df

# End fc2df
# Now you have a geopandas dataframe!







