from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    imagen_url = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<Product {self.nombre}>'
