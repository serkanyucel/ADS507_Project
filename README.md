# ADS507 - Project
Serkan Yücel

# Process

In this project, my aim was to find all schools (excluded universities) in İzmir with the state level. I searched the queries based on the primary school, middle school and high school to prevent the data losses. This caused to some duplication problems but I tried to handle them manually as possible as I could. 

Google API is providing the only 60 results. If the users need to more results, they have to pay the money. Therefore, I could not determine the per-capita schools value in İzmir.

The packages you need to runn the codes are listed below.

branca==0.3.1
certifi==2019.11.28
chardet==3.0.4
folium==0.10.1
idna==2.8
Jinja2==2.10.3
MarkupSafe==1.1.1
numpy==1.18.0
python-google-places==1.4.1
requests==2.22.0
six==1.13.0
urllib3==1.25.7

"locationfindings.py" is essential to find the schools in a specific location. The results of this query searchings are merged in a csv file.
"map.py" is essential to see the all csv files that include the information for the schools in İzmir. All csv files are demonstrated on the colored map that is filled by the total number of the schools. 
