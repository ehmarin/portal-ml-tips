from flask import Blueprint, render_template, session, redirect, url_for, flash, request
from app.models import Product, User, Order, OrderItem
from app import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@bp.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    # Usaremos la sesión de Flask para guardar el carrito temporalmente
    if 'cart' not in session:
        session['cart'] = {}
    
    cart = session['cart']
    product_id_str = str(product_id)
    
    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1
        
    session.modified = True
    flash('Producto agregado al carrito exitosamente. 🌸', 'success')
    return redirect(url_for('main.index'))

@bp.route('/cart')
def cart():
    cart = session.get('cart', {})
    cart_items = []
    total = 0
    for product_id_str, quantity in cart.items():
        product = Product.query.get(int(product_id_str))
        if product:
            subtotal = product.precio * quantity
            total += subtotal
            cart_items.append({'product': product, 'quantity': quantity, 'subtotal': subtotal})
    return render_template('cart.html', cart_items=cart_items, total=total)

@bp.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart = session.get('cart', {})
    if not cart:
        flash('Tu carrito está vacío.', 'warning')
        return redirect(url_for('main.index'))
        
    if request.method == 'POST':
        # Simulación de pago y vaciado del carrito
        session.pop('cart', None)
        flash('¡Compra realizada con éxito! Gracias por confiar en MLtips. ✨', 'success')
        return redirect(url_for('main.index'))
        
    return render_template('checkout.html')