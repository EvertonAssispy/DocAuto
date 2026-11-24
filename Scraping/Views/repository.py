
from urllib.parse import urlparse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers import RepositorioSerializer
from ..services.explorer import explorar


class ExplorarRepositorioView(APIView):

    def post(self, request):

        serializer = RepositorioSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        url = serializer.validated_data["url"]

        partes = urlparse(url).path.strip("/").split("/")

        if urlparse(url).netloc not in ["github.com", "www.github.com"] or len(partes) != 2:
            return Response(
                {"erro": "Informe uma URL válida de um repositório GitHub."},
                status=status.HTTP_400_BAD_REQUEST
            )

        usuario, repositorio = partes

        api_url = f"https://api.github.com/repos/{usuario}/{repositorio}/contents/"

        arquivos = explorar(api_url)

        return Response({
            "total": len(arquivos),
            "arquivos": arquivos
        })
