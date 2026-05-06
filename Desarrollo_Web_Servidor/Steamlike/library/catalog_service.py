import requests
from django.core.cache import cache

CHEAPSHARK_URL = "https://www.cheapshark.com/api/1.0/games"


class CatalogService:

    @staticmethod
    def search(query: str):
        """
        Lógica completa del endpoint /api/catalog/search/
        """
        cache_key = f"catalog_search:{query.strip().lower()}"

        # 1. Buscar en Redis
        cached = cache.get(cache_key)
        if cached:
            print("📦 Datos desde Redis")
            return cached, None

        # 2. Llamada externa
        print("🌐 Llamando a CheapShark")
        try:
            response = requests.get(
                CHEAPSHARK_URL,
                params={"title": query},
                timeout=5
            )
        except requests.RequestException:
            return None, "external_unavailable"

        if response.status_code != 200:
            return None, "external_error"

        cheapshark_data = response.json()

        # 3. Transformar datos (igual que tu vista actual)
        results = []
        for game in cheapshark_data:
            results.append({
                "external_game_id": game.get("gameID"),
                "title": game.get("external"),
                "thumb": game.get("thumb")
            })

        # 4. Guardar en Redis
        cache.set(cache_key, results, timeout=60 * 3)

        return results, None

    @staticmethod
    def resolve(external_ids: list[str]):
        """
        Lógica completa del endpoint /api/catalog/resolve/
        """
        try:
            response = requests.get(
                CHEAPSHARK_URL,
                params={"ids": ",".join(external_ids)},
                headers={"User-Agent": "PilarGiron-ProyectoSteamlike"},
                timeout=5
            )
        except requests.RequestException:
            return None, "external_unavailable"

        if response.status_code != 200:
            return None, "external_error"

        cheapshark_data = response.json()

        results = []
        for game_id, game_info in cheapshark_data.items():
            info = game_info.get("info", {})
            results.append({
                "external_game_id": game_id,
                "title": info.get("title"),
                "thumb": info.get("thumb")
            })

        return results, None