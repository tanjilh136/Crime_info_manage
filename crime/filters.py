import django_filters
from django_filters import DateFilter
# from django_filters import CharField

from .models import *

class CrimeFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="Time", lookup_expr='gte')
    end_date = DateFilter(field_name="Time", lookup_expr='lte')
    # for carecter field search
    # note = CharField(field_name='note', lookup_expr='icontains')


    class Meta:
        model = fileing
        fields = '__all__'
        exclude = ['cName','cRoad_Block_Sector', 'cCity_Village_House', 'cPost_Office', 
        'cPostal_Code', 'cDistrict', 'cPolice_Station', 'cCountry', 'Crime_Descrip', 
        'sRoad_Block_Sector', 'sCity_Village_House', 'sPost_Office',
         'sPostal_Code', 'sPolice_Station', 'sCountry','date'] 
