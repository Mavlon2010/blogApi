from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q
from blog.models import Blog
from blog.serializers import BlogSerializer, mobileBlogDetailSerializer,mobileBlogListSerializer, mobileBlogSearchSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])  # LIST
def list_blogs(request):
    # /api/v1/blogs/
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(['GET'])  # RETRIEVE
def detail_blog(request, pk):
    # /api/v1/blog/<int:pk>/detail
    try:
        blog = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        data = {"detail": f"Blog {pk} is not found!"}
        return Response(data)

    serializer = BlogSerializer(blog)
    return Response(serializer.data)


@api_view(['GET'])
def search_blogs(request):
    # /api/v1/blogs/search/?title={}&desc={}
    title = request.query_params.get('title')
    desc = request.query_params.get('desc')

    if title and desc:
        blogs = Blog.objects.filter(Q(title__icontains=title), Q(description__icontains=desc))
    elif title:
        blogs = Blog.objects.filter(title__icontains=title)
    elif desc:
        blogs = Blog.objects.filter(description__icontains=desc)
    else:
        blogs = Blog.objects.all()

    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def list_mobile_blogs(request):
    # /api/v1/mobile_blogs/
    mobile_blogs = Blog.objects.all()
    serializer = mobileBlogListSerializer(mobile_blogs, many=True)
    return Response(serializer.data)


@api_view(['GET'])  # RETRIEVE
def detail_mobile_blogs(request, pk):
    # /api/v1/mobile_blogs/<int:pk>/detail
    try:
        blog = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        data = {"detail": f"Blog {pk} is not found!"}
        return Response(data)

    serializer = mobileBlogDetailSerializer(blog)
    return Response(serializer.data)


@api_view(['GET'])
def search_mobile_blogs(request):
    # /api/v1/mobile_blogs/search/?title={}&desc={}
    title = request.query_params.get('title')
    desc = request.query_params.get('desc')

    if title and desc:
        blogs = Blog.objects.filter(Q(title__icontains=title), Q(description__icontains=desc))
    elif title:
        blogs = Blog.objects.filter(title__icontains=title)
    elif desc:
        blogs = Blog.objects.filter(description__icontains=desc)
    else:
        blogs = Blog.objects.all()

    serializer = mobileBlogSearchSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def blogs_create(request):
    title = request.data.get('title')
    description = request.data.get('description')

    Blog.objects.create(title=title, description=description)
    return Response({"success": "OK"}, status=201)


@api_view(['POST'])
def blogs_create(request):
    try:
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            blog = serializer.save()
            responce_serializer = BlogSerializer(blog)
            return Response(data={"success": "Created OK", "detail": responce_serializer.data}, status=201)
        return Response(data=serializer.errors, status=400)
    except Exception as e:
        return Response(data={"errors": str(e)}, status=500)


@api_view(["PUT"])
def blogs_update(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    if blog:
        title = request.data.get("title")
        description = request.data.get("description")
        print(title)
        print(description)
        if not (title and description):
            return Response({"title": ["'title' kerak"], "description": ["'description' kerak"]})
        blog.title = title
        blog.description = description
        blog.save()
        return Response({"success": "Ma'lumot yangilandi"})
    else:
        return Response({"error": "Blog mavjud emas!"})


@api_view(['PUT'])  # PARTIAL UPDATE
def blogs_update(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    serializer = BlogSerializer(blog, request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"detail": "Hammasi muvoffaqiyatli yaratildi."}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def blogs_delete(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    blog.delete()
    return Response({"success": f"Blog id:{pk} muvoffaqiyatli o'chirildi"}, status=status.HTTP_204_NO_CONTENT)
