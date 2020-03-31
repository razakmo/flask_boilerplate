from app.main import bp


@bp.route('/')
def home():
    return "Flask Boiler plate"
