from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from datetime import datetime

from django.utils.dateparse import parse_datetime

from .models import BuatRencana

from accounts.models import UserAccount


class ListRencanaView(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = self.request.data
        # judul = data['judul']
        # isi = data['isi']
        # tgl_eks = data['tgl']
        user = data['user']

        get_role = UserAccount.objects.filter(
            user_id=user, role__is_kabid=True).select_related('role__bidang')
        if get_role:
            if get_role.filter(role__bidang__bidang_id=14):
                datas = BuatRencana.objects.filter(
                    user__role__bidang__bidang_id=14).values()
                # return Response(datas, content_type='application/json')
            if get_role.filter(role__bidang__bidang_id=16):
                datas = BuatRencana.objects.filter(
                    user__role__bidang__bidang_id=16).values()
                # return Response(datas, content_type='application/json')
        else:
            datas = BuatRencana.objects.filter(user__user_id=user).values()
        return Response(datas, content_type='applicaton/json')


class BuatRencanaView(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = self.request.data
        judul = data['judul']
        isi = data['isi']
        tgl = data['tgl']
        tgl_eks = datetime.strptime(tgl, '%Y-%m-%d %H:%M:%S')
        # tgl2 = datetime.strftime(tgl_eks, '%Y-%m-%d %H:%M:%S')
        # tgl_eks = data['tgl']
        # print(type(tgl_eks))
        # if judul or isi or tgl_eks is None:
        #     return Response({"error": "Semua harus di input"})
        # else:
        r_kerja = BuatRencana.objects.create(
            judul=judul, isi=isi, tgl_eksekusi=datetime.strftime(
                tgl_eks, '%Y-%m-%d %H:%M:%S'))
        r_kerja.save()
        return Response({"success": "Rencana Kerja Berhasil di buat"})
