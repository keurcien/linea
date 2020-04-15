from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Min, Max
import datetime
from .models import User, Weight

# Create your views here.

def index(request):
    return render(request, 'scale/index.html')

def chart_data(request):

    def daterange():
        dates_ = Weight.objects.aggregate(Min('date'), Max('date'))
        start_date = dates_.get('date__min')
        end_date = dates_.get('date__max')
        delta = end_date - start_date
        return [(start_date + datetime.timedelta(x)).strftime('%Y-%m-%d') for x in range(delta.days + 1)]
    
    dates_ = daterange()

    def process_series(dates_, values):
        res = [None for d in dates_]
        for v in values:
            d = v['date'].strftime("%Y-%m-%d")
            res[dates_.index(d)] = v['value']
        return res

    users = User.objects.values('id', 'name', 'hex_color')
    chart_series = []

    for u in users:
        chart_series.append(
            {
                'name': u.get('name'),
                'data': process_series(dates_, Weight.objects.filter(user_id=u.get('id')).values('value', 'date')),
                'color': u.get('hex_color'),
                'marker': { 'symbol': 'circle' }
            }
        )

    chart = {
        'chart': { 'type': 'line', 'style': { 'fontFamily': 'Roboto'}, 'height': 600 },
        'title': { 'text': 'Courbes de masse', 'style': { 'fontSize': 25, 'fontWeight': 700 }},
        'series': chart_series,
        'xAxis': {
            'categories': dates_,
            'gridLineWidth': 1,
            'labels': {
                'style': {
                    'fontSize': 12,
                    'fontWeight': 700
                }
            }
        },
        'yAxis': {
            'title': { 'text': 'Masse (kg)', 'style': { 'fontSize': 20, 'fontWeight': 700 }},
            'labels': {
                'style': {
                    'fontSize': 12,
                    'fontWeight': 700
                }
            }
        },
        'legend': {
            'itemStyle': {
                'fontSize': 15 
            }
        },
        'tooltip': {
            'style': {
                'fontSize': 18
            }
        },
        'plotOptions': {
            'series': {
                'connectNulls': True
            }
        }
    }

    return JsonResponse(chart)
