from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import *

class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

    def validate_source(self,qiymat ):
        if not qiymat.endswith(".mp3"):
            raise ValidationError(detail="Bunaqa qo'shiq  formati yoq ")
        return qiymat


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

    def validate_date(self, qiymat):
        if qiymat <= "2000-01-01":
            raise ValidationError(detail="1970 yildan kattaroq yil kiriting")
        return qiymat


