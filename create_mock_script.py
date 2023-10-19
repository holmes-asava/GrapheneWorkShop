user = User.objects.create()
author = Author.objects.create(user=user, node=Node.objects.create())
post = Post.objects.create(owner=author, node=Node.objects.create())
comment = Comment.objects.create(node=Node.objects.create(), owner=author, post=post)
