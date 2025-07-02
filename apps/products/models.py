from django.db import connection, IntegrityError


# Create your models here.

def create_products_table():
	"""
		Function to create the table products
		on the database, if this not exists.
	"""
	try:
		with connection.cursor() as cursor:
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS products(
					id SERIAL PRIMARY KEY,
					name VARCHAR(50) NOT NULL UNIQUE,
					price DECIMAL(10,2) NOT NULL,
					stock INT NOT NULL
				)
			""")

			cursor.execute("""
				CREATE INDEX IF NOT EXISTS idx_products on products (name)
			""")

	except IntegrityError as I:
		context = {
			"succes": False,
			"error": str(I)
		}
		return context


def create_categories_table():
	"""
		Function to create categories table on the
		database, if this not exist.
	"""
	try:
		with connection.cursor() as cursor:
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS categories(
					id SERIAL PRIMARY KEY,
					name VARCHAR(20) NOT NULL UNIQUE
				)
			""")
			cursor.execute("""
				CREATE INDEX IF NOT EXISTS idx_categories on categories(name)
			""")

	except IntegrityError as I:
		context = {
			"succes": False,
			"error": str(I)
		}
		return context


def create_product_categories_table():
	"""
		Function to create the product_categories table
		in the database, contains the many to many relation
		between both tables, products and catagories. 
	"""
	try:
		with connection.cursor() as cursor:
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS product_categories(
					product_id INT,
					category_id INT,
					PRIMARY KEY(product_id, category_id),
					FOREIGN KEY (product_id) REFERENCES products(id),
					FOREIGN KEY (category_id) REFERENCES categories(id)
				)
			""")

			cursor.execute("""
				CREATE INDEX IF NOT EXISTS idx_products
				on product_categories(product_id)
			""")

			cursor.execute("""
				CREATE INDEX IF NOT EXISTS idx_categories
				on product_categories(category_id)
			""")

	except IntegrityError as I:
		context = {
			"succes": False,
			"error": str(I)
		}
		return context