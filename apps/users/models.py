from django.db import connection, IntegrityError, transaction
import secrets
from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=100)
    pass_field = models.CharField(db_column='pass', max_length=20)  # Field renamed because it was a Python reserved word.
    position = models.TextField()
    date_sign = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = True
        db_table = 'users'


def insert_users(
    username, name,
    last_name, email,
    passw, position):
    """
        Function to insert new users to the database.
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO users (
                    username,
                    name,
                    lastname,
                    email,
                    pass,
                    position
                ) VALUES (%s, %s, %s, %s, %s, %s)
            """, [username, name, last_name, email, passw, position])
        return {'success': True}
    except IntegrityError as I:
        return {'success': False}


def del_user(user_id):
    """
        Function to delete a user of the database, based in
        the id.
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                DELETE FROM users WHERE id = %s
            """, [user_id])
            if cursor.rowcount < 1:
                return {"success": False, "message": "user does not exist"}
            
        return {"success": True, "message": "sucesfully deleted"}
    
    except IntegrityError as e:
        return {"success": False, "error": str(e)}


def valid_user(username, passw):
    """
        Function to validate if the user exist and create a token
        for the session.
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM users WHERE username = %s AND pass = %s
            """, [username, passw])
            row = cursor.fetchone()
        if row is None:
            return {"success": False}
        
        user_id = row[0]
        token = secrets.token_hex(32)
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO token (key, users)
                VALUES (%s, %s)
            """, [token, user_id])
        return {"success": True, "token": token}
    except IntegrityError as e:
        return {"success": False, "error": str(e)}


def get_id(user):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id FROM users WHERE username = %s
            """, [user])
            user_id = cursor.fetchone()
        if not user_id:
            return {"success": False, "message": "user does not exist"}
        return {"success": True, "user_id": user_id[0]}
    except IntegrityError as I:
        return {"success": False, "error": str(I)}

