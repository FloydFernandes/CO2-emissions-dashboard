from numpy import result_type
import pygal
import os
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima
from statsmodels.tools.eval_measures import rmse
import warnings
import numpy as np



warnings.filterwarnings("ignore") 



df = pd.read_csv('co2_emission.csv',index_col=2, parse_dates=True)
df.rename(columns={"Annual CO₂ emissions (tonnes )": "CO2"}, inplace=True)
df = df.drop(columns="Code")
countries = ['India',"China", 'United States', 'United Arab Emirates', 'South Africa', "Canada", "Brazil", 'United Kingdom', 
             "Australia", 'South Korea', "Japan", 'Afghanistan', 'Saudi Arabia', "Azerbaijan", "Russia", "Germany", 'Republic of the Congo', 'Libya', "Turkey", "Egypt"
]

df_top_20 = df.loc[df['Entity'].isin(countries),:]


def get_country_df(country):
        global df
        df1 = df.loc[df["Entity"] == country]
        return df1

def make_model(train, best_vals, P=0, D=0, Q=0, s=10):
  model = ARIMA(endog=list(train),order=best_vals, seasonal_order= (P, D, Q,s)) 
  return model

def best_seasonal_vals(train, best_vals):
        P = list(range(0,3))
        D = list(range(0,2))
        Q = list(range(0,3))

        i1 = 0
        i2 = 0
        i3 = 0

        seasonal_optimization = {}

        while i1 < len(P):
                while i2 < len(D):
                        while i3 < len(Q):
                                modeling = make_model(train, best_vals, i1, i2, i3)
        

                                model = modeling.fit()

                                aic = model.aic
                                seasonal_optimization[(i1, i2, i3, 10)] = aic

                                i3 += 1

                        i3 = 0
                        i2 += 1
                i2 = 0
                i1 += 1


        best = min(seasonal_optimization.values())

        for k, v in seasonal_optimization.items():
                if v == best:
                        return k 

def get_missing_years(df):
        missing_years=[]
        i = df.index.year[0]
        for x in df.index.year:
                if i != x:
                        missing_years.append(i)
                i+=1
        return missing_years
                        
def arima_model(country, user_input=50):
        df = get_country_df(country)
        missing_years = get_missing_years(df)

        for x in missing_years:
                time = pd.to_datetime(x,format="%Y")
                df.loc[time,:] = np.nan

        df = df.sort_index(ascending=True)

        df = df.interpolate(method ='linear', limit_direction ='forward', limit = 100)

        df = df.drop(columns="Entity")

        size = int(df.shape[0] * 0.2)
        train = df.iloc[:-size,0]
        test = df.iloc[-(size - 1):,0]

        model = auto_arima(train, start_p=0, start_q=0, max_p=10, max_q=10, max_d=4, trace=True, m=1)
        best_order_vals = model.order
        best_seasonal_values = best_seasonal_vals(train, best_order_vals)
        model_train = ARIMA(train,order=best_order_vals, seasonal_order=best_seasonal_values) 
        fitted_model = model_train.fit()
        info =  fitted_model.model_orders    
        
        start = len(train)
        end = len(train) + len(test) -1
        predictions = fitted_model.predict(start,end,typ='levels').rename('ARIMA')
        
        errors = rmse(test,predictions)

        model_final_fitted = ARIMA(df,order=best_order_vals, seasonal_order=best_seasonal_values).fit()



        forecast = model_final_fitted.predict(len(df)-1,len(df)+(user_input-1),typ='levels').rename('ARIMA forecast')

        fr_df = forecast.to_frame()

        fr_dict = dict(zip(list(fr_df.index.year), list(fr_df["ARIMA forecast"])))

        
        
        for_output = [fr_dict, errors, best_order_vals, best_seasonal_values]
       
        return for_output
        






def find_max_for_worldmap(df=df):
        global countries
        maxi = {}

        for c in countries:
                maxi[c] = max(df.loc[df['Entity'] == c, "CO2"])
  
        return maxi


def get_worldmap():
        global df
        worldmap =  pygal.maps.world.World()

  
        # set the title of the map
        worldmap.title = 'Peak CO2 Pollution levels for 20 Countries'

        vals = find_max_for_worldmap(df)


        
        # adding the countries
        worldmap.add("CO2",{
                'in' : vals["India"],
                'cn' : vals["China"],
                'us' : vals["United States"],
                'ae' : vals["United Arab Emirates"],
                'za' : vals["South Africa"],
                'ca' : vals["Canada"],
                'br' : vals["Brazil"],
                'gb' : vals["United Kingdom"],
                'au' : vals["Australia"],
                'kp' : vals["South Korea"],
                'jp' : vals["Japan"],
                'af' : vals["Afghanistan"],
                'sa' : vals["Saudi Arabia"],
                'ru' : vals["Russia"],
                'de' : vals["Germany"],
                'cd' : vals["Republic of the Congo"],
                'ly' : vals["Libya"],
                'tr' : vals["Turkey"],
                'eg' : vals["Egypt"],
                'az' : vals["Azerbaijan"]
        })
        # Changing the directory to static
        cwd = os.getcwd()
        cwd_list = cwd.split("\\")
        if cwd_list[-1] == "static":
                cwd_list.pop()
                cwd = '\\'.join(cwd_list)
                static_dir = cwd + "\static"
                os.chdir(static_dir)
        else:
                static_dir = cwd + "\static"
                os.chdir(static_dir)

        # save into the file
        worldmap.render_to_file('world.svg')




def raw_chart(country):
        df1 = get_country_df(country)
        raw_chart_dict = dict(zip(list(df1.index.year), list(df1.CO2)))
        return raw_chart_dict

        