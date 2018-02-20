import platform
from metoffice.download_data import download_data
from metoffice.clean_data import clean_data
from metoffice.transform_data import fwf_to_csv, consolidate_data
from metoffice.models import Weather, Climate
from metoffice.load import csv_to_weather, csv_to_climate
from graphos.sources.model import ModelDataSource
from django.template import loader
from django.http import HttpResponse
from graphos.renderers.gchart import LineChart, BarChart, ColumnChart, CandlestickChart


# Create your views here
def graph_climate(request):
    # DataSource object
    queryset = Climate.objects.raw("SELECT * FROM store_climate \
                                   where year>1000 \
                                   and year<9999  \
                                   group by season,region \
                                   order by season,region")

    #    data_source = ModelDataSource(queryset, fields= ['season', 'tmax', 'tmin', ] )
    data_source_tmin = ModelDataSource(queryset, fields=['season', 'tmin'])
    data_source_tmax = ModelDataSource(queryset, fields=['season', 'tmax'])
    data_source_tmean = ModelDataSource(queryset, fields=['season', 'tmean'])
    data_source_rainfall = ModelDataSource(
        queryset, fields=['season', 'rainfall'])
    data_source_sunshine = ModelDataSource(
        queryset, fields=['season', 'sunshine'])

    # Chart object

    chart_tmin = ColumnChart(
        data_source_tmin,
        options={
            'title': 'Min. Temperature (England,Scotland,UK,Wales - 1911-2017)'
        })
    chart_tmax = ColumnChart(
        data_source_tmax,
        options={
            'title': 'Max. Temperature (England,Scotland,UK,Wales - 1911-2017)'
        })
    chart_tmean = ColumnChart(
        data_source_tmean,
        options={
            'title': 'Mean Temperature (England,Scotland,UK,Wales - 1911-2017)'
        })
    chart_rainfall = ColumnChart(
        data_source_rainfall,
        options={
            'title': 'Rainfall (England,Scotland,UK,Wales - 1911-2017)'
        })
    chart_sunshine = ColumnChart(
        data_source_sunshine,
        options={
            'title': 'Sunshine (England,Scotland,UK,Wales - 1911-2017)'
        })

    context = {
        'chart_tmin': chart_tmin,
        'chart_tmax': chart_tmax,
        'chart_tmean': chart_tmean,
        'chart_rainfall': chart_rainfall,
        'chart_sunshine': chart_sunshine
    }

    template = loader.get_template('metoffice/graphs_climate.html')

    return HttpResponse(template.render(context, request))

#===============================Not Using this approach========================
def graph_weather(request):

    # Original DataSource object
    # queryset = Climate.objects.filter( region = 'UK',year__gt=1000, year__lt=9999, )
    # queryset = queryset.exclude(season__in=['SUM', 'WIN', 'AUT','ANN', 'SPR'])

    queryset = Weather.objects.raw("SELECT * FROM store_weather \
                                   where year>1000 \
                                   and year<9999  \
                                   and value <9999 \
                                   and attribute = 'tmin' \
                                   order by region, year, season")

    #    data_source = ModelDataSource(queryset, fields= ['season', 'tmax', 'tmin', ] )
    data_source = ModelDataSource(queryset, fields=[ 'season','value'])

    # Chart object
    chart = ColumnChart(
        data_source, options={
            'title': 'Temperature (Min - 1911-2017)'
        })

    context = {'chart': chart}
    template = loader.get_template('metoffice/graphs_weather.html')

    return HttpResponse(template.render(context, request))
#==============================================================================

def main(request):
    """ Download, Extract, Clean, Transform, and Load data."""
    regions = ['UK', 'England', 'Wales', 'Scotland']
    attributes = ['Tmax', 'Tmin', 'Tmean', 'Sunshine', 'Rainfall']

    # check in which pc i'm working
    if platform.system() == 'Windows':
        # data_loc = "D:\Toran\WorkSpace\practice\interview\kisanhub\data"
        data_loc = "./data"
        proxies = {
            "http": "http://toran.sahu:L440Qthink@10.74.91.103:80",
            "https": "http://toran.sahu:L440Qthink@10.74.91.103:80",
        }
    else:
        data_loc = "./data"
        proxies = {
            "http": None,
            "https": None,
        }

    #messages.info(request, 'Three credits remain in your account.')
    print(download_data.__doc__)
    download_data(regions, attributes, data_loc, proxies)
    print(clean_data.__doc__)
    clean_data(data_loc)
    print(fwf_to_csv.__doc__)
    fwf_to_csv(data_loc)
    
# =============================Not Using this approach=========================
#     print(consolidate_data.__doc__)
#     consolidate_data(data_loc)
#     csv_to_weather(data_loc)
# =============================================================================
    
    print("Data loading to ORM started, please wait till completions.")
    csv_to_climate(data_loc)
    print("Data loaded to ORM")
    return HttpResponse("Data loaded to ORM")
