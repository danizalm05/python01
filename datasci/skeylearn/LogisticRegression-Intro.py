'''
Logistic Regression
   p(X) =  logistic(β0+β1X)
   https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/dd57cc433d3e42dea49038ccabbc98c7/ead846c91bad40919bb26d3aac8b03db/1?activate_block_id=block-v1%3AHIT%2BACD_RFP4_DataScienceIntro_HE%2B2022_1%2Btype%40html%2Bblock%40037d65f4b11c428c9b90d9e5629750cc
   https://labs.vocareum.com/main/main.php?m=editor&asnid=537366&stepid=537367&hideNavBar=1
   https://scikit-learn.org/stable/glossary.html#glossary

   https://en.wikipedia.org/wiki/Logistic_regression
'''


#Logistic regression: Given samples (xi,yi)
#  for i=1,…,ni=1,…,n,
#           find the best values of  β0 and  β1 so that:
#           y=logistic(β0+β1X)   or     logit(y)=β0+β1X.

import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn import metrics
from scipy.special import expit
from scipy.special import logit
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10, 6)

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
# hours   and  pass 1 or not pass 0
hours = [0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50]
pass_Exam = [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1]
df = pd.DataFrame({"hours": hours, "pass_exam": pass_Exam})

print(df.head(10))
df.plot.scatter(x='hours',y='pass_exam',s=30)
plt.show()
''' 
For this example, we want to find coefficients β0 and  β1 so that the model
 p(X) = probability ( passing  | X hours studying ) = logistic(β0 + β1 X)
    best explains the data. 
'''
###LogisticRegression model
lrm=linear_model.LogisticRegression()
lrm.fit(df[["hours"]],df["pass_exam"])

df.plot.scatter(x='hours',y='pass_exam',s=30)

#create a set of points along the x axis to print prediction graph
x = np.linspace(df['hours'].min(),df['hours'].max(),50 )
# linspace(start, stop, num  )
#get probabilistic predictions for those points (using predict_proba)
y_pred_p=lrm.predict_proba(np.reshape(x, (-1, 1))) # we need to
#          reshape x to get it to a 2 dimensional array
#get only the probability for the "pass" category
y_pred_p1=[y[1] for y in y_pred_p]

#plot the prediction graph
plt.plot(x,y_pred_p1,color='Black')

# this is an alternative plot option to calculate directly the predicted value, using the model paramters and avoiding predict_proba function
# you can uncomment the line below, and comment the line before and see the results
#plt.plot(x,expit(lrm.intercept_[0]+lrm.coef_[0][0]*x),color='green')

# draw the line of y=0.5 as the decision point
plt.plot(x,[0.5]*len(x),color="red")
plt.show()

''' ---------------------   Model investigation  --------
The curve predicts the probability that a student will pass, given 
how many hours they've studied.
From the plot, we can see that the more hours you spend studying, 
the more likely you are to pass the exam. 
'''
# If I study just 2 hours, what is the likelihood that I'll pass?
hours=2
likelihood = expit(lrm.intercept_[0]+lrm.coef_[0][0]*hours)
print("likelihood to pass If I study just 2 hours = ",likelihood)
'''
How many hours do you have to study in order for 
the probability of passing to be greater than 50%
'''
prob_passing = 0.5
probability50 =  logit(prob_passing) - lrm.intercept_[0]/lrm.coef_[0][0]
print("probability of passing to be greater than 50% = ", probability50)

#               Evaluating a classification method
#---------------------------------------------------------------

y_pred = lrm.predict(df[["hours"]])
print("list of predicted (y's) = ",y_pred)
y_actual=df["pass_exam"]

print("list of actual values (y's) = ", y_actual)
metrics.confusion_matrix(y_actual, y_pred)
print("\nConfusion matrix.\n-----------")
print(metrics.confusion_matrix(y_actual, y_pred))

print("accuracy is:",metrics.accuracy_score(y_actual, y_pred))
print("precision is:",metrics.precision_score(y_actual, y_pred))
print("recall is:",metrics.recall_score(y_actual, y_pred))
print("f1 is:",metrics.f1_score(y_actual, y_pred))

