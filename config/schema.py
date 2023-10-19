import graphene
from graphene_django import DjangoObjectType
from post_manager.models import Post, Comment


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ("id", "text", "owner", "node", "comments")


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = ("id", "post", "text", "owner", "node")


class Query(graphene.ObjectType):
    all_comments = graphene.List(CommentType)
    post_by_id = graphene.Field(PostType, id=graphene.Int(required=True))

    def resolve_all_comments(root, info):
        # We can easily optimize query count in the resolve method
        return Comment.objects.select_related("post").all()

    def resolve_post_by_id(root, info, id):
        try:
            return Post.objects.get(id=id)

        except Post.DoesNotExist:
            return None


schema_1 = graphene.Schema(query=Query)
