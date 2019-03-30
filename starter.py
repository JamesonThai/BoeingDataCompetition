import pandas as pd

def get_csv():
	airline_delay_causes_df = pd.read_csv('bdc/airline_delay_causes.csv')
	flight_sample_df = pd.read_csv('bdc/flight sample.csv') 
	airport_id_df = pd.read_csv('bdc/L_AIRPORT_ID.csv')
	cancellation_df = pd.read_csv('bdc/L_CANCELLATION.csv')
	carriers_df = pd.read_csv('bdc/L_UNIQUE_CARRIERS.csv')
	variable_df = pd.read_csv('bdc/VariableDescription.csv')
	md_df = pd.read_csv('bdc/monthly data/133080461_T_ONTIME_REPORTING 2.csv')
	md_df2 = pd.read_csv('bdc/monthly data/133080461_T_ONTIME_REPORTING 3.csv')
	# Note md_df3 HAS A COLUMN MIX TYPE
	md_df3 = pd.read_csv('bdc/monthly data/133080461_T_ONTIME_REPORTING 6.csv')
	md_df4 = pd.read_csv('bdc/monthly data/133081407_T_ONTIME_REPORTING 4.csv')
	md_df5 = pd.read_csv('bdc/monthly data/133081407_T_ONTIME_REPORTING 5.csv')
	md_df6 = pd.read_csv('bdc/monthly data/133081407_T_ONTIME_REPORTING 7.csv')
	md_df7 = pd.read_csv('bdc/monthly data/133081407_T_ONTIME_REPORTING 8.csv')
	md_df8 = pd.read_csv('bdc/monthly data/133081407_T_ONTIME_REPORTING 9.csv')
	md_df9 = pd.read_csv('bdc/monthly data/133081407_T_ONTIME_REPORTING 10.csv')
	md_df10 = pd.read_csv('bdc/monthly data/133081407_T_ONTIME_REPORTING 11.csv')
	md_df11 = pd.read_csv('bdc/monthly data/133081407_T_ONTIME_REPORTING 12.csv')
	md_df12 = pd.read_csv('bdc/monthly data/560702993_T_ONTIME_REPORTING 1.csv')
	
	return airline_delay_causes_df, flight_sample_df, airport_id_df, cancellation_df, carriers_df, variable_df, md_df, md_df2, md_df3, md_df4, md_df5, md_df6, md_df7, md_df8, md_df9, md_df10, md_df11, md_df12

def main():
	adc_df, fs_df, ai_df, cancellation_df, carriers_df, variable_df, md_df, md_df2, md_df3, md_df4, md_df5, md_df6, md_df7, md_df8, md_df9, md_df10, md_df11, md_df12 = get_csv()
	
	print(head(adc_df))

if __name__ == "__main__":
	main()