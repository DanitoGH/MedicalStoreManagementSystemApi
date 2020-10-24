from datetime import timedelta, date, datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


from ordermanagement.models import CreateOrder


@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def api_get_client_statistics_view(request, c_id):

    if request.user.is_admin and request.user.is_staff:
        return Response({'response': "Sorry, you don't have permission to access this data!"})
        
    try:
        d1 = date.today()
        today = d1.day
        yesterday = (d1 - timedelta(hours=24)).day
        one_week_ago = (d1 - timedelta(days=7))
        month = d1.month
        year = d1.year
            

        # ALL ORDERS OBJECT
        orders = CreateOrder.objects.all()

        #TOTAL ORDER COUNTS
        total_orders = orders.filter(client_id=c_id).count()
        total_delivered_orders = orders.filter(client_id=c_id, status='Delivered').count()
        total_pending_orders = orders.filter(client_id=c_id, status='Pending').count()


        ###################   GRAPH FILTERS  #################

        #TODAY
        todays_total_orders = orders.filter(client_id=c_id, date_ordered__day=today).count()
        todays_delivered_orders = orders.filter(client_id=c_id, status='Delivered', date_ordered__day=today).count()
        todays_pending_orders = orders.filter(client_id=c_id, status='Pending', date_ordered__day=today).count()

        #YESTERDAY
        yesterday_total_orders = orders.filter(client_id=c_id, date_ordered__day=yesterday).count()
        yesterday_delivered_orders = orders.filter(client_id=c_id, status='Delivered', date_ordered__day=yesterday).count()
        yesterday_pending_orders = orders.filter(client_id=c_id, status='Pending', date_ordered__day=yesterday).count()

        #THIS WEEK
        week_ago_total_orders = orders.filter(client_id=c_id, date_ordered__gte=one_week_ago).count()
        week_ago_delivered_orders = orders.filter(client_id=c_id, status='Delivered', date_ordered__gte=one_week_ago).count()
        week_ago_pending_orders = orders.filter(client_id=c_id, status='Pending', date_ordered__gte=one_week_ago).count()

        #THIS MONTH
        this_month_total_orders = orders.filter(client_id=c_id, date_ordered__month=month).count()
        this_month_delivered_orders = orders.filter(client_id=c_id, status='Delivered', date_ordered__month=month).count()
        this_month_pending_orders = orders.filter(client_id=c_id, status='Pending', date_ordered__month=month).count()
        
        #THIS YEAR
        this_year_total_orders = orders.filter(client_id=c_id, date_ordered__year=year).count()
        this_year_delivered_orders = orders.filter(client_id=c_id, status='Delivered', date_ordered__year=year).count()
        this_year_pending_orders = orders.filter(client_id=c_id, status='Pending', date_ordered__year=year).count()

    except CreateOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = {}
        
        data['today_total_orders'] = todays_total_orders
        data['today_pending_orders'] = todays_pending_orders
        data['today_delivered_orders'] = todays_delivered_orders

        data['yesterday_total_orders'] = yesterday_total_orders
        data['yesterday_pending_orders'] = yesterday_pending_orders
        data['yesterday_delivered_orders'] = yesterday_delivered_orders

        data['week_ago_total_orders'] = week_ago_total_orders
        data['week_ago_pending_orders'] = week_ago_pending_orders
        data['week_ago_delivered_orders'] = week_ago_delivered_orders

        data['this_month_total_orders'] = this_month_total_orders
        data['this_month_delivered_orders'] = this_month_delivered_orders
        data['this_month_pending_orders'] = this_month_pending_orders

        data['this_year_total_orders'] = this_year_total_orders
        data['this_year_delivered_orders'] = this_year_delivered_orders
        data['this_year_pending_orders'] = this_year_pending_orders

        data['total_orders'] = total_orders
        data['total_pending_orders'] = total_pending_orders
        data['total_delivered_orders'] = total_delivered_orders
        

        return Response(data=data)