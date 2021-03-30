from django.db import models
from accounts.models import UserAccount


class BuatRencana(models.Model):
    judul = models.CharField(max_length=100)
    isi = models.TextField()
    tgl_eksekusi = models.DateTimeField()
    user = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_created=True, default=0)
    update_flag = models.IntegerField(default=0)

    def __str__(self):
        return str(self.judul)
