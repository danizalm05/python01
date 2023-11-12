'''
  Multiple Linear Regression

For 200 different ‘markets’  , this dataset consists of the number of sales of a particular
product as well as the advertising budget for different media: Digital, radio, and newspaper.

https://labs.vocareum.com/main/main.php?m=editor&asnid=537364&stepid=537365&hideNavBar=1
https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/dd57cc433d3e42dea49038ccabbc98c7/dd04e44b8598468196bdfcddaa6feb3d/?activate_block_id=block-v1%3AHIT%2BACD_RFP4_DataScienceIntro_HE%2B2022_1%2Btype%40sequential%2Bblock%40dd04e44b8598468196bdfcddaa6feb3d
https://scikit-learn.org/stable/glossary.html#glossary

'''
import pandas as pd

from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np

from sklearn import linear_model
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

advert = pd.read_csv('./data/Advertising.csv',index_col=0) #load data
#print(advert.head(10))
# initial description of the data
#print("\n\nadvert.describe()\n--------------\n",advert.describe())
'''
Multiple Linear Regression

Model:
Sales=β0+β1∗Digital+β2∗Radio+β3∗Newspaper.
'''

#This time the features (X)  has 3 columns (attributes)
lr = linear_model.LinearRegression() # create a linear regression object

x = advert[['Newspaper',"Radio","Digital"]]
y = advert['Sales']
lr.fit(X=x, y=y);
print(x.head(10))

'''
When we analyze the model, instead of just getting β0 and β1 as before, 
we should get now β1, β2 and β3 (for each of the attributes) - 
you can see them in the array we get from calling the coef_ function,
 in addition to β0 that you still get from the intercept_ command.
'''
print("\nSlope:",lr.coef_)
print("Intercept:",lr.intercept_)
#nterpretation

# Spending an additional $1,000 on radio advertising results in an
# increase in sales by 189 units. Radio is the most effective at method of
# advertising.
'''
In order to evaluate the model it will be useful to get its  R2 value. 
One option is to use the r2_score method, another one is to use the
model's score function. 
The score function gets the X and y values used to train the regressor, 
and returns the R2 value. 
See both functions before, and luckily they both return the same value..
'''
print("R2:",lr.score(x,y))
print("R2:",r2_score(y,lr.predict(x.values)))

'''
 Part 3 - Non-Linear Regression
 ------------------------------------------------------
    1. Nonlinear relationships and feature engineering
    2. Overfitting
 
   We can consider the interaction between TV and Radio advertising in the model, by taking

Sales = β0 + β1 ∗ Digital_budget    +  β2∗  Radio_budget+
         β3 ∗ Newspaper_budget  +  β4 * Digital_budget∗Radio_budget.
  
The rational behind the last term is that perhaps spending x  on television
 advertising and y  on radio advertising leads to more sales than simply
  x +y.  
   this is synergy effect and  in statistics it is known as
   the interaction effect.

Note: even though the relationship between the independent and 
dependent variables is nonlinear, the model is still linear. 
'''

lr = linear_model.LinearRegression() # create a linear regression object

advert["DigitalxRadio"]=advert["Radio"]*advert["Digital"]


# scikit-learn doesn't work as well with pandas,
# so we have to extract values
x = advert[["Radio","Digital","DigitalxRadio"]].values.reshape(advert[["Radio","Digital","DigitalxRadio"]].shape[0],3)
y = advert['Sales'].values.reshape(advert['Sales'].shape[0],1)

lr.fit(X=x, y=y)


print("Slope:",lr.coef_)
print("Intercept:",lr.intercept_)
print("R2:",lr.score(x,y))

