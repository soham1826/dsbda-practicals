# -*- coding: utf-8 -*-
"""dsbda9SK.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D5warNAksjeNGiacB_8BDETAo_8f0cnh
"""

# use the inbuilt titanic dataset and plot a box plot for distribution of age with respect to each gender along with the information about whether hteu survived or not.
# write observations
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic = sns.load_dataset('titanic')

# Plotting a box plot for distribution of age with respect to each gender and survival
plt.figure(figsize=(12, 6))
sns.boxplot(x='sex', y='age', hue='survived', data=titanic, palette='Set2')
plt.title('Distribution of Age by Gender and Survival')
plt.xlabel('Gender')
plt.ylabel('Age')
plt.show()

# Analysis of the graph
# Overall, females tend to have a lower median age compared to males, both for those who survived and those who did not survive.
# For those who did not survive (color green), the median age of females is noticeably lower than that of males, suggesting that younger females were more vulnerable or at greater risk in the event or scenario represented by this data.
# For those who survived (color orange), the median ages of males and females are more comparable, but females still tend to have a slightly lower median age.
# The interquartile ranges (the boxes) are broader for females who survived compared to females who did not survive, indicating a wider spread of ages among the female survivors.
# There are some outliers (represented by the dots) in both genders and survival categories, indicating the presence of individuals with significantly higher ages compared to the rest of the data.

