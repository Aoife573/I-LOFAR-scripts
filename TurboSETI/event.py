from turbo_seti.find_event.find_event_pipeline import find_event_pipeline
import blimpy
import turbo_seti
import turbo_seti.find_doppler.seti_event as turbo
import turbo_seti.find_event as find

# A list of all the .dat files that turboSETI produced
dat_file_list = ["TESS.dat"]


check_zero_drift = False
filter_threshold = 1
SNR_cut = 10


event_dataframe = find.find_events(dat_file_list,
                       SNR_cut=SNR_cut,
                       check_zero_drift=check_zero_drift,
                       filter_threshold=filter_threshold,
                       on_off_first='OFF')

name = "output"
id_num = "-1"

if check_zero_drift == True:
    event_csv_string = name + '_' + id_num + '_f' + str(filter_threshold) + '_snr' + str(SNR_cut) + '_zero' + '.csv'
else:
    event_csv_string = name + '_' + id_num + '_f' + str(filter_threshold) + '_snr' + str(SNR_cut) + '.csv'
event_dataframe

event_dataframe.to_csv(event_csv_string)

#event_dataframe.iloc[0:10].to_csv('output_snr10.csv') 
# The filename must have the same format as the .csv outputed by find_event_pipeline

#event_dataframe.iloc[0:10]

