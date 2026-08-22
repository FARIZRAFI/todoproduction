from app.app import app


def test_app_exists():
    assert app is not None


def test_index_route():
    routes = [str(rule) for rule in app.url_map.iter_rules()]
    assert "/" in routes
