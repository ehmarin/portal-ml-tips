from app import create_app, db
from app.models import Product

app = create_app()

def seed_database():
    with app.app_context():
        db.create_all()
        
        if Product.query.first() is None:
            print("Iniciando carga de productos dummy para MLtips...")
            p1 = Product(
                nombre="Shampoo Revitalizante",
                descripcion="Shampoo especializado para el cuidado y brillo del cabello femenino.",
                precio=15.50,
                imagen_url="shampoo.jpg"
            )
            p2 = Product(
                nombre="Acondicionador Sedoso",
                descripcion="Acondicionador de hidratación profunda que deja el cabello suave y manejable.",
                precio=16.00,
                imagen_url="acondicionador.jpg"
            )
            p3 = Product(
                nombre="Crema para Peinar Moldeadora",
                descripcion="Crema para peinar sin enjuague para rizos perfectos y protección térmica.",
                precio=12.75,
                imagen_url="crema.jpg"
            )
            db.session.add_all([p1, p2, p3])
            db.session.commit()
            print("Base de datos inicializada y poblada exitosamente.")

if __name__ == "__main__":
    seed_database()