from .models import Message
from import_export import resources


class MessageResource(resources.ModelResource):
    class Meta:
        model = Message
        fields = ('id', 'name', 'phone_number',)