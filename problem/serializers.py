

from rest_framework import serializers
from problem.models import Question

class QuestionSeriazizer(serializers.ModelSerializer):

    assessment = serializers.StringRelatedField(read_only=True)
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:

        model = Question

        fields = "__all__"

        read_only_fields = ["id","assessment","created_at","updated_at","created_by"]