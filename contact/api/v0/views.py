from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

User = get_user_model()
from contact.models import Contact
from .serializers import contactserializer, contact1serializer


class SearchContact(generics.ListAPIView):

    filter_backends = (filters.SearchFilter,)
    queryset = Contact.objects.all()
    serializer_class = contactserializer

    def list(self, request, *args, **kwargs):
        query = request.query_params.get('search')
        context = {}
        data = {}
        if query.isnumeric():
            lis = Contact.objects.filter(Phone_number=query)
            for i in lis:
                if i.Registered_user:
                    context['success'] = True
                    context['status'] = 200
                    context['message'] = "successfully get"
                    serializer = contactserializer(i)
                    data = serializer.data
                    context['data'] = data
                    return Response(context)
            serializer = contactserializer(lis, many=True)
            context['success'] = True
            context['status'] = 200
            context['message'] = "successfully get"
            context['count'] = lis.count()
            data = serializer.data
            context['data'] = data
            return Response(context)
        else:
            context['success'] = True
            context['status'] = 200
            context['message'] = "successfully get"

            qs = Contact.objects.none()
            qs = Contact.objects.filter(Name__startswith=query)
            qs = qs | Contact.objects.filter(Name__contains=query).exclude(Name__startswith=query)
            serializer = contactserializer(qs, many=True)
            context['count'] = qs.count()
            data = serializer.data
            context['data'] = data
            return Response(context)


@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def markSpam(request, id):
    obj = get_object_or_404(Contact, pk=id)
    obj.Marked_by.add(request.user)
    obj.Marked_Spam_no = obj.Marked_by.count()
    obj.save()
    context = {'success': True, 'status': 200, 'message': "successful marked spam"}
    return Response(context)


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def detailView(request, id):
    obj = get_object_or_404(Contact, pk=id)
    context = {}
    data = {}
    qs = obj.In_List.all()
    print(request.user)
    print(qs)
    for i in qs:
        if request.user.id == i.id:
            if obj.Registered_user:
                context['success'] = True
                context['status'] = 200
                context['message'] = "successful get"
                serializer = contact1serializer(obj)
                data = serializer.data
                context['data'] = data
                return Response(context)
    res = contactserializer(obj)
    context['success'] = True
    context['status'] = 200
    context['message'] = "successful get"
    context['data'] = res.data
    return Response(context)
