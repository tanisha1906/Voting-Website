from django.contrib import admin
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.utils import timezone
from .models import UserProfile

class SessionAdmin(admin.ModelAdmin):
    def user_info(self, obj):
        session_data = obj.get_decoded()
        user_id = session_data.get('_auth_user_id')
        try:
            user = User.objects.get(id=user_id)
            return f"{user.username} ({user.email})"
        except User.DoesNotExist:
            return "Anonymous"

    def session_age_days(self, obj):
        return (timezone.now() - obj.expire_date).days

    list_display = ['session_key', 'user_info', 'expire_date', 'session_age_days']
    readonly_fields = ['session_key', 'expire_date']

admin.site.register(UserProfile)
admin.site.register(Session, SessionAdmin)
