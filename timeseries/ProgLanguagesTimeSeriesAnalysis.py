import pandas as pd
import matplotlib.pyplot as plt
import timeseries.TimeSeriesAnalysisCommon as tsc

pd.set_option('display.max_columns', 5)

input_path = "/home/dharani/Desktop/ProgLanguagesTrends.csv"
data_columns = ['WEEK', 'PYTHON', 'JAVA', 'R']
skip_lines = 1

keyword_searches_df = tsc.get_data_frame(input_path, skip_lines, data_columns)
# print(keyword_searches_df.head())
keyword_searches_df.WEEK = pd.to_datetime(keyword_searches_df.WEEK)
keyword_searches_df.set_index('WEEK', inplace=True)
# print(keyword_searches_df.head())
# print(keyword_searches_df.info())
keyword_searches_python = keyword_searches_df[['PYTHON']]
keyword_searches_java = keyword_searches_df[['JAVA']]
keyword_searches_r = keyword_searches_df[['R']]
# print(keyword_searches_python.head())
# print(keyword_searches_java.head())
# print(keyword_searches_r.head())

keyword_python_plt = tsc.plot_data_frame(keyword_searches_python,
                                         "PYTHON - KeyWord Searches - Last 5 Years",
                                         "YEAR", "NoOfSearches")
keyword_java_plt = tsc.plot_data_frame(keyword_searches_java,
                                       "JAVA - KeyWord Searches - Last 5 Years",
                                       "YEAR", "NoOfSearches")
keyword_r_plt = tsc.plot_data_frame(keyword_searches_r,
                                    "R - KeyWord Searches - Last 5 Years",
                                    "YEAR", "NoOfSearches")
allKeyWords_plt = tsc.plot_data_frame(keyword_searches_df,
                                      "PYTHON & JAVA & R - KeyWord Searches - Last 5 Years",
                                      "YEAR", "NoOfSearches")



fig = plt.figure()
python_plt = fig.add_subplot(231)
python_plt.plot(keyword_searches_python,linewidth=0.5,color='blue')
plt.xlabel("YEAR"); plt.ylabel("SearchCount");plt.title("Python - Searches")

java_plt = fig.add_subplot(232)
java_plt.plot(keyword_searches_java,linewidth=0.5,color='orange')
plt.xlabel("YEAR");plt.title("Java - Searches")

r_plt = fig.add_subplot(233)
r_plt.plot(keyword_searches_r,linewidth=0.5,color='green')
plt.xlabel("YEAR"); plt.title("R - Searches")

from matplotlib.gridspec import GridSpec
gs = GridSpec(2, 2, figure=fig)
all_plt = fig.add_subplot(gs[1, :])
all_plt.plot(keyword_searches_df,linewidth=0.5)
all_plt.legend(keyword_searches_df)
plt.xlabel("YEAR"); plt.ylabel("SearchCount");plt.title("Python/Java/R - Searches")
plt.show()


#"PYTHON Trendd vs Searches - Last 5 Years" 
keyword_searches_python_roll_avg = keyword_searches_python.rolling(52).mean()
# print(keyword_searches_python_roll_avg)

keyword_searches_python_trend = pd.concat(
    [keyword_searches_python,keyword_searches_python_roll_avg],axis=1)
keyword_searches_python_trend.columns = ['PYTHON','PythonTrend']
print(keyword_searches_python_trend)


python_trend_plt = tsc.plot_data_frame(keyword_searches_python_trend,
                                       "PYTHON Trendd vs Searches - Last 5 Years",
                                       "YEAR", "NoOfSearches")
python_trend_plt.show()

print(keyword_searches_python)
print(keyword_searches_python.diff())
keyword_searches_python.diff().plot(figsize=(20,10), linewidth=1, fontsize=20)
plt.xlabel('Year', fontsize=20);
plt.title("FOD")
plt.show()

keyword_searches_df.diff().plot(figsize=(20,10), linewidth=1, fontsize=20)
plt.xlabel('Year', fontsize=20);
plt.title("FOD/Differencing")
plt.show()

print(keyword_searches_df.diff().corr())

ax = pd.plotting.autocorrelation_plot(keyword_searches_python);
ax.set_xlim([0, 30])
plt.show()


