def test_post_url(client):
    response = client.post("/urls/shorten", json={"url": "https://example.com"})
    assert response.status_code == 201
    data = response.json()
    assert "code" in data
    assert "short_url" in data
    assert data["original_url"] == "https://example.com/"

def test_redirect_to_original(client):
    # First, create a short URL
    response = client.post("/urls/shorten", json={"url": "https://example.com"})
    data = response.json()
    code = data["code"]

    # Now, test the redirect
    response = client.get(f"/urls/{code}", follow_redirects=False)
    assert response.status_code == 307  # Temporary Redirect
    assert response.headers["location"] == "https://example.com/"

def test_stats(client):
    response = client.post("/urls/shorten", json={"url": "https://example.com"})
    assert response.status_code == 201
    code = response.json()["code"]

    response = client.get(f"/urls/{code}/stats")
    assert response.status_code == 200
    data = response.json()
    assert data["short_code"] == code
    assert data["original_url"] == "https://example.com/"
    assert data["clicks"] == 0
    assert "created_at" in data