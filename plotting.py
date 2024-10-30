import numpy as np
import matplotlib.pyplot as plt
import csv
import os



#Definin the file paths:
Amplitude_response_path    = "Malinger\\spectrum_butterworth_filter.csv"




#Defining function to convert csv file to lists (Amplitude response):
def file_to_list_Response(file, freq_column, magnetude_column):
    freq_list=[]
    magnetude_list=[]
    n=0
    with open(file, 'r') as file:
        data=csv.reader(file)
        for row in data:
            
            if len(row)==0:
                continue
            elif not (row[0][0].isdigit()):
                continue
            freq_list.append(float(row[freq_column]))
            magnetude_list.append(float(row[magnetude_column]))
        return freq_list, magnetude_list



freq_list, amplitude_in = file_to_list_Response(Amplitude_response_path, 0, 1)
freq_list, amplitude_out = file_to_list_Response(Amplitude_response_path, 0, 2)


N=0
A_max =0
A_max_freq =0

for i in range(len(freq_list)):
    if amplitude_out[i]>A_max:
        A_max = amplitude_out[i]
        A_max_freq = freq_list[i]
    if freq_list[i]>4000:
        N = i
        break

freq_list = freq_list[0:N]
amplitude_in = amplitude_in[0:N]
amplitude_out = amplitude_out[0:N]

#creating folder for graphs:
folder_path = 'Graphs'
os.makedirs(folder_path, exist_ok=True)

#Plottign and saving graphs:

plt.figure()
plt.autoscale(tight=True)
plt.ylim(-22,5)

plt.semilogx(freq_list, amplitude_out)
plt.semilogx(freq_list, amplitude_in )



plt.title('Amplitude Response')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude [dB]')
plt.legend(['$v_2$', '$v_1$'])
plt.grid()
plt.savefig('Graphs\Amplitude_response.png')
plt.show()

print(A_max, A_max_freq)