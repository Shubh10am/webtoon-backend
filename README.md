# Webtoons API

## Overview

The Webtoons API provides a robust interface for interacting with a webtoon application. It allows users to authenticate, manage webtoon entries, and retrieve webtoon details. This API is built using Flask and Flask-Restx, utilizing JWT for secure access.

## Table of Contents

1. [API Endpoints](#api-endpoints)
   - [Create Access Token](#1-create-access-token)
   - [Fetch All Webtoons](#2-fetch-all-webtoons)
   - [Add a Webtoon](#3-add-a-webtoon)
   - [Fetch Specific Webtoon Detail](#4-fetch-specific-webtoon-detail)
   - [Delete a Specific Webtoon](#5-delete-a-specific-webtoon)
2. [Utilities](#utilities)
3. [Requirements](#requirements)
4. [Setup](#setup)
5. [Notes](#notes)
6. [License](#license)

## API Endpoints

### 1. Create Access Token

- **Endpoint:** `/perform/create-token`
- **Method:** `POST`
- **Description:** Generates an access token for authenticated users.

#### Request Body:
```json
{
    "username": "shubh",
    "password": "shubh@12"
}
```

#### Response:
- **200 OK:**
  ```json
  {
      "status": "success",
      "message": "Login successful",
      "data": "ACCESS_TOKEN"
  }
  ```
- **401 Unauthorized:**
  ```json
  {
      "status": "error",
      "message": "Invalid credentials"
  }
  ```

---

### 2. Fetch All Webtoons

- **Endpoint:** `/perform/webtoons`
- **Method:** `GET`
- **Description:** Retrieves a list of all webtoons.

#### Response:
- **200 OK:**
  ```json
  {
      "status": "success",
      "message": "Webtoons fetched successfully",
      "data": [
          {
              "webtoons_id": "1",
              "title": "Webtoon Title",
              "description": "Description here",
              "characters": ["Character 1", "Character 2"]
          },
          ...
      ]
  }
  ```

---

### 3. Add a Webtoon

- **Endpoint:** `/perform/webtoons`
- **Method:** `POST`
- **Description:** Adds a new webtoon entry.
- **Authorization:** JWT token required.

#### Request Body:
```json
{
    "title": "Webtoon Title",
    "description": "Webtoon Description",
    "characters": ["Character 1", "Character 2"]
}
```

#### Response:
- **200 OK:**
  ```json
  {
      "status": "success",
      "message": "New Webtoon Entry Added"
  }
  ```

---

### 4. Fetch Specific Webtoon Detail

- **Endpoint:** `/perform/webtoons/<string:webtoons_id>`
- **Method:** `GET`
- **Description:** Fetches details of a specific webtoon by ID.

#### Response:
- **200 OK:**
  ```json
  {
      "status": "success",
      "message": "Webtoon fetched successfully",
      "data": {
          "webtoons_id": "1",
          "title": "Webtoon Title",
          "description": "Description here",
          "characters": ["Character 1", "Character 2"]
      }
  }
  ```
- **400 Bad Request:**
  ```json
  {
      "status": "error",
      "message": "No Webtoons Found from this ID"
  }
  ```

---

### 5. Delete a Specific Webtoon

- **Endpoint:** `/perform/webtoons/<string:webtoons_id>`
- **Method:** `DELETE`
- **Description:** Deletes a specific webtoon entry by ID.
- **Authorization:** JWT token required.

#### Response:
- **200 OK:**
  ```json
  {
      "status": "success",
      "message": "Webtoon Deleted Successfully"
  }
  ```
- **400 Bad Request:**
  ```json
  {
      "status": "error",
      "message": "No Webtoons details found from this webtoon ID"
  }
  ```

---

## Utilities

- **`format_response(data, status_code, message, custom_ob=None)`**: Standardizes API responses.
- **`data_envelope(serializer)`**: Wraps data with a specified serializer for consistent output.

## Requirements

- Python 3.x
- Flask
- Flask-JWT-Extended
- Flask-Restx
- MongoDB (or compatible database)

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your MongoDB connection.**

4. **Run the application:**
   ```bash
   flask run
   ```

## Notes

- The hardcoded credentials should be replaced with a secure authentication method in production.
- Manage JWT tokens securely to prevent unauthorized access.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
