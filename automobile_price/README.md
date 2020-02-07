# Project: Automobile EDA and price prediction

### Context
This dataset consist of data From 1985 Ward's Automotive Yearbook. Here are the sources

Sources:

1) 1985 Model Import Car and Truck Specifications, 1985 Ward's Automotive Yearbook. 2) Personal Auto Manuals, Insurance Services Office, 160 Water Street, New York, NY 10038 3) Insurance Collision Report, Insurance Institute for Highway Safety, Watergate 600, Washington, DC 20037

### Content
This data set consists of three types of entities: (a) the specification of an auto in terms of various characteristics, (b) its assigned insurance risk rating, (c) its normalized losses in use as compared to other cars. The second rating corresponds to the degree to which the auto is more risky than its price indicates. Cars are initially assigned a risk factor symbol associated with its price. Then, if it is more risky (or less), this symbol is adjusted by moving it up (or down) the scale. Actuarians call this process "symboling". A value of +3 indicates that the auto is risky, -3 that it is probably pretty safe.

Note: Several of the attributes in the database could be used as a "class" attribute.

___
### Install

This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [Matplotlib](http://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [SciPy](https://www.scipy.org/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://ipython.org/notebook.html)

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](http://continuum.io/downloads) distribution of Python, which already has the above packages and more included. 

### Run

In a terminal or command window, navigate to the top-level project directory `automobile_price/` (that contains this README) and run one of the following commands:

```bash
ipython notebook automobile_price.ipynb
```  
or
```bash
jupyter notebook automobile_price.ipynb
```

This will open the Jupyter Notebook software and project file in your browser.

### Data

This dataset is available on [kaggle.](https://www.kaggle.com/toramky/automobile-dataset)

The dataset 205 entries with following 18 features.

**Features**
1. `symboling` : It is a risk factor symbol associated to the price & corresponds to the degree to which an automobile is more risky than its price indicates. +3 indicates risky, -3 indicates safety.
2. `make` : Indicates the maker or manufacturer of the automobile.
3. `fuel-type` : Indicates the type of fuel - diesel or gas.
4. `body-style` : Indicates whether the body shape of automobile is a hardtop, wagon, sedan, hatchback or convertible.
5. `drive-wheels` : Indicates the configuration of drive wheels for the automobile.
6. `wheel-base` : It is the distance between the centers of the front wheel and the rear wheel. It is continuous ranging from 86.6 120.9
7. `length` : Indicates length of the automobile and ranges from 141.1 to 208.1
8. `width` : Indicates width of the automobile and ranges from 60.3 to 72.3
9. `height` : Indicates the hieght of the automobile and ranges 47.8 to 59.8
10. `horsepower` : Maximum horsepower the automobile engine can output and ranges from 48 to 288.
11. `peak-rpm` : RPM is a way to measure how many times per minute components in the engine rotate. It ranges from 4150 to 6600
12. `highway-mpg` : Indicates the miles per galon typically consumed at highways. It is continuous from 4150 to 6600
13. `city-mpg` : Indicates the miles per galon typically consumed at cities. It is continuous from 13 to 49
14. `price` : Indicates the price of the automobile and ranges from 5118 to 45400.
15. `normalized-losses` : It is a continuous variable ranging from 65 to 256
16. `engine-location` : Indicates the location of the engine - front or rear.
17. `engine-type` : Indicates the type of engine.
18. `engine-size` : It is continuous from 61 to 326.
