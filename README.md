# URL Shortener API

A lightweight, fast URL shortener built with **FastAPI**. This API converts long URLs into short, shareable codes, handles HTTP redirects, and tracks click analytics.

## Features

* **URL Shortening:** Generate unique short codes for long URLs.
* **Fast Redirection:** Redirects users to the original destination using standard HTTP `301` or `302` status codes.
* **Click Tracking:** Automatically increments a counter every time a short link is accessed.
* **Analytics Endpoint:** Retrieve total click counts and metadata for any short code.
* **Interactive Docs:** Auto-generated Swagger UI and ReDoc documentation out of the box.

---

## Tech Stack

* **Framework:** FastAPI
* **Server:** Uvicorn
* **Validation:** Pydantic
* **Database:** *SQLite*

---

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com
cd url-shortener-fastapi
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install fastapi uvicorn pydantic
```
*pip install .*

### 4. Run the development server
```bash
uvicorn main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

---

## API Endpoints

### 1. Shorten a URL
Creates a new short code for a given URL.

* **URL:** `/shorten`
* **Method:** `POST`
* **Request Body:**
```json
{
  "url": "https://example.com"
}
```
* **Success Response (`201 Created`):**
```json
{
  "code": "aB3d9X",
  "short_url": "http://127.0.0",
  "original_url": "https://example.com"
}
```

---

### 2. Redirect to Original URL
Redirects the client to the original URL and increments the click counter.

* **URL:** `/{code}`
* **Method:** `GET`
* **Response:** `302 Found` (or `301 Moved Permanently`) redirecting to the target `Location`.
* **Error Response (`404 Not Found`):**
```json
{
  "detail": "Short URL not found"
}
```

---

### 3. Get URL Statistics
Returns click metrics and details for a specific short code.

* **URL:** `/{code}/stats`
* **Method:** `GET`
* **Success Response (`200 OK`):**
```json
{
  "code": "aB3d9X",
  "original_url": "https://example.com",
  "clicks": 42,
  "created_at": "2026-11-21T19:00:00Z"
}
```

---

## Interactive Documentation

Once the server is running, you can test the endpoints directly in your browser using FastAPI's built-in documentation:

* **Swagger UI:** `http://127.0.0`
* **ReDoc:** `http://127.0.0`

---

## Example Usage (`cURL`)

**Create a short URL:**
```bash
curl -X POST "http://127.0.0" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://tiangolo.com"}'
```

**Test the redirect:**
```bash
curl -i "http://127.0.0"
```

**Check the stats:**
```bash
curl -X GET "http://127.0.0/stats"
```
