from rest_framework import serializers
from datetime import datetime
from .models import Filme


class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = '__all__'

    def validate_ano(self, value):
        ano_atual = datetime.now().year
        if value < 1900 or value > ano_atual:
            raise serializers.ValidationError(f"O ano deve estar entre 1900 e {ano_atual}.")
        return value