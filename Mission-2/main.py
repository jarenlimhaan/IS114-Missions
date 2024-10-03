from app import CONFIG
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.config.from_mapping(
        {"DEBUG": True}
    )
    app.run(port=int(CONFIG["BACKEND_PORT"]))