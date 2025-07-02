from django.db import connection, IntegrityError

def create_users_table():
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) NOT NULL UNIQUE,
                name VARCHAR(30) NOT NULL,
                lastname VARCHAR(30) NOT NULL, 
                email VARCHAR(100) NOT NULL UNIQUE,
                pass VARCHAR(20) NOT NULL,
                position TEXT NOT NULL CHECK(position IN ('Manager', 'Employee')),
                date_sign TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


def create_providers_table():
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


def create_products_table():
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
            CREATE INDEX IF NOT EXISTS idx_products ON products (name)
        """)


def create_categories_table():
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories(
                id SERIAL PRIMARY KEY,
                name VARCHAR(20) NOT NULL UNIQUE
            )
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_categories ON categories(name)
        """)


def create_product_categories_table():
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
            CREATE INDEX IF NOT EXISTS idx_products ON product_categories(product_id)
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_categories ON product_categories(category_id)
        """)


def create_product_providers_table():
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
            CREATE INDEX IF NOT EXISTS idx_product ON product_providers(product_id)
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_provider ON product_providers(provider_id)
        """)


def create_token_table():
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS token (
                id SERIAL PRIMARY KEY,
                key VARCHAR(64) NOT NULL,
                users INT NOT NULL,
                FOREIGN KEY (users) REFERENCES users(id)
            )
        """)


def run_all_creations():
    create_users_table()
    create_providers_table()
    create_products_table()
    create_categories_table()
    create_product_categories_table()
    create_product_providers_table()
    create_token_table()
