from django.conf import settings

def type_processor(request):
    print('useless')
    return {'TYPE': settings.TYPE}
