from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ProductReview
from products.models import Product
from .forms import ProductReviewForm


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('product_details', product_id=product.id)
    else:
        form = ProductReviewForm()

    return render(request, 'reviews/add_review.html', {
        'form': form, 'product': product})


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(ProductReview, id=review_id, user=request.user)

    if request.method == 'POST':
        form = ProductReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('view_review')
    else:
        form = ProductReviewForm(instance=review)

    return render(request, 'reviews/edit_review.html', {
        'form': form, 'review': review})


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(ProductReview, id=review_id, user=request.user)

    if request.method == 'POST':
        review.delete()
        return redirect('view_review')

    return render(request, 'reviews/delete_review.html', {'review': review})


@login_required
def view_review(request):
    user_reviews = ProductReview.objects.filter(user=request.user)
    context = {
        'user_reviews': user_reviews,
    }

    return render(request, 'reviews/reviews.html', context)
