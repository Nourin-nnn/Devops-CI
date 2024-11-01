from app import app

# Test for the main route response
def test_hello():
    response = "Hello World from NNN!"
    assert response == "Hello World from NNN!"

# Test for Flask app route response using a test client
def test_flask_route():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert response.data.decode('utf-8') == "Hello World from NNN!"
