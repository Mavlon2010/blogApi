from rest_framework import serializers

from blog.models import Blog


# MOBILE
class mobileBlogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class mobileBlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description']


class mobileBlogSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'updated']


# class BlogDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Blog
#         fields = ['id', 'title', 'description']
#
#
# class BlogListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Blog
#         fields = '__all__'
#
#
# class BlogSearchSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Blog
#         exclude = ['id']
#
#
# class BlogCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Blog
#         fields = '__all__'
#
#
# class BlogUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Blog
#         fields = '__all__'
#
#     def update(self, instance, validated_data):
#         print(validated_data.get('title', instance.title))
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.save()
#         return instance

class BlogSerializer(serializers.ModelSerializer):  # CRUD
    characters = serializers.SerializerMethodField()
    words = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'created', 'updated', 'characters', 'words']

    def get_characters(self, obj):
        return len(obj.description)

    def get_words(self, obj):
        return len(obj.description.split())
