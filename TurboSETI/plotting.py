#from turbo_seti.find_event.plot_event_pipeline import plot_event_pipeline
from turbo_seti_sofia.plot_event_pipeline import plot_event_pipeline


fil_files = ["Parkes_58027_22021_ALPHACEN_S_fine.h5"
                 ,"Parkes_58028_22362_ALPHACEN_R_fine.h5"
                 ,"Parkes_58028_22700_ALPHACEN_S_fine.h5"
                 ,"Parkes_58028_23041_ALPHACEN_R_fine.h5"
                 ,"Parkes_58028_23380_ALPHACEN_S_fine.h5"
                 ,"Parkes_58028_23721_ALPHACEN_R_fine.h5"]

fils_list_string = "fil_files.lst"
plot_event_pipeline('condensed_A_f2_snr10.csv',
                    fils_list_string,
                    user_validation=True)

