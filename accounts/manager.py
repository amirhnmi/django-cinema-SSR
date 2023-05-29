from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """a custom manager for create user and super user with email and password"""
    
    def create_user(self,email,password,**kwargs):
        """overwrite CreateUser method for create a user by email and password"""
        
        if not email:
            raise ValueError("user must have an email")
        
        email = self.normalize_email(email)
        user = self.model(email=email,**kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**kwargs):
        """overwrite createsuperuser method for create superuser by email and password"""
    
        kwargs.setdefault("is_staff",True)
        kwargs.setdefault("is_superuser",True)
        kwargs.setdefault("is_active",True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("super user must have is_staff=True")
        
        if kwargs.get("is_superuser") is not True:
            raise ValueError("super user must have is_superuser=True")
        
        if kwargs.get("is_active") is not True:
            raise ValueError("super user must have is_ctive=True")

        return self.create_user(email, password, **kwargs)