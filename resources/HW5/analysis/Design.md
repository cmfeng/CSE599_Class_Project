# Design Document

This document describes the specifications for each component and function associated with the five use cases described in Question 1. 

### compareLakes
- **Name**: compareLakes
- **Function**: This function allows users to create a bar plot comparing different chosen variables across all eleven lakes.
- **Input**: This requires lakes.cvs data. This also requires users to choose a variable to plot using the ipywidgets.
- **Output**: A barplot exported as a .png file. 
- **Interactions**: 

This is an example of what the psuedocode might look like.  
```sh
$ load required packages  
$ call in csv data  
$ assign date-time index  

$ create widget  
$ ask for user input to widget  
$ plot results  
$ export results   
```

### plotMethane
- **Name**: plotMethane
- **Function**: This function allows users to create a scatterplot comparing methane concentrations to several other variables shown to be important for methane production in aquatic systems.
- **Input**: This requires lakes.cvs data. This also requires users to choose a variable to plot using the ipywidgets.
- **Output**: A scatterplot exported as a .png file. 
- **Interactions**: 

### plotFdom
- **Name**: plotFDOM
- **Function**: This function allows users to create a scatterplot comparing FDOM to several other variables shown to be important for methane production in aquatic systems.
- **Input**: This requires lakes.cvs data. This also requires users to choose a variable to plot using the ipywidgets.
- **Output**: A scatterplot exported as a .png file. 
- **Interactions**: 

### checkNulls
- **Name**: checkNulls
- **Function**: This function allows users to check for nulls in the lakes.csv dataset. 
- **Input**: This requires lakes.cvs data. This also requires users to choose a variable to plot using the ipywidgets.
- **Output**: A scatterplot exported as a .png file. 
- **Interactions**: 


### compareMethods
- **Name**: compareMethods
- **Function**: This function allows users to create a barplot comparing wind flux estimates from a model to several directly measured flux estimates
- **Input**: This requires lakes.cvs data. This also requires users to choose a variable to plot using the ipywidgets.
- **Output**: A scatterplot exported as a .png file. 
- **Interactions**: 

