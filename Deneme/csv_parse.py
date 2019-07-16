import csv
from scipy import stats  
import numpy as np  
import matplotlib.pylab as plt2
import matplotlib.pyplot as plt
import pandas as pd
filename='C:\\Users\samet.yildiz\\OneDrive - airties.com\\PA Trimming\\4930 HW-ENG Results Analysis\\Results_evaluation.csv'

df = pd.read_csv(filename)
"""
print(df['Delta'].plot(kind='hist',bins=100))
plt.xlabel('delta values')
plt.show()
"""#

pa_trimming_NO = df[df.PA_Trimming == 'NO']
pa_trimming_YES = df[df.PA_Trimming == 'YES']

pa_trimming_NO_in_limit = pa_trimming_NO.query('-1.5<Delta<1.5')
pa_trimming_YES_in_limit = pa_trimming_YES.query('-1.5<Delta<1.5')

def get_filter_Data_Count(variable,criteria,key):
    if criteria == "Sample_No":
        return round(variable[variable.Sample_No == key].shape[0],3)
    elif criteria == "Antenna":
        return round(variable[variable.Antenna == key].shape[0],3)
    elif criteria == "BW":
        return round(variable[variable.BW == key].shape[0],3)
    elif criteria == "Channel":
        return round(variable[variable.Antenna == key].shape[0],3)
    elif criteria == "Modulation":
        return round(variable[variable.BW == key].shape[0],3)
    
def get_filtered_delta(variable,criteria,key):
    if criteria == "Sample_No":
        return variable[variable.Sample_No == key]
    elif criteria == "Antenna":
        return variable[variable.Antenna == key]
    elif criteria == "BW":
        return variable[variable.BW == key]
    elif criteria == "Channel":
        return variable[variable.Antenna == key]
    elif criteria == "Modulation":
        return variable[variable.BW == key]  

dut_1_before_trim_rate = round(get_filter_Data_Count(pa_trimming_NO_in_limit,"Sample_No","DUT-1")/ get_filter_Data_Count(pa_trimming_NO,"Sample_No","DUT-1"),3)
dut_2_before_trim_rate = round(get_filter_Data_Count(pa_trimming_NO_in_limit,"Sample_No","DUT-2")/ get_filter_Data_Count(pa_trimming_NO,"Sample_No","DUT-2"),3)
dut_3_before_trim_rate = round(get_filter_Data_Count(pa_trimming_NO_in_limit,"Sample_No","DUT-3")/ get_filter_Data_Count(pa_trimming_NO,"Sample_No","DUT-3"),3)
dut_4_before_trim_rate = round(get_filter_Data_Count(pa_trimming_NO_in_limit,"Sample_No","DUT-4")/ get_filter_Data_Count(pa_trimming_NO,"Sample_No","DUT-4"),3)
dut_5_before_trim_rate = round(get_filter_Data_Count(pa_trimming_NO_in_limit,"Sample_No","DUT-5")/ get_filter_Data_Count(pa_trimming_NO,"Sample_No","DUT-5"),3)
dut_6_before_trim_rate = round(get_filter_Data_Count(pa_trimming_NO_in_limit,"Sample_No","DUT-6")/ get_filter_Data_Count(pa_trimming_NO,"Sample_No","DUT-6"),3)
dut_7_before_trim_rate = round(get_filter_Data_Count(pa_trimming_NO_in_limit,"Sample_No","DUT-7")/ get_filter_Data_Count(pa_trimming_NO,"Sample_No","DUT-7"),3)
dut_9_before_trim_rate = round(get_filter_Data_Count(pa_trimming_NO_in_limit,"Sample_No","DUT-9")/ get_filter_Data_Count(pa_trimming_NO,"Sample_No","DUT-9"),3)
dut_10_before_trim_rate = round(get_filter_Data_Count(pa_trimming_NO_in_limit,"Sample_No","DUT-10")/ get_filter_Data_Count(pa_trimming_NO,"Sample_No","DUT-10"),3)

dut_1_after_trim_rate = round(get_filter_Data_Count(pa_trimming_YES_in_limit,"Sample_No","DUT-1")/ get_filter_Data_Count(pa_trimming_YES,"Sample_No","DUT-1"),3)
dut_2_after_trim_rate = round(get_filter_Data_Count(pa_trimming_YES_in_limit,"Sample_No","DUT-2")/ get_filter_Data_Count(pa_trimming_YES,"Sample_No","DUT-2"),3)
dut_3_after_trim_rate = round(get_filter_Data_Count(pa_trimming_YES_in_limit,"Sample_No","DUT-3")/ get_filter_Data_Count(pa_trimming_YES,"Sample_No","DUT-3"),3)
dut_4_after_trim_rate = round(get_filter_Data_Count(pa_trimming_YES_in_limit,"Sample_No","DUT-4")/ get_filter_Data_Count(pa_trimming_YES,"Sample_No","DUT-4"),3)
dut_5_after_trim_rate = round(get_filter_Data_Count(pa_trimming_YES_in_limit,"Sample_No","DUT-5")/ get_filter_Data_Count(pa_trimming_YES,"Sample_No","DUT-5"),3)
dut_6_after_trim_rate = round(get_filter_Data_Count(pa_trimming_YES_in_limit,"Sample_No","DUT-6")/ get_filter_Data_Count(pa_trimming_YES,"Sample_No","DUT-6"),3)
dut_7_after_trim_rate = round(get_filter_Data_Count(pa_trimming_YES_in_limit,"Sample_No","DUT-7")/ get_filter_Data_Count(pa_trimming_YES,"Sample_No","DUT-7"),3)
dut_9_after_trim_rate = round(get_filter_Data_Count(pa_trimming_YES_in_limit,"Sample_No","DUT-9")/ get_filter_Data_Count(pa_trimming_YES,"Sample_No","DUT-9"),3)
dut_10_after_trim_rate = round(get_filter_Data_Count(pa_trimming_YES_in_limit,"Sample_No","DUT-10")/ get_filter_Data_Count(pa_trimming_YES,"Sample_No","DUT-10"),3)

print("Before PA Trimming DUT-1: " + str(dut_1_before_trim_rate)+", After PA Trimming DUT-1: " + str(dut_1_after_trim_rate) +", Increase rate DUT-1: " + str(1-dut_1_before_trim_rate/dut_1_after_trim_rate))
print("Before PA Trimming DUT-2: " + str(dut_2_before_trim_rate)+", After PA Trimming DUT-2: " + str(dut_2_after_trim_rate)+", Increase rate DUT-1: " + str(1-dut_2_before_trim_rate/dut_2_after_trim_rate))
print("Before PA Trimming DUT-3: " + str(dut_3_before_trim_rate)+", After PA Trimming DUT-3: " + str(dut_3_after_trim_rate)+", Increase rate DUT-1: " + str(1-dut_3_before_trim_rate/dut_3_after_trim_rate))
print("Before PA Trimming DUT-4: " + str(dut_4_before_trim_rate)+", After PA Trimming DUT-4: " + str(dut_4_after_trim_rate)+", Increase rate DUT-1: " + str(1-dut_4_before_trim_rate/dut_4_after_trim_rate))
print("Before PA Trimming DUT-5: " + str(dut_5_before_trim_rate)+", After PA Trimming DUT-5: " + str(dut_5_after_trim_rate)+", Increase rate DUT-1: " + str(1-dut_5_before_trim_rate/dut_5_after_trim_rate))
print("Before PA Trimming DUT-6: " + str(dut_6_before_trim_rate)+", After PA Trimming DUT-6: " + str(dut_6_after_trim_rate)+", Increase rate DUT-1: " + str(1-dut_6_before_trim_rate/dut_6_after_trim_rate))
print("Before PA Trimming DUT-7: " + str(dut_7_before_trim_rate)+", After PA Trimming DUT-7: " + str(dut_7_after_trim_rate)+", Increase rate DUT-1: " + str(1-dut_7_before_trim_rate/dut_7_after_trim_rate))
print("Before PA Trimming DUT-9: " + str(dut_9_before_trim_rate)+", After PA Trimming DUT-9: " + str(dut_9_after_trim_rate)+", Increase rate DUT-1: " + str(1-dut_9_before_trim_rate/dut_9_after_trim_rate))
print("Before PA Trimming DUT-10: " + str(dut_10_before_trim_rate)+", After PA Trimming DUT-10: " + str(dut_10_after_trim_rate)+", Increase rate DUT-1: " + str(1-dut_10_before_trim_rate/dut_10_after_trim_rate))

ant0_no= get_filter_Data_Count(pa_trimming_NO,"Antenna","ANT0")
ant1_no= get_filter_Data_Count(pa_trimming_NO,"Antenna","ANT1")
ant2_no= get_filter_Data_Count(pa_trimming_NO,"Antenna","ANT2")
ant3_no= get_filter_Data_Count(pa_trimming_NO,"Antenna","ANT3")

ant0_yes= get_filter_Data_Count(pa_trimming_YES,"Antenna","ANT0")
ant1_yes= get_filter_Data_Count(pa_trimming_YES,"Antenna","ANT1")
ant2_yes= get_filter_Data_Count(pa_trimming_YES,"Antenna","ANT2")
ant3_yes= get_filter_Data_Count(pa_trimming_YES,"Antenna","ANT3")


ant0_pass_no = get_filter_Data_Count(pa_trimming_NO_in_limit,"Antenna","ANT0")
ant1_pass_no = get_filter_Data_Count(pa_trimming_NO_in_limit,"Antenna","ANT1")
ant2_pass_no = get_filter_Data_Count(pa_trimming_NO_in_limit,"Antenna","ANT2")
ant3_pass_no = get_filter_Data_Count(pa_trimming_NO_in_limit,"Antenna","ANT3")

ant0_pass_yes = get_filter_Data_Count(pa_trimming_YES_in_limit,"Antenna","ANT0")
ant1_pass_yes = get_filter_Data_Count(pa_trimming_YES_in_limit,"Antenna","ANT1")
ant2_pass_yes = get_filter_Data_Count(pa_trimming_YES_in_limit,"Antenna","ANT2")
ant3_pass_yes = get_filter_Data_Count(pa_trimming_YES_in_limit,"Antenna","ANT3")

print("Before PA Trimming ANT0: " + str(round(ant0_pass_no/ant0_no,3))+", After PA Trimming ANT0: " + str(round(ant0_pass_yes/ant0_yes,3)))
print("Before PA Trimming ANT1: " + str(round(ant1_pass_no/ant1_no,3))+", After PA Trimming ANT1: " + str(round(ant1_pass_yes/ant1_yes,3)))
print("Before PA Trimming ANT2: " + str(round(ant2_pass_no/ant2_no,3))+", After PA Trimming ANT2: " + str(round(ant2_pass_yes/ant2_yes,3)))
print("Before PA Trimming ANT3: " + str(round(ant3_pass_no/ant3_no,3))+", After PA Trimming ANT3: " + str(round(ant3_pass_yes/ant3_yes,3)))


#print(pa_trimming_NO_in_limit[pa_trimming_NO_in_limit.Modulation == 'MCS8NSS1'])
#print("PA Trimming results : " + str(pa_trimming_YES_in_limit.shape[0]) + " PASS, " + str(pa_trimming_YES.shape[0]- pa_trimming_YES_in_limit.shape[0] )+ " FAIL, Success Ratio:" + str(pa_trimming_YES_in_limit.shape[0]/pa_trimming_YES.shape[0]) )
#print("Non-PA Trimming results : " + str(df_filtered_no.shape[0]) + " PASS, " + str(pa_trimming_NO.shape[0]- df_filtered_no.shape[0] )+ " FAIL, Success Ratio:" + str(df_filtered_no.shape[0]/pa_trimming_NO.shape[0]))
# filtering with query method 
