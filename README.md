# eRivers

### About this package:
Rivers, lakes and wetlands are generally known to be net sources of greenhouse gases to the atmosphere as they regularly emit CO2 and CH4, but much work remains quantifying spatial variability and sources, especially for large river systems highly impacted by human activities and infrastructure. The motivation behind this collaborative effort is to build an online, open-source tool for synthesizing remotely sensed watershed-related geospatial data with in situ field observations of water chemistry. Our ultimate goal is to automate data ingestion, fusion and exploration to help understand the patterns and controls driving changes in aquatic greenhouse gases to help inform regional and global carbon budgets.


### Dependencies and how to install
#### Required Packages:
* matplotlib
* pandas
* Bokeh
* scikit-learn
* numpy
* statsmodels

Here are how to install packages:
#### 1. Download miniconda and install it on your system and use the conda command-line tool to update your package listing and install the IPython notebook:
#### 2. Update conda's listing of packages for your system:
$ conda update conda
#### 3. Install IPython notebook and all its requirements
$ conda install ipython-notebook
#### 4. Install Python's Data Science packages
$ conda install numpy scipy pandas matplotlib
#### 5. Bokeh Package
##### 1. If you are already an Anaconda user, you can simply run the command:

conda install bokeh

This will install the most recent published Bokeh release from the Continuum Analytics Anaconda repository, along with all dependencies.

##### 2. Alternatively, it is possible to install from PyPI using pip:

pip install bokeh

#### Running Example Notebooks

To run our demo notebooks or our packages, clone this github repo to your local machine and navigate to the Analysis folder.  From here, you can import our functions and run demo Notebooks locally


### Links to Demo Notebooks
 * [Data Cleaning Example](/Analysis/eRiversExample.ipynb/)
 * [Mapping Example](/Analysis/maps/ee_mapping.ipynb/)

### License:
This project utilizes the MIT license.

