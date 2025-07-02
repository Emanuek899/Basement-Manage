from django.db import connection, IntegrityError

# Create your models here.
def create_providers_table():
	try:
		with connection.cursor() as cursor:
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS providers(
					id SERIAL PRIMARY KEY,
					name VARCHAR(50) NOT NULL,
					address VARCHAR(100) NOT NULL,
					phone_number1 VARCHAR(20) NOT NULL,
					phone_number2 VARCHAR(20) DEFAULT 'Not provided',
					email VARCHAR(100) NOT NULL
				)
			""")
	except IntegrityError as I:
		context = {
			"success": False,
			"error": str(I)
		}


def create_product_providers_table():
	"""
		Create table woth the relation many to many between
		tables products and providers.
	"""
	try:
		with connection.cursor() as cursor:
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS product_providers(
					product_id INTEGER,
					provider_id INTEGER,
					PRIMARY KEY (product_id, provider_id),
					FOREIGN KEY (product_id) REFERENCES products(id),
					FOREIGN KEY (provider_id) REFERENCES providers(id)
				)
			""")
			cursor.execute("""
				CREATE INDEX IF NOT EXISTS idx_product
				on product_providers(product_id)
			""")

			cursor.execute("""
				CREATE INDEX IF NOT EXISTS idx_provider
				on product_providers(provider_id)
			""")

	except IntegrityError as I:
		context = {
			"succes": False,
			"error": str(I)
		}
		return context