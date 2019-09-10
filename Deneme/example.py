import csv
from scipy import stats  
import numpy as np  
import matplotlib.pylab as plt2
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
from matplotlib.ticker import PercentFormatter
import matplotlib.ticker as ticker
from matplotlib.pyplot import legend
import matplotlib
from numpy.random import randn
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from scipy import stats
from sklearn.utils.extmath import density
#filename='C:\\Users\samet.yildiz\\OneDrive - airties.com\\PA Trimming\\4930 HW-ENG Results Analysis\\Example.csv'
filename='C:\\Users\samet.yildiz\\OneDrive - airties.com\\PA Trimming\\4930 HW-ENG Results Analysis\\Results_evaluation.csv'
#filename='C:\\Users\samet.yildiz\\OneDrive - airties.com\\PA Trimming\\4930 HW-ENG Results Analysis\\DUT9_results.csv'
#filename='C:\\Users\samet.yildiz\\OneDrive - airties.com\\PA Trimming\\4930 HW-ENG Results Analysis\\results_wo_dut9.csv'
filename='C:\\Users\samet.yildiz\\OneDrive - airties.com\\PA Trimming\\4960_PA_Trimming\\4960_pa_trimming_Sweep.csv'
filename='C:\\Users\samet.yildiz\\OneDrive - airties.com\\Air4960\\Air4960_5G_S1_revised.csv'

df = pd.read_csv(filename)
def filter_data(df, string_key,val_key):
    df_out=df
    count=0
    for i in string_key:
        df_out = df_out[df_out[string_key[i]] == val_key[i]]################ BURADA KALDIM
        count+=1
    return df_out

def print_pass_rate(val,lim):
    val_pass = val.query('-'+lim+'<Delta<'+lim)
    print("PASS RATE: " + str(round(val_pass.shape[0]/val.shape[0],3)))
    
def get_pass_data(val):
    val_pass = val.query('-1.5<Delta<1.5')
    return val_pass

def get_fail_data(val):
    val_pass = val.query('-1.5<Delta<1.5')
    return val_pass

def get_delta(val):
    return val['Delta']
def get_pass_delta(val):
    val_pass = val.query('-1.5<Delta<1.5')
    return val_pass['Delta']
def get_fail_delta(val):
    val_pass = val.query('Delta<-1.5 & Delta>1.5')
    return val_pass['Delta']
def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(100 * y)

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] is True:
        return s + r'$\%$'
    else:
        return s + '%'
def plot_data_histogram_single(data_series,val_try):
    title_str = ''
    for i in val_try:
        title_str = title_str + i + ' '
    fig, ax = plt.subplots()
    
    plt.axvline(x=1.5, color='k', linestyle='--')
    plt.axvline(x=-1.5, color='k', linestyle='--')
    
    ax.annotate(r'$+1.5dB$', xy=(1.4, 2),
            )
    ax.annotate(r'$-1.5dB$', xy=(-1.6, 2),
            )
    str_title = title_str+' Transmit Power Chain Distribution'
    plt.title(str_title, y=1.05)
    plt.xticks(np.arange(-4,4,0.5))
    plt.xlim(-4,4)
    plt.yticks(np.arange(0,2,0.2))
    plt.ylim(0,2)
    i=0
    color=['Green','Red','Blue','Black','Bright Cyan']
    colorline=['g','r','b','k','bc']
    sns.set()
    labels=['ANT0','ANT1','ANT2','ANT3']
    labels_short=['A0','A1','A2','A3']
    for data in data_series:
        sns.kdeplot(data,color=color[i], shade=True, label=labels[i])
        sns.distplot(data,color=color[i], bins=30)
        mean_val=round(np.mean(data),3)
        plt.axvline(x=mean_val, color=colorline[i], linestyle=':')  
        ax.annotate(r'$\mu_{'+labels_short[i]+'}='+str(mean_val)+'dB$', xy=(mean_val-0.2, 1.8-i*0.2),
            )
        ax.annotate(r'$\mu_{'+labels_short[i]+'}$'+ ': Mean Value of '+labels[i], xy=(2.4, 1.5-i*0.1),
            )
        
        i+=1  
        #n, bins, rectangles = plt.hist(data,color=color[i], density=True)

    plt.xlabel('Transmit Power Delta (dBm)\n[Measured Power - Target Power] ')
    plt.ylabel('Distribution Probability')
        
def plot_data_histogram(data_series,val_try):
    title_str = ''
    for i in val_try:
        title_str = title_str + i + ' '
    fig, ax = plt.subplots()
    
    plt.axvline(x=1.5, color='k', linestyle='--')
    plt.axvline(x=-1.5, color='k', linestyle='--')
    
    ax.annotate(r'$+1.5dB$', xy=(1.4, 2),
            )
    ax.annotate(r'$-1.5dB$', xy=(-1.6, 2),
            )
    str_title = title_str+'All Transmit Power Delta (PA Trimmed Tx Pow-Non-PA Trimed Tx Pow)'
    plt.title(str_title, y=1.05)
    plt.xticks(np.arange(-4,4,0.5))
    plt.xlim(-4,4)
    plt.yticks(np.arange(0,2,0.2))
    plt.ylim(0,2)
    i=0
    color=['Green','Red','Blue','Black','Bright Cyan']
    colorline=['g','r','b','k','bc']
    sns.set()
    labels=['ANT0','ANT1','ANT2','ANT3']
    labels_short=['A0','A1','A2','A3']
    for data in data_series:
        sns.kdeplot(data,color=color[i], shade=True, label=labels[i])
        sns.distplot(data,color=color[i], bins=30)
        mean_val=round(np.mean(data),3)
        plt.axvline(x=mean_val, color=colorline[i], linestyle=':')  
        ax.annotate(r'$\mu_{'+labels_short[i]+'}='+str(mean_val)+'dB$', xy=(mean_val-0.2, 1.8-i*0.2),
            )
        ax.annotate(r'$\mu_{'+labels_short[i]+'}$'+ ': Mean Value of '+labels[i] , xy=(2.4, 1.5-i*0.1),
            )
        
        i+=1  
        #n, bins, rectangles = plt.hist(data,color=color[i], density=True)
        
    

    plt.xlabel('Transmit Power Delta (dBm)')
    plt.ylabel('Distribution Probability')

"""pa_trim_no_ant0_20MHz = df_no['Delta']
pa_trim_yes_ant0_20MHz = df_yes['Delta']"""
test_try= ['']
val_try = ['']

count =0
test_arr={}
val_arr={}

#x1 = {0:'PA_Trimming'}
#x2 = {0:'PA_Trimming'}
x1 = {0:'Antenna'}
x2 = {0:'Antenna'}
x3 = {0:'Antenna'}
x4 = {0:'Antenna'}
x1_val = {0:'ANT0'}
x2_val = {0:'ANT1'}
x3_val = {0:'ANT2'}
x4_val = {0:'ANT3'}
if val_try[0]!='':
    for k in range(0,len(test_try)):
        x1[k+1] = test_try[k]
        x1_val[k+1] = val_try[k]
        x2[k+1] = test_try[k]
        x2_val[k+1] = val_try[k]
        x3[k+1] = test_try[k]
        x3_val[k+1] = val_try[k]
        x3[k+1] = test_try[k]
        x4_val[k+1] = val_try[k]

z1 = filter_data(df, x1,x1_val)
z2 = filter_data(df, x2,x2_val)
z3 = filter_data(df, x3,x3_val)
z4 = filter_data(df, x4,x4_val)
title_str = ''
for i in val_try:
    title_str = title_str + i + ' '

print("Total Pass rate")
print_pass_rate(df,'1.5')
print_pass_rate(df,'2')
print_pass_rate(df,'3')
print("ANT0 Pass rate")
print_pass_rate(z1,'1.5')
print_pass_rate(z1,'2')
print_pass_rate(z1,'3')
print("ANT1 Pass rate")
print_pass_rate(z2,'1.5')
print_pass_rate(z2,'2')
print_pass_rate(z2,'3')
print("ANT2 Pass rate")
print_pass_rate(z3,'1.5')
print_pass_rate(z3,'2')
print_pass_rate(z3,'3')
print("ANT3 Pass rate")
print_pass_rate(z4,'1.5')
print_pass_rate(z4,'2')
print_pass_rate(z4,'3')
"""print_pass_rate(z2)
print_pass_rate(z3)
print_pass_rate(z4)"""

x1_val_20 = get_delta(z1)
x2_val_20 = get_delta(z2)
x3_val_20 = get_delta(z3)
x4_val_20 = get_delta(z4)
"""sns.distplot(x_val_20, kde=True,bins=30)
sns.distplot(y_val_20, kde=True,bins=30)
plt.show()
"""

plot_data_histogram_single([x4_val_20],val_try)
"""plot_data_histogram_single([x2_val_20],val_try)
plot_data_histogram_single([x3_val_20],val_try)
plot_data_histogram_single([x4_val_20],val_try)"""
"""plot_data_histogram([x2_val_20],val_try)
plot_data_histogram([x3_val_20],val_try)
plot_data_histogram([x4_val_20],val_try)"""
plt.show()


"""plot_data_histogram([x_val_20,y_val_20],val_try)
plt.show()"""

"""
kwargs = dict(alpha=0.5, bins=100)
plt.hist(pa_trim_no_ant0_20MHz, **kwargs, color='g', label='ANT0 20MHz NO')
plt.hist(pa_trim_yes_ant0_20MHz, **kwargs, color='b', label='ANT0 20MHz YES')
plt.gca().set(title='Frequency Histogram of Diamond Depths', ylabel='Frequency')
plt.axvline(x=1.5, color='r', linestyle=':')
plt.axvline(x=-1.5, color='r', linestyle=':')
plt.show()"""

"""sns.distplot(pa_trim_no_ant0_20MHz,color='red')
sns.distplot(pa_trim_yes_ant0_20MHz,  color='blue')"""
# manipulate
