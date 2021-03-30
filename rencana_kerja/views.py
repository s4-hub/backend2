from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

from .models import BuatRencana

from accounts.models import UserAccount


class BuatRencanaView(APIView):

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
