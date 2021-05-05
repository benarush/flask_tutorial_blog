from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint, jsonify)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post, User
from flaskblog.posts.forms import PostForm
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import datetime


posts = Blueprint('posts', __name__,)

@posts.route("/posts/api", methods=["GET"])
@jwt_required()
def get_posts():
    # Access the identity of the current user with get_jwt_identity
    current_user = User.query.filter_by(email=get_jwt_identity()).first()
    posts = []
    posts_q = Post.query.all()
    for post in posts_q:
        posts.append({'title': post.title, 'content': post.content, 'author': post.author.username,
                      'date_posted': post.date_posted})
    print(posts)
    return jsonify(posts=posts), 200

@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.content.data = post.content
        form.title.data = post.title
    return render_template('create_post.html', title='Update Post',
                               form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))


@posts.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)

