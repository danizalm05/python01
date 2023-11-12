'''
  Linear Regression
Part 1 - Simple Linear Regression Implementation
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

advert = pd.read_csv('./data/Advertising.csv',index_col=0) #load data
print(advert.head(10))
# initial description of the data
print("\n\nadvert.describe()\n--------------\n",advert.describe())


# visualize the data.
# Start with a scatter plot, with different indication for each advertising channel.

plt.scatter(x=advert['Digital'],y=advert['Sales'],c='r',marker='s',label='Digital')
plt.scatter(x=advert['Radio'],y=advert['Sales'],c='b',marker='o',label='Radio')
plt.scatter(x=advert['Newspaper'],y=advert['Sales'],c='k',marker='*',label='Newspaper')

plt.legend(numpoints=1,loc=4)
plt.xlabel('Ad budget (Thousands of dollars)')
plt.ylabel('Sales (units of product)')
plt.show()

'''
Observations
The more money spent, the larger the number of sales.
The most money was spent on Digital advertising. 
The amount for Radio and Newspaper is about the same in all markets.
The standard deviation for TV advertising is larger.
'''

'''
First, let's just look at the effect of Digital advertising on sales.
 We use the linear regression model:
                     Sales  =  beta_0 + beta_1 * Digital. 

Build our first linear regression model

We will use the  LinearRegression() class and train the model using it's fit function.
We will start by building a model that predicts the sales only 
 based on Digital advertising. Therefore, in the call to fit, we pass as  X  only 
 the column of  Digital  (expressed as advert.iloc[:,0:1] ).
advert.iloc[:, 0:1] # first 2 columns of data frame with all rows (column of digital)
advert.iloc[:, 3: ] # column of sales
'''
#print(advert.iloc[:,3:].head(4))


# Build  linear regression model
digital_budget = advert.iloc[:,0:1]
sales = advert.iloc[:,3:]
model = linear_model.LinearRegression().fit(   digital_budget ,   sales   )
'''
Apply the model (using predict)

Prediction of number of sales based on the Digital advertising budget.
 We will use the same scatter plot as before to show the actual sales based on Digital 
 advertisng, but also add a line that represents the sales prediction according to the linear 
 regression model. 
 You can see below, how we use the predict function of the model, to express the sales
  prediction.
'''


prediction = model.predict(digital_budget)

plt.scatter(x=advert['Digital'],y=advert['Sales'],c='k',marker='*',label='Digital')
plt.plot( advert['Digital'],    prediction   ,      'k',color='blue',linewidth=3 )

plt.xlabel('Digital budget (Thousands of dollars)')
plt.ylabel('Sales (Thousand units of product)')
plt.show()

#What are the values of   β0 and β1
# let's look inside the model
print("b1:",model.coef_)
print("b0:",model.intercept_)

'''
 Interpretation and discussion
-----------------------------
The intercept of the line is β̂0 = 7.032  
This means that without any Digital advertising, the model predicts that 7,032
units of product will be sold.
The slope of the line is β̂1=0.0475β. This means that the model predicts that 
for every additional $1  spent on TV advertising, an additional 47.5 units of 
product are sold.

Are these good results?   
Evaluation metrics

One way to measure the quality of the fit is to look at the sum of the 
squared error,
           n
   SSE  =  ∑( yi −  β̂0−β̂1*xi )^2.
          y=1

We don't have exactly a method for this in python,so we can either 
calculate it ourselves

'''
print(" type  advert.Sales = ",type(advert.Sales))

print("type (model.predict(advert.iloc[:,0:1])) = ",type(model.predict(advert.iloc[:,0:1])))

print("type   advert.Sales.tolist() = ",type(advert.Sales.tolist()))
print("type(model.predict(advert.iloc[:,0:1]).flatten()) = ",
      type(model.predict(advert.iloc[:,0:1]).flatten()))

print(type(advert.Sales.tolist())) # change pandas.core.series.Series  to  <class 'list'>

#change <class 'numpy.ndarray'> to one dimantion <class 'numpy.ndarray'>
print(type(model.predict(advert.iloc[:,0:1]).flatten()  ))
print( model.predict(advert.iloc[:,0:1]).flatten()   )

# SSE  Sum of Squared Errors
# TSS  Total Sum Squared,
def sse(Y, Y_HAT):
    sse = sum([(y - y_hat)**2 for y,y_hat in zip(Y, Y_HAT)])
    return sse

SSE = sse(advert.Sales.tolist(),model.predict(advert.iloc[:,0:1]).flatten())

print("\nSSE = ",SSE)

'''
 Alternatively, we can use the method of mean_squared_error. 
However, since it calculates the mean, we need to multiply 
the output we get with the number of items that we predicted.  
'''
from sklearn.metrics import mean_squared_error

SSE02 = mean_squared_error(advert.Sales.tolist(),
      model.predict(advert.iloc[:,0:1]).flatten())*len(advert.Sales.tolist())
print("SSE02 = ",SSE02)
'''
           n
   SSE  =  ∑( yi −  β̂0−β̂1*xi )^2.
          y=1
         
           n
   TSS  =  ∑( y_average −  β̂0−β̂1*xi )^2.  = Varience
          y=1
  always  SSE <= TSS  and     0 <= SSE/TSS <= 1

r2 = 1 - SSE/TSS    big 'r2' means small error      

'''


#r2_score method
from sklearn.metrics import r2_score

r2s = r2_score(advert.Sales.tolist(),model.predict(advert.iloc[:,0:1]).flatten())
print("\nR2 =",r2s )
# As you can see, in our model, the value is R2=0.612R , which isn't bad.
# The model explains  61% of the variability in sales.

# Regression for Radio
lr_radio = linear_model.LinearRegression() # create a linear regression object

# scikit-learn doesn't work as well with pandas, so we have to extract values
x = advert['Radio'].values.reshape(advert['Radio'].shape[0],1)
y = advert['Sales'].values.reshape(advert['Sales'].shape[0],1)

lr_radio.fit(X=x, y=y)

plt.scatter(x, y,  color='black')
plt.plot(x, lr_radio.predict(x), color='blue', linewidth=3)

plt.xlabel('Radio budget (Thousands of dollars)')
plt.ylabel('Sales (Thousand units of product)')
plt.show()
### # Regression for Radio and Newspaper
lr_newspaper = linear_model.LinearRegression() # create a linear regression object

# scikit-learn doesn't work as well with pandas, so we have to extract values
x = advert['Newspaper'].values.reshape(advert['Newspaper'].shape[0],1)
y = advert['Sales'].values.reshape(advert['Sales'].shape[0],1)

lr_newspaper.fit(X=x, y=y)

plt.scatter(x, y,  color='black')
plt.plot(x, lr_newspaper.predict(x), color='blue', linewidth=3)

plt.xlabel('Newspaper budget (Thousands of dollars)')
plt.ylabel('Sales (Thousand units of product)')
plt.show()

print("Slope:",lr_newspaper.coef_)
print("Intercept:",lr_newspaper.intercept_)
print("R2:",lr_newspaper.score(x,y))

print("Slope:",lr_radio.coef_)
print("Intercept:",lr_radio.intercept_)
print("R2:",lr_radio.score(x,y))

#Three models on a single plot with different colors:

plt.scatter(x=advert['Digital'],y=advert['Sales'],c='r',marker='s',label='Digital')
plt.scatter(x=advert['Radio'],y=advert['Sales'],c='b',marker='o',label='Radio')
plt.scatter(x=advert['Newspaper'],y=advert['Sales'],c='g',marker='*',label='Newspaper')
plt.legend(numpoints=1,loc=4)

plt.plot(advert['Digital'], model.predict(advert['Digital'].values.reshape(advert['Digital'].shape[0],1)),c='r',linewidth=3)
plt.plot(advert['Radio'],lr_radio.predict(advert['Radio'].values.reshape(advert['Radio'].shape[0],1)),c='b',linewidth=3)
plt.plot(advert['Newspaper'],lr_newspaper.predict(advert['Newspaper'].values.reshape(advert['Newspaper'].shape[0],1)),c='g',linewidth=4)

plt.xlabel('Ad budget (Thousands of dollars)')
plt.ylabel('Sales (units of product)')
plt.show()