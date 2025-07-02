from django.db import models
from django.db import connection, IntegrityError, transaction

# Create your models here.
class Token(models.Model):
    key = models.CharField(max_length=64)
    users = models.ForeignKey('users.Users', models.DO_NOTHING, db_column='users')

    class Meta:
        managed = False
        db_table = 'token'


def validate_token(user_id):
    if user_id is None:
        return {"success": False}
        
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT EXISTS (
                    SELECT id FROM token WHERE users = %s
                ) 
            """, [user_id])
            result = cursor.fetchone()

        print(repr(result))

        if result is None:
            return {"success": False}
        return {"success": result[0]}

    except IntegrityError as I:
        return {"success": False, "error": str(I)}


def del_token(token):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                DELETE FROM token  WHERE key = %s
            """, [token])
            if cursor.rowcount > 0:
                return {"success": True, "message": "logout sucesfully"}
        return {"success": False, "message": "token does not exist"}
        
    except IntegrityError as Int:
        print(Int)
        return {"success": False, "error": str(Int)}
    
    except Exception as e:
        print(str(e))
        return {"success": False, "error": str(e)}