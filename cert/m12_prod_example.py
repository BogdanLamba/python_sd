"""Modul de configurare flexibila pentru o aplicatie web."""


def create_endpoint(path: str, *methods, **options) -> dict:
    """Defineste un endpoint HTTP cu metode si optiuni flexibile.

    Args:
        path: Calea URL a endpoint-ului (ex. '/api/users').
        *methods: Metodele HTTP acceptate (GET, POST, etc.).
        **options: Optiuni suplimentare: auth, rate_limit, cache_ttl etc.

    Returns:
        Dict cu configuratia completa a endpoint-ului.

    Example:
        >>> create_endpoint('/api/users', 'GET', 'POST', auth=True)
        {'path': '/api/users', 'methods': ('GET', 'POST'), 'auth': True, ...}
    """
    defaults = {"auth": False, "rate_limit": 100, "cache_ttl": 0}
    config = {**defaults, **options}   # options suprascrie defaults

    return {
        "path": path,
        "methods": methods if methods else ("GET",),
        **config,
    }


_registry: list = []   # variabila globala de modul


def register_endpoint(path: str, *methods, **options) -> None:
    """Inregistreaza un endpoint in registrul global.

    Args:
        path: Calea URL.
        *methods: Metodele HTTP.
        **options: Optiuni endpoint.
    """
    global _registry
    endpoint = create_endpoint(path, *methods, **options)
    _registry.append(endpoint)
    print(f"Registered: {endpoint['path']} {endpoint['methods']}")


def get_registry() -> list:
    """Returneaza o copie a registrului de endpoint-uri."""
    return list(_registry)


if __name__ == "__main__":
    register_endpoint("/api/users",  "GET", "POST", auth=True)
    register_endpoint("/api/health", "GET", cache_ttl=60)
    register_endpoint("/api/login",  "POST", rate_limit=10)

    print(f"\nTotal endpoints: {len(get_registry())}")